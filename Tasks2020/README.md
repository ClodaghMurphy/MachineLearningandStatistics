# MachineLearningandStatistics
GMIT - Machine Learning and Statistics module 2020. <br>


This repository contains an assessment submitted as GMIT Programming for Tasks 2020 Assessment, last commit December 18, 2020.<br>
Course Higher Diploma in Data Analytics, GMIT, Ireland<br>
Lecturer: Dr. Ian McLoughlin<br>
Author: Clodagh Murphy<br>
Email: g00376300@gmit.ie<br>
Dates: October- December 2020<br>


## 1. Contents of this repository
The repository contains:
* This `README.md` file
*`all_tasks` jupyter notebook with four tasks set out in this order
1. `sqrt2` - a python function to print the $ \sqrt{2} $ to 100 decimal places
2. `Chi-Squared Test` - verifying the result that appears on wikipedia using `scipy.stats`
3. `stdev.s` - demonstrate using `numpy` that excel's STDEV.S function is a better estimate for the standard deviation of a population than STDEV.P.
4. `k-means`-use of `scikit-learn` to apply k-means clustering to Fisher’s famous Iris data set
Note: Code that prints long lists of numbers on the screen has been commented out to keep the pages compact.
These can be uncommented as required.


## 2. Instructions for downloading this github repository
Log on to GitHub and search for user ClodaghMurphy, the repository is entitled MachineLearningandStatistics.<br>
On github.com choose the green `Code` button to clone or download the code onto your machine.<br>
```
git clone https://github.com/ClodaghMurphy/MachineLearningandStatistics
```
For further information on how github works, video guides are available at https://www.youtube.com/githubguides<br>

## 3. How to run the jupyter notebook containing this project 
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


