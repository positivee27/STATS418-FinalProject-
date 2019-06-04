#!/usr/bin/env python3
from flask import Flask, jsonify, request
from prediction import predict

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def test():
        return 'The server is up - good job!!!'

    @app.route('/votes', methods=['POST'])
    def getvotes():

        to_predict = request.json

        print(to_predict)
        pred = predict(to_predict)
        return jsonify({"predicted votes": pred.tolist()})
    return app


if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0')