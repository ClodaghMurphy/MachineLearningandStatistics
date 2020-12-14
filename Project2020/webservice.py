#https://www.datacamp.com/community/tutorials/machine-learning-models-api-python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "this is where the machine learning model gets API-ed!"


if __name__ == '__main__':
    app.run(debug=True)