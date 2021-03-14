from flask import request, abort
from flask_restful import Resource
from app.core.api import API
from app.core.dao import DAO


class UsersApi(API):
    def init_dao(self):
        self.dao_mapper = {
            "default": "app.dao.mysql.hr.users_dao"
        }

    def get(self):
        return self.call("get_users")

    def post(self):
        return self.call("set_user")

    def delete(self):
        return self.call("del_user")

    def put(self):
        return self.call("mod_user")
