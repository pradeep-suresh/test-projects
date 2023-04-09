import requests
from flask import Blueprint, jsonify, abort, current_app, request, abort
from flask_restful import Resource, Api, fields, inputs, reqparse

from financial_modeling_data import FinancialModelingPrepAPI

index_performance_blueprint = Blueprint('index_performance', __name__)
api = Api(index_performance_blueprint)

class IndexPerformance(Resource):
    URL = '{fmp_url}quotes/index?apikey={apikey}'

    def __init__(self, **kwargs):
        self.fmp_url = kwargs['fmp_url']
        self.apikey = kwargs['apikey']

    def get(self):
        response = requests.get(IndexPerformance.URL.format(
            fmp_url = self.fmp_url,
            apikey = self.apikey
        ))

api.add_resource(IndexPerformance, '/quotes/index', resouce_class_kwargs = FinancialModelingPrepAPI.__dict__)