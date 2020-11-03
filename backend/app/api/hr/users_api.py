from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource
from app.dao.hr.users_dao import UsersDao
from app.dao.hr.groups_dao import GroupsDao

class UsersApi(ApiResource):
    def get(self):
        dao = UsersDao(self.p)
        return self.response(dao.get_users())

    def post(self):
        dao = UsersDao(self.p)
        return self.response(dao.set_user())

    def delete(self):
        dao = UsersDao(self.p)
        return self.response(dao.del_user())

    def put(self):
        dao = UsersDao(self.p)
        return self.response(dao.mod_user())
