from flask import Flask, Blueprint, request
from flask_restful import Api

from . import (
    error_api)

sample_bp = Blueprint('sample', __name__)
sample_api = Api(sample_bp, prefix='/sample')

# GET/POST/DELETE/PUT
sample_api.add_resource(error_api.APIError, '/api/error', endpoint='api_error')
sample_api.add_resource(error_api.DAOError, '/dao/error', endpoint='dao_error')