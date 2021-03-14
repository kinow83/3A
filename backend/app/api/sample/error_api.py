from flask import request, abort
from flask_restful import Resource
from app.core.api import API
from app.core.dao import DAO
from app.core.exceptions import ApiException, api_error_check
from app.core.error import ERR



class APIError(API):
    def init_dao(self):
        pass

    def get(self):        
        raise ApiException(*ERR.ERROR_SAMPLE, {"msg": "This is APIError test"})
        return self.dao_call("")

class DAOError(API):
    def init_dao(self):
        self.dao_mapper = {
            "default": "app.dao.mysql.sample.error"
        }

    def get(self):
        return self.dao_call("get_error")