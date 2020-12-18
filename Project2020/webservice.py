#https://www.datacamp.com/community/tutorials/machine-learning-models-api-python
from flask import Flask

app = Flask(__name__)




# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
#Flask doesn't do anything until you call it!
#give your app a name, app is a nice generic one
#fl you've abbreviated it at import stage
#use functions through the module name
app = fl.Flask(__name__)

# Add root route.
#@ is a decorator calling the app defined above
@app.route("/")#route function tells flask what url triggers the function
def home():
  return app.send_static_file('index.html')

@app.route("/helloworld")
def hello():
    return "this is where the machine learning model gets API-ed!"

# Add uniform route.
#input coming from a network connection, through http
#identify the api
@app.route('/api/uniform')#route function tells flask what url triggers the function
def uniform():
  return {"value": np.random.uniform()}

# Add normal route.
#input coming from a network connection, through http
@app.route('/api/normal')#route function tells flask what url triggers the function
def normal():
  return {"value": np.random.normal()}

# Add linear route.
#input coming from a network connection, through http
#identify the api
@app.route('/api/linear')#route function tells flask what url triggers the function
def linearpredict():#the rest of the function needs to be finalised
  return {"value": np.random.exponential()}

# Add polynomial route.
#input coming from a network connection, through http
#identify the api
@app.route('/api/polynomial')#route function tells flask what url triggers the function
def polypredict():#the rest of the function needs to be finalised
  return {"value": np.random.multinomial()}


if __name__ == '__main__':
    app.run(debug=True)