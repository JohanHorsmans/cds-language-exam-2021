#!/usr/bin/env python

# Import system tools:
import os
import sys
sys.path.append(os.path.join(".."))

# Import pandas for working with dataframes:
import pandas as pd

# Import numpy for working with arrays:
import numpy as np

# Import the classifier utility-function as 'clf': 
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.metrics import balanced_accuracy_score, classification_report, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit
from sklearn import metrics
from sklearn.preprocessing import LabelBinarizer

# Import tensforlow ann tools from tensorflow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, Embedding, 
                                     Flatten, GlobalMaxPool1D, Conv1D)
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras import backend as K
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.regularizers import L2

# Import argparse to specify arguments in the script from the commandline:
import argparse

# Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A script designed to classify Game of Thrones seasons based on dialogue with a neural network. The following arguments can be specified but you can also run the code with default parameters:")

ap.add_argument("-e", "--epochs", default = 10, type = int, help = "int, number of training epochs for the neural network [DEFAULT]: 10")

ap.add_argument("-es", "--embedding_size", default = 50, type = int, help = "int, the size of the word embeddings loaded from the the GloVe-model. Options: 50, 100, 200, 300 [DEFAULT]: 50")

# Parse the arguments:
args = vars(ap.parse_args())

# Define the main function of the script and what parameters it takes: 
def main(epochs, embedding_size):
    
    # Define helper function to load the saved GloVe embeddings and build an embedding matrix:
    def create_embedding_matrix(filepath, word_index, embedding_dim):
        vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
        embedding_matrix = np.zeros((vocab_size, embedding_dim))

        with open(filepath) as f:
            for line in f:
                word, *vector = line.split()
                if word in word_index:
                    idx = word_index[word] 
                    embedding_matrix[idx] = np.array(
                        vector, dtype=np.float32)[:embedding_dim]

        return embedding_matrix
    
    # Define path to the dataset:
    filename = os.path.join("data", "Game_of_Thrones_Script.csv")

    # Read the data and save it as a variable called "GoT".
    GoT = pd.read_csv(filename)
    
    # Save the "Sentence"-column from the GoT-data and save it as a variable called "sentences"
    sentences = GoT['Sentence'].values
    
    # Save the "Season"-column from the GoT-data and save it as a variable called "labels"
    labels = GoT['Season'].values

    # Create and testing- and training data split using sk.learn. Specify
    X_train, X_test, y_train, y_test = train_test_split(sentences, # X-input
                                                        labels, # y-input
                                                        test_size=0.25, # Specify that 25% of the data should be added to the test-set.
                                                        random_state=24) # Set random state for reproducibility.

    # Use LabelBinarizer to transform the labels to a binary one-vs-all fashion (to make it compatible with the neural network):
    lb = LabelBinarizer()
    y_train = lb.fit_transform(y_train)
    y_test = lb.fit_transform(y_test)
    
    # Initialize tokenizer to convert text to numbers:
    tokenizer = Tokenizer(num_words=None)

    # Fit tokenizer to training data
    tokenizer.fit_on_texts(X_train)

    # Tokenize training- and testting data:
    X_train_toks = tokenizer.texts_to_sequences(X_train)
    X_test_toks = tokenizer.texts_to_sequences(X_test)

    # Define overall vocabulary size:
    vocab_size = len(tokenizer.word_index) + 1 # Adding 1 due to the reserved 0 index in Python.
    
    # To make the tokenizer-output work, we need to pad the documents to have idential length.
    maxlen = len(max(X_train, key=len)) # Set the max-length to be the longest sentence in the dataset. This is done to ensure that no data is lost.

    # Pad the training data to the maximum length defined above:
    X_train_pad = pad_sequences(X_train_toks, 
                                padding='post', # sequences can be padded "pre" or "post" (post means adding 0s to the end of the sequence)
                                maxlen=maxlen)

    # Pad the training data to the maximum length defined above:
    X_test_pad = pad_sequences(X_test_toks, 
                               padding='post', 
                               maxlen=maxlen)
    
    # If the "glove.6B.zip" file does not exist in the directory then download it and unzip it. If it does exist, do nothing:
    if not os.path.exists("glove.6B.zip"):
        os.system('wget http://nlp.stanford.edu/data/glove.6B.zip')
        os.system('unzip glove.6B.zip')

    # Set the embedding dimensions to be the same as the specified embedding_size argument:
    embedding_dim = embedding_size

    # Use the previously defined helper function to build an embedding matrix using the GloVe-model (with the specified embedding size):
    embedding_matrix = create_embedding_matrix(os.path.join(f"glove.6B.{embedding_size}d.txt"),
                                               tokenizer.word_index, 
                                               embedding_dim)
    
    # Initialize Sequential model to build neural network
    model = Sequential()

    # add Embedding layer
    model.add(Embedding(input_dim=vocab_size,       # There should be as many input nodes as there are words generated by the Tokenizer()
                        output_dim=embedding_dim,   # Add defined embedding size
                        input_length=maxlen,        # Add max length of padded sentences 
                        weights=[embedding_matrix], # Add pretrained GloVe weights
                        trainable=False))           # Make sure that the embeddings are static so we fine-tune rather than train from scratch.

    # CONV+ReLU -> MaxPool -> FC+ReLU -> Out
    
    # Add convolutional layer with ReLU-activation:
    model.add(Conv1D(128, 5, 
                    activation='relu'))

    # Add max-pooling layer:
    model.add(GlobalMaxPool1D())

    # Add Dense layer with 10 neurons and ReLU-activation
    model.add(Dense(10, 
                    activation='relu'))

    # Add output layer with 8 nodes; 1 for each class (i.e. season):
    model.add(Dense(8, 
                    activation='softmax'))

    # Compile model:
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Train the model for specified number of epochs:
    history = model.fit(X_train_pad, y_train,
                        epochs=epochs,
                        verbose=False,
                        validation_data=(X_test_pad, y_test),
                        batch_size=10)
    

    # Predict the testing data:
    dl_predictions = model.predict(X_test_pad)
    
    # Make labels integers rather than float-probabilities:
    dl_predictions=np.argmax(dl_predictions, axis=1)
    y_test=np.argmax(y_test, axis=1)
    
    # Print classification matrix to the terminal:
    print(classification_report(y_test, dl_predictions))

#If the script is called from the command-line make epochs the first argument and embedding_size the second argument:
if __name__ =="__main__":
    main(
    args["epochs"],
    args["embedding_size"])