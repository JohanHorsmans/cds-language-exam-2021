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

### Creating reusable network analysis pipeline

This exercise is building directly on the work we did in class. I want you to take the code we developed together and in you groups and turn it into a reusable command-line tool. You can see the code from class here:

https://github.com/CDS-AU-DK/cds-language/blob/main/notebooks/session6.ipynb

This command-line tool will take a given dataset and perform simple network analysis. In particular, it will build networks based on entities appearing together in the same documents, like we did in class.

* Your script should be able to be run from the command line
* It should take any weighted edgelist as an input, providing that edgelist is saved as a CSV with the column headers "nodeA", "nodeB"
* For any given weighted edgelist given as an input, your script should be used to create a network visualization, which will be saved in a folder called viz.
* It should also create a data frame showing the degree, betweenness, and eigenvector centrality for each node. It should save this as a CSV in a folder called output.

__Tips__
* You should use argparse() in the Python standard library
* Your code should contain a main() function
* Don't worry too much about efficiency - networkx is really slow, there's no way around i!
* If you have issues with pygraphviz, just use the built-in matplotlib functions in networkx.
* You may want to create an argument for the user to define a cut-off point to filter data. E.g. only include node pairs with more than a certain edge weight.
* Make sure to use all of the Python scripting skills you've learned so far, including in the workshops with Kristoffer Nielbo

__Bonus challenges__
* Attempt to implement coreference resolution on entities (time-consuming)
* Bundle your code up into a Python class, focusing on code modularity
* Let the user define which graphing algorithm they use (pretty tricky)
* Are there other ways of creating networks, rather than just document co-occurrence? (really tricky)

__General instructions__
* For this assignment, you should upload a standalone .py script which can be executed from the command line
* Save your script as network.py
* You must include a requirements.txt file and a bash script to set up a virtual environment for the project. You can use those on worker02 as a template
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line

__Purpose__
This assignment is designed to test that you have an understanding of:

* how to create command-line tools with Python;
* how to perform network analysis using networkx;
* how to create resuable and reproducible pipelines for data analysis.

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
