import pickle
from flask import Flask, request, app, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

reg_predict = pickle.load(open('reg_predict.pickle', 'rb'))
scalar = pickle.load(open('scalar.pickle','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.json['data']
    data_transformed = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = reg_predict.predict(data_transformed)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = [float(x) for x in request.form.values()]
    data_transformed = scalar.transform(np.array(data).reshape(1, -1))
    output = reg_predict.predict(data_transformed)[0] 
    return render_template("home.html", prediction_text = "Your dream house will cost {}".format(round(output)) + " lakhs")

if __name__ == "__main__":
    app.run(debug=True)
