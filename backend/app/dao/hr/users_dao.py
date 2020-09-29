from app.lib.mariadb import DB
from app.lib.resource import DaoResource

class UsersDao(DaoResource):
    def get_users(self):
        user_id = self.p.get("user_id")
        if user_id:
            sql = "SELECT * FROM users WHERE user_id = '{user_id}'".format(user_id=user_id)
            return DB.select(sql)
        else:
            sql ="SELECT * FROM users"
            return DB.select(sql)

    def set_user(self):
        ok, cause = self.required(["user_id", "user_name", "passwd"])
        if not ok:
            return False, cause

        user_id = self.p.get("user_id")
        user_name = self.p.get("user_name")
        passwd = self.p.get("passwd")
        sql = """
            INSERT INTO users (user_id, user_name, passwd, status) VALUES
            ('{user_id}', '{user_name}', '{passwd}', 0)
        """.format(user_id=user_id, user_name=user_name, passwd=passwd)
        return DB.insert(sql)

    def del_user(self):
        ok, cause = self.required(["user_id"])
        if not ok:
            return False, cause

        user_id = self.p.get("user_id")
        ok, cause = self.get_users()
        if not ok:
            return False, cause
        if not len(cause):
            return False, "unknown user_id: {user_id}".format(user_id=user_id)
        
        sql = "DELETE FROM users WHERE user_id = '{user_id}'".format(user_id=user_id)
        return DB.delete(sql)