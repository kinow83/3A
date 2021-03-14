from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL
from app.dao.mysql.hr.users_dao import UsersDao
from app.dao.mysql.hr.groups_dao import GroupsDao

class NasDao(DaoResource):
    def get_nas(self, vp=None):
        vp = vp if vp else self.p

        nas_id = vp.get("nas_id")
        nasname = vp.get("nasname")
        where_sql = ""

        if nas_id:
            where_sql += "AND nas_id = '{}'".format(nas_id)
        if nasname:
            where_sql += "AND nasname = '{}'".format(nasname)

        sql = "SELECT * FROM nas WHERE 1=1 {where_sql}".format(where_sql=where_sql)
        ok, res = DB.select(sql)
        if not ok:
            return self.fail_message(res)

        for nas in res:
            secret = nas.get("secret")
            if secret:
                pass

        return OK(res)

    def set_nas(self, vp=None):
        vp = vp if vp else self.p

        ok, res = self.required(["nasname", "shortname", "secret"])
        if not ok:
            return self.fail_required(res)

        nasname = vp.get("nasname")
        shortname = vp.get("shortname")
        secret = vp.get("secret")

        ok, res = self.get_nas({"nasname": nasname})
        if not ok:
            return FAIL(res)
        if len(res) > 0:
            return fail_duplicated("nasname")


    def del_nas(self):
        pass

    def mod_nas(self):
        pass