<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-language-exam-2021">
    <img src="../README_images/nlp2.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Assignment 4</h3> 

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

### Applying (un)supervised machine learning to text data

The assignment this week involves a little bit of a change of pace and a slightly different format. As we have the Easter break next week, you also have a longer period assigned to complete the work.

For this task, you will pick your own dataset to study.

This dataset might be something to do with COVID-19 discourse on Reddit; IMDB reviews; newspaper headlines; whatever it is that catches your eye. However, I strongly recommend using a text dataset from somewhere like Kaggle - https://www.kaggle.com/datasets

When you've chosen the data, do one of the following tasks. One of them is a supervised learning task; the other is unsupervised. 

__NOTE: I HAVE CHOSEN THE FOLLOWING TASK:__

* Train a text classifier on your data to predict some label found in the metadata. For example, maybe you want to use this data to see if you can predict sentiment label based on text content.

You should formulate a short research statement explaining why you have chosen this dataset and what you hope to investigate. This only needs to be a paragraph or two long and should be included as a README file along with the code. E.g.: I chose this dataset because I am interested in... I wanted to see if it was possible to predict X for this corpus.

In this case, your peer reviewer will not just be looking to the quality of your code. Instead, they'll also consider the whole project including choice of data, methods, and output. Think about how you want your output to look. Should there be visualizations? CSVs?

You should also include a couple of paragraphs in the README on the results, so that a reader can make sense of it all. E.g.: I wanted to study if it was possible to predict X. The most successful model I trained had a weighted accuracy of 0.6, implying that it is not possible to predict X from the text content alone. And so on.

__Tips__
* Think carefully about the kind of preprocessing steps your text data may require - and document these decisions!
* Your choice of data will (or should) dictate the task you choose - that is to say, some data are clearly more suited to supervised than unsupervised learning and vice versa. Make sure you use an appropriate method for the data and for the question you want to answer
* Your peer reviewer needs to see how you came to your results - they don't strictly speaking need lots of fancy command line arguments set up using argparse(). You should still try to have well-structured code, of course, but you can focus less on having a fully-featured command line tool

__General instructions__
* You should upload standalone .py script(s) which can be executed from the command line
* You must include a requirements.txt file and a bash script to set up a virtual environment for the project You can use those on worker02 as a template
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line

__Purpose__
This assignment is designed to test that you have an understanding of:

* how to formulate research projects with computational elements;
* how to perform (un)supervised machine learning on text data;
* how to present results in an accessible manner.

<!-- METHODS -->
## Methods

The problem of this assignment relates to mangling and processing date-time-data and calculating rolling sentiment scores for a large text corpus. I use pandas to convert the data to date-time format and arrange them in chronological order. To reduce run-time, I carry out the analysis on a subset of 100.000 randomly sampled headlnes. I use SpaCy text blob to calculate the sentiment-score for the headlines. I batch the data together with a batch-size of 500 to make the analysis run faster. I then calculate mean sentiment score for each week and month and plot the scores in two separate graphs (see _discussion of results_). Lastly, the script also writes a csv-file named _"sentiment.csv"_ with the score for each individual headline.

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 3:
```bash
cd {root directory (i.e. cds-language-exam-2021}
cd assignment_3
python3 sentiment.py
```
<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following folders:

|Folder|Description|
|:--------|:-----------|
```data/``` | Folder containing a dataset consisting over a million headlines taken from the Australian news source ABC (Start Date: **2003-02-19** ; End Date: **2020-12-31**)

Furthermore, it holds the following files:
|File|Description|
|:--------|:-----------|
```sentiment.py``` | The python script for the assignment
```README.md``` | The README file that you are currently reading.

<!-- DISCUSSION OF RESULTS -->
## Discussion of results

Two plots are produced by the script. One for the weekly rolling sentiment score (figure 1) and one for the monthly rolling sentiment score (figure 2). The two plots show that the news data is generally positive (Sentiment score > 0) in spite of the fluctuations on a weekly/monthly basis. We see that the variance in sentiment scores is larger on a weekly basis than on a monthly basis, indicating that the variance seen from week to week is quite similar in both directions and thus, to a certain extent, cancels each other out when analysed on a monthly basis.


<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/plot2.png" alt="Weekly">
  </a>
  
<p align="center">
Figure 1: Weekly sentiment score
  
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/plot1.png" alt="Monthly">
  </a>

<p align="center">
Figure 2: Monthly sentiment score


<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
