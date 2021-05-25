<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-language-exam-2021">
    <img src="../README_images/nlp2.png" alt="Logo" width="150" height="150">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Assignment 2</h3> 

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

### String processing with Python

Using a text corpus found on the cds-language GitHub repo __or__ a corpus of your own found on a site such as Kaggle, write a Python script which calculates __collocates__ for a specific keyword.

* The script should take a directory of text files, a keyword, and a window size (number of words) as input parameters, and an output file called out/{filename}.csv
* These parameters can be defined in the script itself
* Find out how often each word collocates with the target across the corpus
* Use this to calculate mutual information between the target word and all collocates across the corpus
* Save result as a single file consisting of three columns: collocate, raw_frequency, MI

* __BONUS CHALLENGE:__ Use argparse to take inputs from the command line as parameters

__General instructions__

* For this assignment, you should upload a standalone .py script which can be executed from the command line.
* Save your script as collocation.py
* Make sure to include a requirements.txt file and your data
* You can either upload the scripts here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow the structure of your script and to use them from the command line

__Purpose__

This assignment is designed to test that you have a understanding of:

* how to structure, document, and share a Python scripts;
* how to effectively make use of native Python packages for string processing;
* how to extract basic linguistic information from large quantities of text, specifically in relation to a specific target keyword

<!-- METHODS -->
## Methods

The problem in this assignment relates to manually calculating collocates for a specific keyword and window-size in a text corpus. For the task, I used the [_100 English Novels_](https://github.com/computationalstylistics/100_english_novels)-dataset containing a total of 100 .txt-files with novels from the 19th and 20th century. 

To solve the task i started by loading- and preprocessing the text to make it lowercase and remove all odd characters. This was done to ensure that, i.e., "fish." and "Fish!" would be recognized as identical words. I then proceeded to write a while-loop to create collocates for the specified window size and keyword. After this, I then progressed to do a series of for-loops with various steps of data-wrangling and mathematical calculations to compute collocate-metrics for all words within the specified window-size of the keyword. Using _pandas_, the script lastly writes a csv-file containing the collocate-word, the raw frequency (i.e. O11-score) and the Mutual Information (MI) score. This csv-file is written to a folder called "out" which is also created by the script. To solve the bonus assignment, I used argparse to enable the user to specify arguments from the terminal. With argparse, I made it possible for the user to specify their own filepath, keyword and window-size with the arguments --filepath, --keyword and --window_size, respectively.

For testing the keyword-argument, I recommend using less common keywords to reduce the runtime of the script. The default keyword is _"california"_.

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-language-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 2:
```bash
cd {root directory (i.e. cds-language-exam-2021)}
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
help = string, the keyword for which you wish to find collocates and calculate metrics. Needs to be lowercase. 
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

This repository contains the following folder:

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

I succeeded in creating a script that calculates various collocate-metrics for specific keywords and window-sizes and automatically saves selected metrics in a .csv-file. Furthermore, I solved the bonus assignment by making it possible to specify script-parameters from the terminal.


<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
