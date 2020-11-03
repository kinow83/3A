from app.lib.utils import *
import re

def OK(data={}):
    return True, data

mysql_exception_re = re.compile("<class 'pymysql.err..*'>")

def FAIL(cause):
    if mysql_exception_re.match(str(type(cause))):
        code, msg = cause.args
        return False, quotes(msg)
    return False, quotes(cause)
