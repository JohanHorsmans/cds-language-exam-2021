<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-language-exam-2021">
    <img src="../README_images/nlp2.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Assignment 6</h3> 

  <p align="center">
    Johan Kresten Horsmans
    <br />
    <a href="https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/Language_Analytics_Exam.pdf"><strong>Link to PDF with all portfolio descriptions »</strong></a>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#official-description-from-instructor">Official description from instructor</a></li>
    <li><a href="#methods">Methods</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure and contents</a></li>
    <li><a href="#discussion-of-results">Discussion of results</a></li>
  </ol>
</details>

<!-- OFFICIAL DESCRIPTION FROM INSTRUCTOR -->
## Official description from instructor

### Text classification using Deep Learning

Winter is... hopefully over.

In class this week, we've seen how deep learning models like CNNs can be used for text classification purposes. For your assignment this week, I want you to see how successfully you can use these kind of models to classify a specific kind of cultural data - scripts from the TV series Game of Thrones.

You can find the data here: https://www.kaggle.com/albenft/game-of-thrones-script-all-seasons

In particular, I want you to see how accurately you can model the relationship between each season and the lines spoken. That is to say - can you predict which season a line comes from? Or to phrase that another way, is dialogue a good predictor of season?

Start by making a baseline using a 'classical' ML solution such as CountVectorization + LogisticRegression and use this as a means of evaluating how well your model performs. Then you should try to come up with a solution which uses a DL model, such as the CNNs we went over in class.

__Tips__
* Think carefully about the kind of preprocessing steps your text data may require and document these decisions.
* Think just as carefully about the kind of parameters you use in you model. They all make a difference!
* Some sentences are very short; some are longer. Think about how you should handle this.

__General instructions__
* You should upload standalone .py script(s) which can be executed from the command line - one for the LogisticRegression model and one for the DL model.
* You must include a requirements.txt file and a bash script to set up a virtual environment for the project You can use those on worker02 as a template
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line

__Purpose__
This assignment is designed to test that you have an understanding of:

* how to build CNN models for text classification;
* how to use pre-trained word embeddings for downstream tasks;
* how to work with real-world, complex cultural text data.

<!-- METHODS -->
## Methods
The problem of the assignment relates to classifying complex textual data using, respectively, a logistic regression- and a deep learning classifier. For both models, I preprocess the data and split it into a training- and testing set (with 25% of the sentences allocated to the testing-set). For the logistic regression classifier, I use the LogisticRegression-model from the sklearn.linear_model module. For the deep learning classifier, I utilize the pretrained [_GloVe word-embeddings_](https://nlp.stanford.edu/projects/glove/). 

Word embeddings are basically a big vector representation of how words are located in an abstract word-space, where related entities are placed in close proximity of each other. Such a vector representation implies (conceptually) that if one, for example, took the embedding for the word king and subtracted the embedding for the word man and followingly added the embedding for woman, one should be left with the embedding for the word queen, i.e.:

<p align="center">
    king - man + woman = queen
</p>

The reason for using these embeddings is that this representation of how words are related to one another should help my model make better predictions. By computing how different words relate to each other, the model can potentially infer how classifications of some sentences can extend to other similar sentences. This is a phenomenon referred to as transfer learning. To utilize the pre-trained embeddings on a classification task, such as this, one just needs to add a neural network to the end of the GloVe embedding layer. 

The neural network that I added consisted of the following; a convolutional layer with ReLU-activation, a max-pooling layer, a dense layer with 128 neurons and ReLU-activation and an output layer with 8 nodes (1 for each class).

For the Logistic Regression model i vectorize the data and transfrom it to lowercased unigrams and bigrams with tf-idf transformation. For the Deep Learning model i binarize the labels and tokenize the text. I then convert the data to an embedding matrix with either 50, 100, 200 or 300 dimensions (specified as an argument from the terminal).

For the deep learning model, I made it possible to specify training epochs and embedding-dimensions from the terminal using argparse.

I have decided to use the macro F1-score as my evaluation metric. For the reason behind this, please refer to [assignment 5, methods](https://github.com/JohanHorsmans/cds-language-exam-2021/tree/main/assignment_5#methods).

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 5:
```bash
cd {root directory (i.e. cds-language-exam-2021)}
cd assignment_6
python3 GoT_lr.py
python3 GoT_dl.py
```

You can specify the following optional argument from the terminal in the ```GoT_dl.py```-script:

_Epochs:_
```bash
"-e", "--epochs"
default = 10
type = int, 
help = "int, number of training epochs for the neural network [DEFAULT]: 10"
```

_Embedding-size:_
```bash
"-es", "--embedding_size", 
default = 50, 
type = int, 
help = "int, the size of the word embeddings loaded from the the GloVe-model. Options: 50, 100, 200, 300 [DEFAULT]: 50")
```

<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following folder:

|Folder|Description|
|:--------|:-----------|
```data/``` | Folder containing a csv-file with the script from every season of _Game of Thrones_.

Furthermore, it holds the following files:
|File|Description|
|:--------|:-----------|
```GoT_lr.py``` | The python script for the logistic regression model in this assignment.
```GoT_dl.py``` | The python script for the deep learning model in this assignment.
```README.md``` | The README file that you are currently reading.

<!-- DISCUSSION OF RESULTS -->
## Discussion of results

For the logistic regression model, I achieved a macro F1-score of 0.25. For the deep-learning model, I achieved a macro F1-score of 0.20 after training for 20 epochs using a word embedding size of 300 features. These results are not impressive but they act as a nice illustration of the complexity of the task. To improve results, I hypothesize that it would be beneficial to use word enitity recognition to extract the names present in the sentences and use that as a predictor of the season. Especially for a show such as Game of Thrones where many characters die in every season, I believe that this could greatly improve results.

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
