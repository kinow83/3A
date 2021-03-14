from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource
from app.dao.mysql.nas.nas_dao import NasDao

class NasApi(ApiResource):
    def init(self):
        self.dao_mapper = {
            "default": "app.dao.mysql.hr.nas_dao"
        }

    def get(self):
        return self.dao_response("get_nas")

    def post(self):
        return self.dao_response("set_nas")

    def delete(self):
        return self.dao_response("del_nas")

    def put(self):
        return self.dao_response("mod_nas")