# system tools
import os
import sys
sys.path.append(os.path.join(".."))

# data munging tools
import pandas as pd
import numpy as np
import utils.classifier_utils as clf
from utils.neuralnetwork import NeuralNetwork


# Machine learning stuff
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit
from sklearn import metrics
from sklearn.metrics import balanced_accuracy_score, classification_report, plot_confusion_matrix
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree, svm
from sklearn.neural_network import MLPClassifier


def main():
    
    #Create filenames to load train and test data
    filename = os.path.join("data","Train_Hate.tsv")
    filename_test = os.path.join("data", "Test_Hate.tsv")

    #load Data    
    DATA = pd.read_csv(filename, index_col=0, sep="\t")
    DATA_TEST = pd.read_csv(filename_test, index_col=0, sep="\t")
    
    #Preprocessing: Dropping NA's 
    DATA = DATA.dropna()
    DATA_TEST = DATA_TEST.dropna()

    #Converting label-column to 0's and 1's
    DATA["subtask_a"] = np.where(DATA["subtask_a"] == 'NOT', 0, 1)
    DATA_TEST["subtask_a"] = np.where(DATA_TEST["subtask_a"] == 'NOT', 0, 1)
    
    #Dividing data into X and y variables
    X_train = DATA["tweet"]
    y_train = DATA["subtask_a"]
    X_test = DATA_TEST["tweet"]
    y_test = DATA_TEST["subtask_a"]
    
    #Vectorizing to make unigrams and bigrams and remove:
    #-frequently used words
    
    vectorizer = TfidfVectorizer(ngram_range = (1,2),
                             lowercase =  True,
                             max_df = 0.95)

    #Vectorize Training data
    X_train_feats = vectorizer.fit_transform(X_train)
    #Vectorize Test data
    X_test_feats = vectorizer.transform(X_test)
    #List feature names
    feature_names = vectorizer.get_feature_names()
    
    
    #Classifiers
    lr_classifier = LogisticRegression(random_state=42).fit(X_train_feats, y_train)

    #Logistic Regression predictions
    lr_predictions = lr_classifier.predict(X_test_feats)

    # Instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 100, random_state = 42)
    #Train the model on training data
    rf.fit(X_train_feats, y_train);

    #Random Forest predictions
    rf_predictions = rf.predict(X_test_feats)


    #Initialize SVM classifier
    clf_svm = svm.SVC(kernel='linear')
    
    #Fit SVM
    clf_svm = clf_svm.fit(X_train_feats, y_train)
    
    #Get SVM predictions
    svm_predictions = clf_svm.predict(X_test_feats)


    #Decicision tree
    clf_dt = tree.DecisionTreeClassifier()
    
    #Fit Decision tree
    clf_dt = clf_dt.fit(X_train_feats, y_train)

    #Get Decision tree predictions
    dt_predictions = clf_dt.predict(X_test_feats)


    #Neural Network
    clf_nn = MLPClassifier(solver='lbfgs', alpha=1e-5,
                         hidden_layer_sizes=(256, 128), random_state=1)


    #Fitting Neural network
    clf_nn = clf_nn.fit(X_train_feats, y_train)

    #Getting neural network predictions
    nn_predictions = clf_nn.predict(X_test_feats)
    

    #Creating ensemble predictions by adding them together and setting a threshold
    preds = np.where(rf_predictions+nn_predictions+dt_predictions+lr_predictions > 1.4, 1, 0)

    print("Confusion Matrix:")
    print(pd.crosstab(y_test, preds))

    print("Ckassification report:")
    print(classification_report(y_test, preds))
    
    print("A macro F1-score of .71 would place us in a 23rd place in the competition. Not bad for a computationally inexpensive ensemble model.")
    
if __name__=="__main__":
    main()

    
