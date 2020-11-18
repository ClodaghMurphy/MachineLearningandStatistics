# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
#Flask doesn't do anything until you call it!
#aha, the name variable, a type of keyword
#give your app a name, app is a nice generic one
#fl you've abbreviated it at import stage
#use functions through the module name
app = fl.Flask(__name__)

# Add root route.
#@ is a decorator calling the app defined above
@app.route("/")#route function tells flask what url triggers the function
def home():
  return app.send_static_file('index.html')

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
