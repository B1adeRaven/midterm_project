import pickle

from flask import Flask
from flask import request
from flask import jsonify


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv, model = load('model_C=20.bin')

app = Flask('Bankrupt business')


@app.route('/predict', methods=['POST'])
def predict():
    business = request.get_json()

    X = dv.transform([business])
    y_pred = model.predict_proba(X)[0, 1]
    bankrupt_business = y_pred >= 0.5

    result = {
        'bankrupt_business_probability': float(y_pred),
        'bankrupt_business': bool(bankrupt_business)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
