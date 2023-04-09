import requests
from flask import Blueprint, jsonify, abort, current_app, request, abort
from flask_restful import Resource, Api, fields, inputs, reqparse

from financial_modeling_data import FinancialModelingPrepAPI

index_performance_blueprint = Blueprint('index_performance', __name__)
api = Api(index_performance_blueprint)

class HistoricalPerformance(Resource):
    # Date format yyyy-mm-dd
    URL = '{fmp_url}historical-price-full/{ticker_symbol}?from={start_date}&to={end_date}&apikey={apikey}'

    query_parser = reqparse.RequestParser()
    query_parser.add_argument('start', type=inputs.date, required=True)
    query_parser.add_argument('end', type=inputs.date, required=True)

    def __init__(self, **kwargs):
        self.fmp_url = kwargs['fmp_url']
        self.apikey = kwargs['apikey']

    def get(self, ticker_symbol):
        args = Calendar.query_parser.parse_args(strict=True)

        response = requests.get(HistoricalPerformance.URL.format(
            fmp_url = self.fmp_url,
            ticker_symbol = ticker_symbol,
            start_date = args.start, 
            end_date = args.end,
            apikey = self.apikey
        ))

api.add_resource(HistoricalPerformance, '/historical-quotes/<string:ticker_symbol>', resouce_class_kwargs = FinancialModelingPrepAPI.__dict__)
    