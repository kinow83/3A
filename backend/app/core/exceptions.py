import logging

from flask import request, jsonify
from functools import wraps
from flask_babel import gettext, ngettext, lazy_gettext
from flask_babel import gettext

logger = logging.getLogger(__name__)


class CM:
    def __init__(self, code, message):
        self.code = str(code)
        self.message  = message

class ApiException(Exception):
    def __init__(self, cm, cause=None):
        super().__init__()

        self.code = cm.code
        self.message = cm.message
        self.cause = cause

    def set_message(self, msg):
        self.message = msg

    def to_dict(self):
        res = {}
        res["code"] = self.code
        res["message"] = self.message
        return res

    def __str__(self):
        return '{}({})'.format(self.message, self.code)

    def __repr__(self):
        return '<{} {}: {}>'.format(self.__class__.__name__, self.code, self.message)


def api_error_check(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        try:
            return f(self, *args, **kwargs)
        except ApiException as e:       
            lazy_message = lazy_gettext(e.message, **e.cause)            
            e.set_message(str(lazy_message))
            response = jsonify(e.to_dict())
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify(e)
            response.status_code = 400
            return response
    return wrapper
