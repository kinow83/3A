from flask import Flask, Blueprint, request
from flask_restful import Api

from . import (
    users_api, 
    groups_api)

hr_bp = Blueprint('hr', __name__)
hr_api = Api(hr_bp, prefix='/hr')

# GET/POST/DELETE/PUT
hr_api.add_resource(users_api.UsersApi, '/users', endpoint='users')
# GET/POST/DELETE/PUT
hr_api.add_resource(groups_api.GroupsApi, '/groups', endpoint='groups')