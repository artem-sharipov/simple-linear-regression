# simple-linear-regression
This is my simple student task solution of finding linear regression coefficients using the least squares method based on data from a text file with a specific data representation.

## Problem statement

There is a file with coordinates of points in a two-dimensional coordinate system. You need to write a simple program that correctly calculates the values from the file, calculates the linear regression parameters for a set of points, and plots the points and linear regression on the plot. Additionally, a file is created for verification in Mathcad. The task is really very simple and shows the convenience of the language when processing data for reports and explanatory notes in the learning process.

## Solution

The solution to the problem is a file with the source code `solution/solution.py` and the result of its execution. The result of the code execution is shown in the image below. 

![Solution plot window](/img/solution_plot_window.png "Solution plot window")

The image shows a graphical window with the plot of data points and their linear regression. The points were obtained by parsing the source data file `data/data023.txt`, and the coefficients of the linear equation (linear regression) were calculated using the least squares method based on the data points.

The graphical window was created using the [pyplot](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot) graphical interface of the matplotlib [Matplotlib](https://matplotlib.org/) library.

## Usage

> [!IMPORTANT]
> I use Ubuntu (WSL),
> so the listed commands are relevant,
> to a greater extent, for such systems.


### Preparation

Before executing the solution file, you need to prepare the environment.
To run the code, you must have a Python 3 programming language interpreter installed in the system.
You can check for an interpreter and find out its version using the command:

```bash
python3 --version 
```

In my case, the result of executing the command is as follows:

```
$ python3 --version
Python 3.10.12
```
> [!NOTE]
> On your system, 
> the interpreter may be called `python` 
> instead of `python3`.

If the interpreter is already in your system, you can continue the preparatory operations, otherwise you need to install the interpreter in a way supported by your system.

In Python programming language projects, I recommend using a virtual environment (**venv**).

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

### Run

To run the code, use the following command:
```bash
python3 solution/solution.py
```

## TODO

I plan to improve the code and refactor it. Perhaps the presented solution will help someone solve their problem. I hope that I will design this repository well so that it reminds me of the happy times of my first year at university.