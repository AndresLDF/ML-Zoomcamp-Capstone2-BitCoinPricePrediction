import pickle
import pandas as pd

from flask import Flask
from flask import request
from flask import jsonify


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

model_1d = load('Trained_Models/model_selected_1d.bin')
model_7d = load('Trained_Models/model_selected_7d.bin')


app = Flask('capstone')

@app.route('/predict', methods=['POST'])
def predict():
    PreparedInput = request.get_json()
    
    df = pd.DataFrame([PreparedInput])
    y_pred_1d = model_1d.predict(df)
    y_pred_7d = model_7d.predict(df)
    
    y_pred_1d_list = y_pred_1d.tolist()
    y_pred_7d_list = y_pred_7d.tolist()

    result = {
        'One day prediction': y_pred_1d_list[0],
        'Seven days prediction':  y_pred_7d_list[0],
    } 

    return jsonify(result)