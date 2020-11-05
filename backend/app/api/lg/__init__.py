from flask import Flask, Blueprint, request
from flask_restful import Api

from . import (
    radauthlog_api)

lg_bp = Blueprint('lg', __name__)
lg_api = Api(lg_bp, prefix='/lg')

# GET
lg_api.add_resource(radauthlog_api.RadauthlogApi, '/radauthlog', endpoint='radauthlog')