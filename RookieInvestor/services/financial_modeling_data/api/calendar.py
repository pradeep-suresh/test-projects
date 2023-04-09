import requests
from flask import Blueprint, jsonify, abort, current_app, request, abort
from flask_restful import Resource, Api, fields, inputs, reqparse

from financial_modeling_data import FinancialModelingPrepAPI


calendar_blueprint = Blueprint('calendar', __name__)
api = Api(calendar_blueprint)


class Calendar(Resource):
    URL = '{fmp_url}{calendar}?from={start_date}&to={end_date}&apikey={apikey}'
    accepted_args = ['stock_divdend_calendar', 'earning_calendar', 'economic_calendar']

    query_parser = reqparse.RequestParser()
    query_parser.add_argument('start', type=inputs.date, required=True)
    query_parser.add_argument('end', type=inputs.date, required=True)

    def __init__(self, **kwargs):
        self.fmp_url = kwargs['fmp_url']
        self.apikey = kwargs['apikey']

    def get(self, calendar_type):
        args = Calendar.query_parser.parse_args(strict=True)

        if calendar_type in Calendar.accepted_args:
            response = requests.get(
                Calendar.URL.format(
                    fmp_url = self.fmp_url, 
                    calendar=calendar_type,
                    start_date = args.start, 
                    end_date = args.end, 
                    apikey = self.apikey
                )
            )
        else:
            abort(404)

api.add_resource(Calendar, '/calendar/<string:calendar_type>', resource_class_kwargs=FinancialModelingPrepAPI.__dict__)
