#adapted from https://www.datacamp.com/community/tutorials/machine-learning-models-api-python

# Dependencies
# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

from flask import request, jsonify
import joblib
import traceback
import pandas as pd


app = fl.Flask(__name__)


###############################

#################################

# Add root route.
#@ is a decorator calling the app defined above
#@app.route("/")#route function tells flask what url triggers the function
#def home():
 # return app.send_static_file('index.html')

@app.route('/hello')
def hello():
  return "this is where the Machine Learning model gets API-ed"

# Add uniform route.
#input coming from a network connection, through http
#identify the api
@app.route('/api/uniform')#route function tells flask what url triggers the function
def uniform(): 
  return {"value": np.random.uniform()}

@app.route('/api/dataset')
def dataset(): 
 return app.send_static_file('cleanpower.csv')

@app.route('/predictlinear')
def predictlinear():
  import datetime
  return (datetime.datetime.now().strftime("%A, %B %d %Y at %I:%M %p"))
  #lr = joblib.load("model.pkl") #import the previously pickled model
  #this is the code that produced a result in my notebook (lin_reg.predict( ([ [8.5] ]) )))
  #return {"this is where the linear prediction page will go": (lr.predict( ([ [8.5] ]) ))}

 
@app.route('/predictpoly')
def predictpoly():
 poly = joblib.load("model2.pkl")#import the previously pickled model
 #There is something wrong here, i'm getting a server error 500
 #the resource failed to load
 return {"this is where the polynomial prediction page will go": (poly.predict([[8.5]]) )}

  

#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    lr = joblib.load("model1.pkl") # Load "model.pkl"
    poly = joblib.load("model2.pkl")
    print ('Model loaded')

   

    app.run(port=port, debug=True)