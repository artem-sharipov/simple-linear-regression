# simple-linear-regression
This is my simple student task solution of finding linear regression coefficients using the least squares method based on data from a text file with a specific data representation.

## Problem statement

There is a file with coordinates of points in a two-dimensional coordinate system. You need to write a simple program that correctly calculates the values from the file, calculates the linear regression parameters for a set of points, and plots the points and linear regression on the plot. Additionally, a file is created for verification in Mathcad. The task is really very simple and shows the convenience of the language when processing data for reports and explanatory notes in the learning process.

## Usage
In Python programming language projects, I recommend using a virtual environment (**venv**). The following commands are shown for working in Linux (WSL).

Create a virtual environment:
```bash
python3 -m venv .venv 
```
Activate the virtual environment:
```bash
source .venv/bin/activate
```
After this action, the commands will be executed within the virtual environment.
This will be indicated by a mark `(.venv)` before the console prompt.

Next, you can start installing the necessary dependencies for the code to work. It's easy to do this by having a file `requirements.txt`.
This file contains all the requirements for the installed packages to run the code.
The file was created by me using the `pip freeze > requirements.txt`. You just need to run the following command:
```pip
pip install -r requirements.txt
```
This command will install all the packages listed in the file `requirements.txt`.
That's all. You can run the code.

To run the code, use the following command:
```bash
python3 solution/solution.py
```
The linear regression coefficients will appear in the console and a window with a dependency plot will open.

## TODO

I plan to improve the code and refactor it. Perhaps the presented solution will help someone solve their problem. I hope that I will design this repository well so that it reminds me of the happy times of my first year at university.