from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource
from app.dao.hr.users_dao import UsersDao
from app.dao.hr.groups_dao import GroupsDao

class GroupsApi(ApiResource):
    def get(self):
        dao = GroupsDao(self.p)
        return self.response(dao.get_groups())

    def post(self):
        dao = GroupsDao(self.p)
        return self.response(dao.set_group())

    def delete(self):
        dao = GroupsDao(self.p)
        return self.response(dao.del_group())

    def put(self):
        dao = GroupsDao(self.p)
        return self.response(dao.mod_group())

class GroupsTreeApi(ApiResource):
    def get(self):
        dao = GroupsDao(self.p)
        return self.response(dao.get_groups_tree())