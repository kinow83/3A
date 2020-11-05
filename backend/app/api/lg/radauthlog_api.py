from flask import request, abort
from flask_restful import Resource
from app.lib.resource import ApiResource
from app.dao.hr.users_dao import UsersDao
from app.dao.hr.groups_dao import GroupsDao
from app.dao.lg.radlog_dao import RadlogDao

class RadauthlogApi(ApiResource):
    def get(self):
        dao = RadlogDao(self.p)
        return self.response(dao.get_radauthlog())
