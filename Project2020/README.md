# MachineLearningandStatistics
GMIT - Machine Learning and Statistics module 2020. <br>


This repository contains a project submitted as part of the Machine Learning and Statistics module 2020.<br>
Course Higher Diploma in Data Analytics, GMIT, Ireland<br>
The Lecturer is Dr. Ian McLoughlin<br>
Author: Clodagh Murphy<br>
Email: G00376300@gmit.ie<br>
Dates: October- December 2020<br>

## Z. Description of the Project
Create a web service that uses machine learning to make predictions based on the data set: powerproduction. 

Produce a model that accurately predicts wind turbine power output from wind speed values in the data set. 
Develop a web service that will respond with predicted power values based on speed values sent as HTTP requests.
Web service is a form of API that assumes an API is hosted over a server and can be consumed.
Django, Falcon, Flask and Hug are some of the web service development frameworks in Python.


## X. Contents of this repository
The repository contains:
* This `README.md` 
* `roughwork.ipynb` shows some of the detail behind the project
* `train-model.ipynb` trains a model using the powerproduction data set. In the notebook the model is explained and its accuracy analysed.<br>
Note: Code that prints long lists of numbers on the screen has been commented out to keep the pages compact.
These can be uncommented as required.


* `powerproduction.csv` was the original dataset provided
* `cleanpower.csv` is the updated version 
* `requirements.txt` - what is needed is set out clearly in this separate file. 
It used for specifying what python packages (and versions) are required to run this project. 
To install your packages using requirements.txt:

    - Open a terminal or command prompt<br>
    - Navigate to the folder with requirements.txt<br>
    - run: pip install -r requirements.txt<br>
    - Installation of dependencies is complete.<br>
*




## Z. Instructions for downloading this repository
Log on to GitHub and search for user ClodaghMurphy, the repository is entitled MachineLearningandStatistics.<br>
On github.com choose the green `Code` button to clone or download the code onto your machine.<br>
```
git clone https://github.com/ClodaghMurphy/MachineLearningandStatistics
```
For further information on how github works video guides are available here https://www.youtube.com/githubguides<br>

## Z. How to run the jupyter notebook containing this project 
Jupyter Notebooks are a spin-off project from the IPython project. The name, Jupyter, comes from the programming languages that it supports: Julia, Python, and R.<br>
It is an open source web application used to create and share documents that contain live code, equations, visualizations and text.<br>
The Jupyter Notebook is a useful tool to learn Python language and also enables sharing of data and images in a very accessible way.<br>

##### Install with conda
If you use conda, you can install it with:
`conda install -c conda-forge jupyterlab`
##### Install with pip
If you use pip, you can install it with:
`pip install jupyter`
If installing using pip install --user, you must add the user-level bin directory to your PATH environment variable in order to launch jupyter lab. If you are using a Unix derivative (FreeBSD, GNU / Linux, OS X), you can achieve this by using export PATH="$HOME/.local/bin:$PATH" command.

##### Run JupyterLab
Once installed, launch Jupyter Notebook on your terminal with:
`jupyter notebook`


Jupyter will initialise in the background and your default browser will pop up in a new tab connecting to webserver.<br> http://localhost:8888/tree<br>
The terminal will simultaneously display instructions on how to stop the connection to that webserver in addition to URL details that <br>contain a unique token.<br>

http://localhost:8888/?token=XXXXXYYYYY123456789<br>
Chrome and firefox are the optimal web browsers to use and you may need to copy the url into one of these instead of using the default<br> pop-up.<br>
You are running the Jupyter server and can use it to open and engage with my repository contents.<br>



## How to run the web service

Follow instructions!<br>
Input the relevant line on your cmd linux/Windows/bash<br>
A "hard kill" is required to close the application (Ctrl C)<br>
`bash Linux
export FLASK_APP=webservice.py
python3 -m flask run`


`bash Windows
set FLASK_APP=webservice.py
python -m flask run`


`docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image`

`$ export FLASK_APP=webservice.py<br>
$ flask run<br>
 * Running on http://127.0.0.1:5000/`


