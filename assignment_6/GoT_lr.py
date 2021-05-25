#!/usr/bin/env python

# Import system tools:
import os
import sys
sys.path.append(os.path.join(".."))

# Import pandas for working with dataframes:
import pandas as pd

# Import the classifier utility-function as 'clf': 
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.metrics import balanced_accuracy_score, classification_report, plot_confusion_matrix

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MaxAbsScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit
from sklearn import metrics

# Set seed for reproducibility:
import random
random.seed(10)

# Define the main function of the script:
def main():
    
    # Define path to the dataset:
    filename = os.path.join("data", "Game_of_Thrones_Script.csv")

    # Read the data and save it as a variable called "GoT".
    GoT = pd.read_csv(filename)

    # Save the "Sentence"-column from the GoT-data and save it as a variable called "sentences"
    sentences = GoT["Sentence"].values
    
    # Save the "Season"-column from the GoT-data and save it as a variable called "labels"
    labels = GoT["Season"].values
    
    X_train, X_test, y_train, y_test = train_test_split(sentences, # X-input
                                                        labels, # y-input
                                                        test_size=0.25, # Specify that 25% of the data should be added to the test-set.
                                                        random_state=24) # Set random state for reproducibility.
    
    # Define that I want to use TF-IDF vectorization:
    vectorizer = TfidfVectorizer(ngram_range = (1,2),
                                 lowercase =  True,
                                 max_df = 0.95)
    
    # Vectorize Training data
    X_train_feats = vectorizer.fit_transform(X_train)
    
    # Vectorize Test data
    X_test_feats = vectorizer.transform(X_test)
        
    # Fit Logistic Regression model:
    lr_classifier = LogisticRegression(random_state=24).fit(X_train_feats, y_train)

    # Predict the testing-data using the fitted Logistic Regression model
    lr_predictions = lr_classifier.predict(X_test_feats)
    
    # Print classification matrix to the terminal:
    print(classification_report(y_test, lr_predictions))
    
#If the script is called from the command-line run the main-function:
if __name__ =="__main__":
    main()