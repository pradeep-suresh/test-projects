# src/__init__.py

import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

import os

# instantiate the app
app = Flask(__name__)

api = Api(app)

# Instantiate the db
db = SQLAlchemy(app)


# model
class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')