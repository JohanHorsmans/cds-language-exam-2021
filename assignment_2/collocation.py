#!/usr/bin/python

# Import system tools:
import os 
import sys
sys.path.append(os.path.join(".."))

# Import argparse to specify arguments in the script from the commandline:
import argparse 

# Import re for regular expression-tools:
import re

# Import Counter from collections for count-tools:
from collections import Counter

# Import pandas for working with dataframes
import pandas as pd

# Import Path for dealing with filepaths:
from pathlib import Path

# Import math for mathematical functions:
import math

# Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A function designed to calculate collocates for a specific keyword across a text-corpus. The following argument can be specified but you can also run the code with default parameters:")

ap.add_argument("-f", "--filepath", default = "data", type = str, help = "string, path to text-corpus. Texts need to be .txt-files. Be wary of difference in operating systems in terms of spcifying path with \" / \" or \" \ \" [DEFAULT]: data")

ap.add_argument("-k", "--keyword", default = "california", type = str, help = "string, the keyword for which you wish to find collocates and calculate metrics. [DEFAULT]: california")

ap.add_argument("-w", "--window_size", default = 2, type = int, help = "integer, collocate window-size. [DEFAULT]: 2")

# Parse the arguments:
args = vars(ap.parse_args())

# Define the main function of the script and what parameters it takes: 
def main(filepath, keyword, window_size): #Define a function with three parameters, "filepath", "keyword" & "window_size".
    
    #Defining empty lists for appending variables:
    u = []
    collocates = []
    collocate_word = []
    O11 = []
    O12 = []
    all_words = []
    
    for text in Path(filepath).glob("*.txt"): #Loop through all .txt-files in the filepath...
        with open(text, "r", encoding="utf-8") as text: #open the contents of the .txt-file.
            loaded_text = text.read() #load the contents of the .txt-file.
            loaded_text = loaded_text.lower() #use the lower-method to make all letters in the text lowercase to ensure that identical words with different casing are regarded as the same word.
            regex = re.compile('[^a-zA-Z\s]') #use regular expression to define special characters which I want to delete. \s is whitespace, a-zA-Z - matches all the letters, ^ - negates them all so it deletes everything else. This is done to ensure that, i.e., "fish." and "Fish!" are recognized as identical words.
            loaded_text = regex.sub('', loaded_text) #remove words defined in the above regular expression.
        t = -1 #Define indexing-variable, t, as -1
        loaded_text = loaded_text.split() #Split text into individual words.
        all_words.append(loaded_text) #Append the text to a list that will be hold all words in the texts.
        while True: #While true (i.e. as long as possible)...
            try: #... do the following:
                t = loaded_text.index(keyword, t + 1) #Try to find keyword at t + 1 (where t increases by 1 iteratively).
                keyword = loaded_text[t] #Save keyword to variable called "keyword".
                lower_window = loaded_text[t-window_size:t] #Define lower window.
                upper_window = loaded_text[t+1:t+window_size+1] #Define upper window.
                u.append(loaded_text[t]) #Append the keyword to the "u"-list.
                collocates.extend(lower_window + upper_window) #Add the words from the lower- and upper window to the "collocates-list".
            except ValueError: 
                break
    
    #Flatten the "all_words"-list to a single line with no breaks:
    all_words_flat = [] 
    for sublist in all_words:
        for item in sublist:
            all_words_flat.append(item)

    #Calculate O11:
    collocates = (" ".join(collocates)) #Transform "collocates"-lists into a single string. 
    collocates = collocates.split() #Split collocates-string into individual words.
    collocate_count = Counter(collocates).most_common(len(collocates)) #Count unique words and their apperance. The reason for using the most_common specifications is that it gives a tuple as an output, which can be indexed. 
        
    for i in list(range(0,len(collocate_count))): #For each element in the collocate...
        collocate_word.append(collocate_count[i][0]) #... Append the word to the "collocate_word"-list.
        O11.append(collocate_count[i][1]) #... Append the count of the word to the "O11"-list.

    #Calculate O12:
    for word in collocate_word: #For each word in the callocates...
        O12.append(all_words_flat.count(word)) #... append how often the word appears in the entire corpus to the "O12"-list.
    
    for i in list(range(0, len(collocate_word))): #For the amount of words in "collocate_words"...
        O12[i] = O12[i]-O11[i] #...iterate through the O12 list and replace the values with O12 - O11 (iteratively).
        
    #Calculate R1:
    R1 = list(range(0, len(collocate_word))) #Make a list called "R1" with integers ranging from zero to the number of collocates.

    for i in R1: #For each element in the "R1"-list.
        R1[i] = O12[i]+O11[i] #...Replace R1-value with O12 + O11 (iteratively).

    #Calculate O21:
    O21 = list(range(0, len(collocate_word))) #Make a list called "O21" with integers ranging from zero to the number of collocates.
        
    for i in O21: #For each element in the "O21"-list.
        O21[i] = len(u) - O11[i] #...Replace O21-value with O11 (iteratively) subtracted from the amount keywords in total.

    #Calculate C1:
    C1 = list(range(0, len(collocate_word))) #Make a list called "C1" with integers ranging from zero to the number of collocates.
    
    for i in C1: #For each element in the "C1"-list.
        C1[i] = O11[i] + O21[i] #...Replace C1-value with O11 + O21 (iteratively).

    #Calculate N:
    N = len(all_words_flat) #Calculate the total amount of words.

    #Calculate E11:
    E11 = list(range(0, len(collocate_word))) #Make a list called "C1" with integers ranging from zero to the number of collocates.
    
    for i in E11: #For each element in the "C1"-list.
        E11[i] = (R1[i]*C1[i])/N #...Replace C1-value with (R1*C1)/N (iteratively).

    #Calculate MI:
    MI = list(range(0, len(collocate_word))) #Make a list called "MI" with integers ranging from zero to the number of collocates.
    
    for i in MI: #For each element in the "C1"-list.
        MI[i] = math.log((O11[i]/E11[i])) #... Calculate the MI-score.
        
#Writing .CSV-file:

    # Specify that if there does not exist a folder called "out", in the directory of the script, it is to be made:
    if not os.path.exists("out"):
            os.makedirs("out")
    
    dict = {'collocate': collocate_word, 'raw_frequency': O11, 'MI': MI} #Create a dictionary with the column-names and values for the .CSV-file
    df = pd.DataFrame(dict) #Creating a pandas-dataframe using the above dictionary.
    df = df.sort_values("MI", ascending = False) #Sorting the dataframe so the MI column is sorted after score (high -> low).
    df.to_csv(f'out/{keyword} - window_size_{window_size}.csv') #Write the dataframe to the "out"-folder as a .csv-file called {keyword} - window_size_{window_size}.csv' .

#If the script is called from the commandline make filepath the first argument, keyword the second argument and window_size the third argument:
if __name__=="__main__":
    main(
    args["filepath"],
    args["keyword"],
    args["window_size"])

    