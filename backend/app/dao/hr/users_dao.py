from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL
from app.dao.hr.groups_dao import GroupsDao

class UsersDao(DaoResource):
    def get_users(self):
        group_id = self.p.get("group_id")
        user_id = self.p.get("user_id")        
        where_sql = ""

        if group_id:            
            if user_id:
                where_sql += "AND A.user_id = '{}'".format(user_id)
            sql = """
                SELECT B.*, C.group_id, C.group_name 
                FROM users A, users_groups B, groups C
                WHERE 
                    A.user_id = B.user_id AND 
                    B.group_id = C.group_id AND 
                    B.group_id = '{group_id}' 
                    {where_sql}
            """.format(group_id=group_id, where_sql=where_sql)
        else:
            if user_id:
                where_sql += "AND user_id = '{}'".format(user_id)
            sql = """
                SELECT A.*, C.group_id, C.group_name FROM users A
                LEFT JOIN users_groups B ON A.user_id = B.user_id
                LEFT JOIN groups C ON B.group_id = C.group_id
                WHERE 1=1 {where_sql}
            """.format(where_sql=where_sql)                
        return DB.select(sql)

    def set_user(self):
        ok, res = self.required(["user_id", "username", "passwd", "group_id", "group_name"])
        if not ok:
            return self.fail_required(res)
        ok, res = GroupsDao({"group_id": self.p.get("group_id")}).get_groups()
        if not ok:
            return self.fail_message(res)
        if len(res) == 0:
            return self.fail_message("can't find group {}".format(self.p.get("group_name")))

        user_id = self.p.get("user_id")
        username = self.p.get("username")
        passwd = self.p.get("passwd")
        group_id = self.p.get("group_id")
        sql = """
            INSERT INTO users (user_id, username, passwd, status) VALUES
            ('{user_id}', '{username}', '{passwd}', 0)
        """.format(user_id=user_id, username=username, passwd=passwd)
        ok, res = DB.insert(sql)
        if not ok:
            return self.fail_message(res)

        sel = """
            INSERT INTO users_groups (user_id, group_id) VALUES ('{user_id}', '{group_id}')
        """.format(user_id=user_id, group_id=group_id)
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