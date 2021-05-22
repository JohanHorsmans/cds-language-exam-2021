<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-language-exam-2021">
    <img src="../README_images/nlp2.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Assignment 3</h3> 

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

### Dictionary-based sentiment analysis with Python

This is a dataset of over a million headlines taken from the Australian news source ABC (Start Date: **2003-02-19** ; End Date: **2020-12-31**).

* Calculate the sentiment score for every headline in the data. You can do this using the spaCyTextBlob approach that we covered in class or any other dictionary-based approach in Python.
* Create and save a plot of sentiment over time with a 1-week rolling average
* Create and save a plot of sentiment over time with a 1-month rolling average
* Make sure that you have clear values on the x-axis and that you include the following: a plot title; labels for the x and y axes; and a legend for the plot
* Write a short summary (no more than a paragraph) describing what the two plots show. You should mention the following points: 1) What (if any) are the general trends? 2) What (if any) inferences might you draw from them?

* __HINT:__ You'll probably want to calculate an average score for each day first, before calculating the rolling averages for weeks and months.

__General instructions__

* For this assignment, you should upload a standalone .py script which can be executed from the command line or a Jupyter Notebook
* Save your script as sentiment.py or sentiment.ipynb
* Make sure to include a requirements.txt file and details about where to find the data
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line

__Purpose__
This assignment is designed to test that you have a understanding of:

* how to perform dictionary-based sentiment analysis in Python;
* how to effectively use pandas and spaCy in a simple NLP workflow;
* how to present results visually, working with datetime formats to show trends over time

<!-- METHODS -->
## Methods

The problem in this assignment relates to manually calculating collocates for a specific keyword and window-size in a text corpus. To solve the task i started by loading- and preprocessing the text to make it lowercase and remove all odd characters. This was done to ensure that, i.e., "fish." and "Fish!" are recognized as identical words. I then proceeded to do a series of for-loops with various steps of data-wrangling and mathematical calculatons to compute collocate-metrics for all words within the specified window-size of the keyword. Using _pandas_, the script lastly writes a csv-file containing the collocate-word, the raw frequency (i.e. O11-score) and the Mutual Information (MI) score. This csv-file is written to a folder called "out" which is also created by the script. To solve the bonus assignment, I used argparse to enable the user to specify arguments from the terminal. With argparse, I made it possible for the user to specify their own filepath, keyword and window-size with the arguments --filepath, --keyword and --window_size, respectively.

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 2:
```bash
cd {root directory (i.e. cds-language-exam-2021}
cd assignment_2
python3 collocation.py
```
__You can specify the following optional argument from the terminal:__

_Custom filepath:_
```bash
"-f", "--filepath"
default = "data"
type = str
help = string, path to text-corpus. Texts need to be .txt-files. Be wary of difference in operating systems in terms of spcifying path with "/" or "\".
```

_Keyword:_
```bash
"-k", "--keyword"
default = "california"
type = str
help = string, the keyword for which you wish to find collocates and calculate metrics.
```

_Window size:_
```bash
"-w", "--window_size"
default = 2
type = int
help = integer, collocate window-size.
```
You can also type: ```python3 collocation.py -h``` for a detailed guide on how to specify script-arguments. 

<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following folders:

|Folder|Description|
|:--------|:-----------|
```data/``` | Folder containing a dataset consisting of 100 classic English novels in .txt-format.

Furthermore, it holds the following files:
|File|Description|
|:--------|:-----------|
```collocation.py``` | The python script for the assignment
```README.md``` | The README file that you are currently reading.

<!-- DISCUSSION OF RESULTS -->
## Discussion of results

The two plots show that the news data is generally positive (Sentiment score > 0) in spite of the fluctuations on a weekly/monthly basis. We see that the variance in sentiment scores is larger on a weekly basis than on a monthly basis, indicating that the variance seen from week to week is quite similar in both directions and thus, to a certain extent, cancels each other out when analysed on a monthly basis.

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
