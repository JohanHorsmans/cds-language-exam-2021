#!/usr/bin/env python
# coding: utf-8

# Import system tools:
import os 
import sys
sys.path.append(os.path.join(".."))

# Import spacy for performing NLP-tasks:
import spacy 

# Import pandas for creating dataframes:
import pandas as pd

# Import matplotlib for creating plots:
import matplotlib.pyplot as plt 

# Import SpacyTextBlob for sentiment analysis:
from spacytextblob.spacytextblob import SpacyTextBlob

# Initialize spaCy:
nlp = spacy.load("en_core_web_sm")

# Initialize spaCy text blob (sentiment analysis tool) and add it as a a component to the spaCy nlp-pipeline:
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

# Define the main function of the script: 
def main():
    
    # Specify that if there does not exist a folder called "out", in the directory of the script, it is to be made:
    if not os.path.exists("out"):
            os.makedirs("out")

    print("[INFO]: Loading data")
    # Loading data
    in_file = os.path.join("data", "abcnews-date-text.csv") # Specify path to data.
    headlines = pd.read_csv(in_file) # Read the .csv-file as a dataframe called 'headlines'.

    print("[INFO]: Preprocessing data")
    # Preprocessing:
    headlines['publish_date'] = pd.to_datetime(headlines.publish_date, format="%Y%m%d") # Converting the publish_date to a datetime format. Following the output above I specify that the dates are arranged as years, months, days (%Y%m%d). Y is upper case since the year is specified with century (i.e. four numbers).  
    
    # Sorting the dates in chronological order:
    headlines = headlines.sort_values("publish_date") 
    
    #To reduce processing time, I take a sample of 100.000 comments. If you wish to process the full data just remove this line of code:
    headlines = headlines.sample(100000) 

    print("[INFO]: Calculating sentiment scores")
    
    # Define empty list for sentiment-scores:
    sentiment_scores = [] 

    # Calculate sentiment scores:
    for doc in nlp.pipe(headlines["headline_text"], batch_size=500): # For each headline in the "headline_text"-column (iterated chronologically)...
        score = doc._.sentiment.polarity #... calculate text polarity and save it as 'score'...
        sentiment_scores.append(score) #... append 'score' to the 'sentiment_scores'-list

    # Add list with the sentiment scores ass a column in the headlines-dataframe:
    headlines["sentiment_score"] = sentiment_scores

    # Compute mean sentiment score for week and month:
    mean_week = headlines.resample("w",on ="publish_date").mean()
    mean_month = headlines.resample("m",on ="publish_date").mean()

    print("[INFO]: Making plots")
    # Make plot of the weekly rolling mean of sentiment scores:
    week_plot = mean_week.plot(
        ylabel = "Sentiment Score", # Define the label for the y-axis.
        xlabel = "Date", # Define the label for the x-axis.
        ylim = (-0.2,0.2), # Set the window size on the y-axis.
        title = "Weekly rolling mean of sentiment scores") # Set plot title

    # Save week_plot:
    mean_week_plot = week_plot.get_figure()
    mean_week_plot.savefig(os.path.join("out", "mean_week_plot"))

    # Make plot of the monthly rolling mean of sentiment scores:
    month_plot = mean_month.plot(
        ylabel = "Sentiment Score", # Define the label for the y-axis.
        xlabel = "Date", # Define the label for the x-axis.
         ylim = (-0.2,0.2), # Set the window size on the y-axis.
        title = "Monthly rolling mean of sentiment scores") # Set plot title
    
    print("[INFO]: Saving plots")
    
    # Save month_plot:
    mean_month_plot = month_plot.get_figure()
    mean_month_plot.savefig(os.path.join("out", "mean_month_plot"))
    
    print("[INFO]: Saving .csv-file with sentiment-scores")
    
    # Write the "headlines"-dataframe as a .csv-file called 'sentiment.csv:
    headlines.to_csv(os.path.join("out", "sentiment.csv")) 

if __name__=="__main__":
    main()