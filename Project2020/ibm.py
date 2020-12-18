#https://developer.ibm.com/technologies/artificial-intelligence/tutorials/deploy-a-python-machine-learning-model-as-a-web-service/
import pickle
import flask
import os

app = flask.Flask(__name__)

#port = int(os.getenv("PORT", 9099))

#Import the model file that was created previously:model = pickle.load(open("linearmodel.pkl","rb"))
model= pickle.load(open("lin_reg2.pkl","rb"))
#pickle.dump(lin_reg2, open("lin_reg2.pkl","wb"))
@app.route("/")
def hello():
    return "this is where the machine learning model gets API-ed!"

# Add index route.
@app.route("/")
def home():
  return app.send_static_file('index.html')


def uniform():
  return {"value": np.random.uniform()}

#Add a route that will allow you to send a JSON body of features and will return a prediction:
@app.route('/index', methods=['POST'])
def predict():

    features = flask.request.get_json(force=True)['features']
    prediction = model.predict([features])[0]
    response = {'prediction': prediction}

    return flask.jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
 #    app.run(host='0.0.0.0', port=port)