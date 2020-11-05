from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL

class UsersDao(DaoResource):
    def get_users(self):
        group_id = self.p.get("group_id")
        user_id = self.p.get("user_id")        
        where_sql = ""

        if group_id:            
            if user_id:
                where_sql += "AND A.user_id = '{}'".format(user_id)
            sql = """
                SELECT B.*, A.group_id FROM users_groups A, users B
                WHERE A.user_id = B.user_id AND A.group_id = '{group_id}' {where_sql}
            """.format(group_id=group_id, where_sql=where_sql)
        else:
            if user_id:
                where_sql += "AND user_id = '{}'".format(user_id)
            sql = "SELECT * FROM users WHERE 1=1 {where_sql}".format(where_sql=where_sql)                
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