from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource, DaoResource

class GroupsApi(ApiResource):
    def init(self):
        '''
        self.dao_mapper = {
            "get_groups": "app.dao.mysql.hr.groups_dao",
            "set_group": "app.dao.mysql.hr.groups_dao",
            "del_group": "app.dao.mysql.hr.groups_dao",
            "mod_group": "app.dao.mysql.hr.groups_dao",
        }
        '''
        self.dao_mapper = {
            "default": "app.dao.mysql.hr.groups_dao"
        }

    def get(self):
        return self.dao_response("get_groups")

    def post(self):
        return self.dao_response("set_group")

    def delete(self):
        return self.dao_response("del_group")

    def put(self):
        return self.dao_response("mod_group")

class GroupsTreeApi(ApiResource):
    def init(self):
        self.dao_mapper = {
            "default": "app.dao.mysql.hr.groups_dao"
        }

    def get(self):
        return self.dao_response("get_groups_tree")