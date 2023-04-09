import os

from flask import Flask, jsonify
from flask_restx import Resource, Api

class FinancialModelingPrepAPI():
    fmp_url = 'https://financialmodelingprep.com/api/v3/'
    apikey = 'd01f4b2799dc3426b96834df2db48094'

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # register blueprints
    from financial_modeling_data.api.ping import ping_blueprint
    from financial_modeling_data.api.calendar import calendar_blueprint
    from financial_modeling_data.api.market_performance import market_performance_blueprint
    from financial_modeling_data.api.index_performance import index_performance_blueprint

    app.register_blueprint(ping_blueprint)
    app.register_blueprint(calendar_blueprint)
    app.register_blueprint(market_performance_blueprint)
    app.register_blueprint(index_performance_blueprint)


    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app
