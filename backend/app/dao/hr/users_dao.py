from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL

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
        ok, res = self.required(["user_id", "username", "passwd"])
        if not ok:
            return self.fail_required(res)

        user_id = self.p.get("user_id")
        username = self.p.get("username")
        passwd = self.p.get("passwd")
        sql = """
            INSERT INTO users (user_id, username, passwd, status) VALUES
            ('{user_id}', '{username}', '{passwd}', 0)
        """.format(user_id=user_id, username=username, passwd=passwd)
        return DB.insert(sql)

    def del_user(self):
        ok, res = self.required(["user_id"])
        if not ok:
            return self.fail_required(res)

        user_id = self.p.get("user_id")
        ok, res = self.get_users()
        if not ok:
            return FAIL(res)
        if not len(res):
            return self.fail_unknown("user_id", user_id)
        
        sql = "DELETE FROM users WHERE user_id = '{user_id}'".format(user_id=user_id)
        return DB.delete(sql)

    def mod_user(self):
        ok, res = self.required(["user_id", "username", "passwd"])
        if not ok:
            return self.fail_required(res)

        user_id = self.p.get("user_id")
        ok, res = self.get_users()
        if not ok:
            return FAIL(res)
        if not len(res):
            return self.fail_unknown("user_id", user_id)

        user_id = self.p.get("user_id")
        username = self.p.get("username")
        passwd = self.p.get("passwd")
        sql = """
            UPDATE users SET username='{username}', passwd='{passwd}'
            WHERE user_id='{user_id}'
        """.format(user_id=user_id, username=username, passwd=passwd)
        return DB.update(sql)