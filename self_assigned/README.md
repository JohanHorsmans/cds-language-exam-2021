<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-language-exam-2021">
    <img src="../README_images/nlp2.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center"><ins>Self Assigned Project:</ins>

Danish hate speech detection</h3> 

  <p align="center">
    Johan Kresten Horsmans & Gustav Aarup Lauridsen
    <br />
    <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021/blob/main/Language_Analytics_Exam.pdf"><strong>Link to PDF with all portfolio descriptions »</strong></a>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#official-description-from-instructor">Official description from instructor</a></li>
    <li><a href="#methods">Methods</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure and contents</a></li>
    <li><a href="#discussion-of-results">Discussion of results</a></li>
  </ol>
</details>

<!-- CONTRIBUTION -->
## Contribution
I have made and designed the project assignment with [Gustav Aarup Lauridsen](https://github.com/Guscode). Gustav and I contributed equally to every stage of this project from initial conception and implementation, through the production of the final output and structuring of the repository. (50/50%)

<!-- OFFICIAL DESCRIPTION FROM INSTRUCTOR -->
## Project description

### Danish hate speech detection
For our self-assigned project, we wish to see if we can improve the Danish hate-speech detection algorithm that we designed for assignment 5. Here, we achieved a macro F1-score of 0.71. The current state-of-the-art, as described in [_OffensEval2020_](https://arxiv.org/pdf/2006.07235.pdf), achieves a macro F1-score of 0.81. Our goal with this project is to beat this score and build a new state-of-the-art model. We wish to do this using the new [_Ælæctra_](https://github.com/MalteHB/-l-ctra)-architecture. First, we wish to train an Ælektra-model on the official OffensEval2020-dataset (model 1). Followingly, we want to see if we can improve the model's classifications by expanding the training dataset by machine translating comments from an English hate-speech-dataset to Danish and then train an Ælæktra-model on this expanded dataset (model 2).

Following this we are going to upload the best-performing model to [_huggingface_](huggingface.co) and build a .py-script and a Jupyter notebook designed to easily help users deploy the model from huggingface on their own data. 

In summary, the project is comprised of the following steps:
1. Train and test an Ælæktra-model on the official OffensEval2020-dataset
2. Machine translate English hate-speech-data to Danish and use it to expand the Danish dataset.
3. Train an Ælæktra-model on the expanded dataset and test it on the OffensEval2020 testing-data
4. Upload the best model to huggingface.co
5. Create a Jupyter notebook and .py-script designed to help users deploy the model on their own data.


<!-- METHODS -->
## Methods

__NOTE: Some parts of the following section is repeated from [_assignment 5_](https://github.com/JohanHorsmans/cds-language-exam-2021/tree/main/assignment_5)__

We have chosen the OffensEval2020 dataset containing 3000+ Danish comments from Ekstra Bladet and Reddit, labeled with a binary coding scheme indicating offensiveness (link: https://figshare.com/articles/dataset/Danish_Hate_Speech_Abusive_Language_data/12220805).

OffensEval2020 was a competition where researchers and data scientists from all over the world competed to create the best classification models for various languages (including Danish).

The best team in the Danish task achieved a macro F1-score of 0.8119 and the worst team achieved a score of 0.4913. For the full paper, see: https://arxiv.org/pdf/2006.07235.pdf

We wanted to create a text classifier that could classify offensive comments in Danish and compare our macro F1-score with the results from the OffensEval2020 competition.

We trained the following models: Logistic Regression, Support Vector Machine, Neural Network, Random Forest & Decision Tree (see code for further specifications). We also combined them in an ensemble where a mix of majority vote- and average ensembling was employed (see code for specifications). We have chosen to use macro F1-score as our metric:

The F1-score is a metric devised to fuse the relation between model precision and recall into a unified score. The metric is defined as taking the harmonic mean of precision and recall. The reason for using the harmonic mean, rather than the arithmetic mean, is that the harmonic mean of a recall-score of 0 and a precision-score of 100 would result in an F1-score of 0, rather than 50. This is advantageous, since it means that a model cannot achieve a high F1-score by having a high recall or precision by itself. The macro-averaging procedure of the macro F1-score involves calculating the arithmetic mean of the F1-score for each class.

For our modeling, we have chosen to use the Ælæktra-architecture. The reason behind using this model is that it, across a large range of tasks, has proven itself to be a new gold-standard for Danish NLP-tasks. Furthermore, it requires fewer computational resources to train compared to similar model-architectures.

For the machine translation, we utilized xxxx.

We ran- and developed the code on [_Google Colaboratory_](https://colab.research.google.com/?utm_source=scs-index).

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 5:
```bash
cd {root directory (i.e. cds-language-exam-2021}
cd assignment_5
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

For model 1 (original dataset), we achieved a macro F1-score of xx after training for x epochs. For model 2 (expanded dataset), we achieved a macro F1-score of XX. The previously highest performing Danish model achieved a macro F1-score of 0.81 (as described in OffensEval2020). As such, we argue that we have built a new gold-standard model for hate speech detection in Danish. To help facilitate the implementation of the model in real-life scenarios, we have designed a .py-script and a Jupyter notebook with guides for how to run the model on new data. Furthermore, we have released our expanded dataset in this repository and, thus, created the largest publically available dataset of Danish hate speech.

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
