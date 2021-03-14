from app.core.dao import DAO
from app.core.exceptions import ApiException
from app.core.error import ERR

class Error(DAO):
    def get_error(self):
        print(self.p)
        print(self.m)
        raise ApiException(ERR.ERROR_DAO, {"dao": "mysql", "api": "sample"})
        return {"TEST": "OK"}