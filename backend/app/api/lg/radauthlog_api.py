from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource
from app.lib.resource import ApiResource, DaoResource

class RadauthlogApi(ApiResource):
    def init(self):
        self.dao_mapper = {
            "default": "app.dao.mysql.lg.radlog_dao"
        }

    def get(self):
        return self.dao_response("get_radauthlog")
