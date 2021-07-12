import os
import sys
from flask import Flask, jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class HelloScribetech(Resource):
    def get(self):
        response = {
                "Message": "HELLO SCRIBETECH",
                }

        return jsonify(response)


api.add_resource(HelloScribetech, '/gethello')


if __name__ == "__main__":

    PORT = os.environ.get('PORT')
    HOST = os.environ.get('HOST')
    app.run(host=HOST, port=PORT, debug=True)
