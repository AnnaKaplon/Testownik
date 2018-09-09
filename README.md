
# README

### Introduction

Application made to support the learning process. It reads questions and answers from file, imitates school test and endly gives you number of good and wrong responses. 

### Questions file format

Data file has to have csv format. Columns with questions and good answers have to be named `question` and `good_answer`. Columns with other headers will be considered as wrong answers.

`Example.csv` contains examples data.

### Requirements

To ensure proper operation of the application following packages have to be installed:
* pandas
* PyQt5
* easygui
