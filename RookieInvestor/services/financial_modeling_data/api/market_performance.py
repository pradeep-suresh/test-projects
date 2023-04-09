import requests
from flask import Blueprint, jsonify, abort, current_app, request, abort
from flask_restful import Resource, Api, fields, inputs, reqparse

from financial_modeling_data import FinancialModelingPrepAPI


market_performance_blueprint = Blueprint('market_performance', __name__)
api = Api(market_performance_blueprint)

class SectorPerformance(Resource):
    URL = '{fmp_url}sector-performance?apikey={apikey}'

    def __init__(self, **kwargs):
        self.fmp_url = kwargs['fmp_url']
        self.apikey = kwargs['apikey']

    def get(self):
        response = requests.get(SectorPerformance.URL.format(
            fmp_url = self.fmp_url,
            apikey = self.apikey
        ))

class StockPerformance(Resource):
    URL = '{fmp_url}{performance_type}?apikey={apikey}'
    accepted_args = ['gainers', 'losers', 'actives']

    def __init__(self, **kwargs):
        self.fmp_url = kwargs['fmp_url']
        self.apikey = kwargs['apikey']

    def get(self, performance_type):
        if performance_type in StockPerformance.accepted_args:
            requests.get(StockPerformance.URL.format(
                fmp_url = self.fmp_url,
                performance_type = performance_type,
                apikey = self.apikey
            ))
        else:
            abort(404)


api.add_resource(SectorPerformance, '/sector-performance', resource_class_kwargs=FinancialModelingPrepAPI.__dict__)
api.add_resource(StockPerformance, '/stock-performance/<string:performance_type>', resource_class_kwargs=FinancialModelingPrepAPI.__dict__)