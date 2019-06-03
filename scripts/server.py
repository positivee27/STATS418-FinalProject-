#!/usr/bin/env python3
from flask import Flask, jsonify, request
from prediction import predict

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def test():
        return 'The server is up!!!'

    @app.route('/mpg', methods=['POST'])
    def mpg():
        return jsonify(predict(request.json))
    return app


if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0')