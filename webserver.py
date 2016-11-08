# -*- coding: utf-8 -*-

from flask import Flask, jsonify

from recommendation.Predict.predict_rating import predict_rating

app = Flask(__name__)

@app.route('/predict_rating/<user_id>')
def get_predict_rating_api(user_id):
    pr = predict_rating()

    print('------------------webserver start--------------------')
    data = pr.get_predict_rating_web(user_id)

    print('------------------data searching end--------------------')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)
    #app.run(debug=True, host='localhost', port=8080)