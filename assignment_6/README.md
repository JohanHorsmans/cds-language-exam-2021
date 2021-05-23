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
    <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021/blob/main/Language_Analytics_Exam.pdf"><strong>Link to PDF with all portfolio descriptions »</strong></a>
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
We have chosen the OffensEval2020 dataset containing 3000+ Danish comments from Ekstra Bladet and Reddit, labeled with a binary coding scheme indicating offensiveness (link: https://figshare.com/articles/dataset/Danish_Hate_Speech_Abusive_Language_data/12220805).

OffensEval2020 was a competition where researchers and data scientists from all over the world competed to create the best classification models for various languages (including Danish).

The best team in the Danish task achieved a macro F1-score of 0.8119 and the worst team achieved a score of 0.4913. For the full paper, see: https://arxiv.org/pdf/2006.07235.pdf

We wanted to create a text classifier that could classify offensive comments in Danish and compare our macro F1-score with the results from the OffensEval2020 competition.

We trained the following models: Logistic Regression, Support Vector Machine, Neural Network, Random Forest & Decision Tree (see code for further specifications). We also combined them in an ensemble where a mix of majority vote- and average ensembling was employed (see code for specifications). We have chosen to use macro F1-score as our metric:

The F1-score is a metric devised to fuse the relation between model precision and recall into a unified score. The metric is defined as taking the harmonic mean of precision and recall. The reason for using the harmonic mean, rather than the arithmetic mean, is that the harmonic mean of a recall-score of 0 and a precision-score of 100 would result in an F1-score of 0, rather than 50. This is advantageous, since it means that a model cannot achieve a high F1-score by having a high recall or precision by itself. The macro-averaging procedure of the macro F1-score involves calculating the arithmetic mean of the F1-score for each class.

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 5:
```bash
cd {root directory (i.e. cds-language-exam-2021}
cd assignment_6
python3 HateClass.py
```
<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following folders:

|Folder|Description|
|:--------|:-----------|
```data/``` | Folder containing a testing- and training dataset consisting over a 3.000 social media comments labeled after offensiveness (i.e. _NOT_ and _OFF_).

Furthermore, it holds the following files:
|File|Description|
|:--------|:-----------|
```HateClass.py``` | The python script for the assignment
```README.md``` | The README file that you are currently reading.

<!-- DISCUSSION OF RESULTS -->
## Discussion of results

Our best performing model was our ensemble containing all models, which achieved a macro F1-score of 0.71. It is important to note that the dataset is heavily skewed towards non-offensive comments, so the macro F1-score should be taken with a grain of salt. Nonetheless it would have ranked as the 23rd best model (out of 38) in the OffensEval2020 competition, so we deem it to be quite successful when taking the circumstances into account. For an even better model, see our [self-assigned project](https://github.com/JohanHorsmans/cds-language-exam-2021/tree/main/self_assigned), where we achieve a macro F1-score of XX on the same dataset.

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
