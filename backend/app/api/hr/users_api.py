from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource, DaoResource

class UsersApi(ApiResource):
    def init(self):
        '''
        self.dao_mapper = {
            "get_users": "app.dao.mysql.hr.users_dao",
            "set_user": "app.dao.mysql.hr.users_dao",
            "del_user": "app.dao.mysql.hr.users_dao",
            "mod_user": "app.dao.mysql.hr.users_dao",
        }
        '''
        self.dao_mapper = {
            "default": "app.dao.mysql.hr.users_dao"
        }

    def get(self):
        return self.dao_response("get_users")

    def post(self):
        return self.dao_response("set_user")

    def delete(self):
        return self.dao_response("del_user")

    def put(self):
        return self.dao_response("mod_user")
