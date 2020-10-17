#!/usr/bin/env python
# coding: utf-8

from flask import Flask
from flask import request
import pickle
# For testing the model
import numpy as np
import logging
import json



logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)

# The name of the pickle file
file_name_model = "model.pkl"

#open the binary of the tree decision model with pickle
model = pickle.load(open(file_name_model, 'rb'))


def response(status, message):
    return {
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': "*"},
        "statusCode": status,
        "body": json.dumps({"response": message})
    }


@app.route("/")
def home():
    return response(200, "welcome")


@app.route("/test/prediction")
def test():
    array = np.array([4.9, 3. , 1.4, 0.2]).reshape(1,-1)
    logger.info('array for testing' + str(array))
    data = {'x': array.tolist()}
    data['predicted'] = model.predict(array).tolist()
    print(" Data in test is : ", str(data))
    return response(200, data)


@app.route("/predict", methods = ["POST", "GET"])
def predict():
    data = {
        'x': request.args.get("x")
    }
    try:
        array = np.array(json.loads(data['x']))
        logger.info(" Printing x value " + str(array))
        data['x'] = array.tolist()
        data['predicted'] = model.predict(array.reshape(1, -1)).tolist()
    except:
        return response(400, "Bad Request")
    
    return response(200, data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000)
