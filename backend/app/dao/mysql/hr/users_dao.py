from app.core.dao import DAO
from app.core.exceptions import ApiException
from app.core.error import ERR

class UsersDao(DAO):
    def get_users(self):
        print(self.p)
        print(self.m)

        raise ApiException(ERR.ERROR_DAO, {"dao": "UsersDao", "api": "get_users"})

        return {"TEST": "OK"}