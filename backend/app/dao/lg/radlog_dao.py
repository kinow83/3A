import time
from app.lib.mariadb import DB
from app.lib.resource import DaoResource
from app.lib.ret import OK, FAIL

class RadlogDao(DaoResource):
    def get_radauthlog(self):
        user_id = self.p.get("user_id")

        where_sql = ""
        if user_id:
            where_sql += "AND A.user_id = '{}'".format(user_id)

        sql = """
            SELECT A.user_id, IF(A.result=1, 'success', 'failure') result, A.reason, A.authdate, B.username
            FROM radpostauth A
            LEFT JOIN users B ON A.user_id = B.user_id
            WHERE 1=1 {where_sql}
        """.format(where_sql=where_sql)
        return DB.select(sql)