#SEE ALSO https://www.datacamp.com/community/tutorials/machine-learning-models-api-python


# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
#Flask doesn't do anything until you call it
#give your app a name, app is a nice generic one
#fl you've abbreviated it at import stage
#use functions through the module name
app = fl.Flask(__name__)


###############################
#pickling piece#
#################################

# Add root route.
#@ is a decorator calling the app defined above
#@app.route("/")#route function tells flask what url triggers the function
#def home():
 # return app.send_static_file('index.html')

@app.route('/hello')
def hello():
  return "this is where the Machine Learning model gets API-ed!"

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
  return {"predictlinear": (1+5)}


@app.route('/predictpoly')
def predictpoly():
  return {"this is where the polynomial prediction page will go!": (5*2)}

  

if __name__ == '__main__':
    app.run(debug=True)

