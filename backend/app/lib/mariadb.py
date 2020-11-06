import pymysql
from functools import wraps
from app.lib.ret import OK, FAIL

class MariaDB():
    def __init__(self):
        self.connect_info = {
            'host': "localhost",
            'port': 3306,
            'user': "radius",
            'passwd': "radpass",
            'db': "radius",
            'autocommit': True,
            'charset': "utf8",
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.conn = None
        self.cursor = None


    def open(self):
        try:
            # TODO: remove datetime convert function
            from pymysql.constants import FIELD_TYPE
            from pymysql.converters import conversions as conv
            conv = conv.copy()
            del conv[FIELD_TYPE.DATETIME]
            conv[10]=str

            self.conn = pymysql.connect(
                        #unix_socket='/secui/config/db/mysql.sock',
                        host = self.connect_info.get('host'),
                        port = self.connect_info.get('port'),
                        user = self.connect_info.get('user'),
                        passwd = self.connect_info.get('passwd'),
                        db = self.connect_info.get('db'),
                        autocommit = self.connect_info.get('autocommit'),
                        charset = self.connect_info.get('charset'),
                        cursorclass = self.connect_info.get('cursorclass'),
                        conv=conv)
        except:
            raise
        else:
            self.cursor = self.conn.cursor()
            return self

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None

        if self.cursor:
            self.conn.close()
            self.conn = None

    def execute(self, cmd):
        cmd = cmd.strip()
        print("[DB] sql: {}".format(cmd))
        return self.cursor.execute(cmd)

    def callproc(self, procname, args=()):
        return self.cursor.callproc(procname, args)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()


def dbio(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = MariaDB()
        db.open()
        res = func(db, *args, **kwargs)
        db.close()
        return res
            
    return wrapper

class DB():
    @staticmethod
    @dbio
    def insert(db, cmd):
        try:
            db.execute(cmd)
            return OK()
        except Exception as e:
            return FAIL(e)

    @staticmethod
    @dbio
    def update(db, cmd):
        try:
            db.execute(cmd)
            return OK()
        except Exception as e:
            return FAIL(e)

    @staticmethod
    @dbio
    def delete(db, cmd):
        try:
            db.execute(cmd)
            return OK()
        except Exception as e:
            return FAIL(e)

    @staticmethod
    @dbio
    def callproc(db, procname, args=()):
        try:
            return OK(db.callproc(procname, args))
        except Exception as e:
            return FAIL(e)

    @staticmethod
    @dbio
    def select(db, cmd):
        try:
            if db.execute(cmd) > 0:
                return OK(db.fetchall())
            else:
                return OK([])
        except Exception as e:
            return FAIL(e)
        
    @staticmethod
    @dbio
    def selectone(db, cmd):
        try:
            if db.execute(cmd) > 0:
                return OK(db.fetchone())
            else:
                return OK({})
        except Exception as e:
            return FAIL(e)