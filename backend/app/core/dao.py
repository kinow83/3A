import json
import importlib
from functools import wraps
from app.lib.stringcase import camelcase
from app.core.exceptions import ApiException


class DAO():
    def __init__(self, parameters, meta):
        self.p = parameters
        self.m = meta


    def call(self, path, method):
        try:
            module = importlib.import_module(path)
        except Exception as e:
            raise Exception("[ERROR] call: {}.{}".format(path, method))
        dao = path.rsplit('.')[-1] # last domain

        cls = getattr(module, camelcase(dao))
        inst = cls(self.p, self.m)
        method = getattr(cls, method)
        if method:
            return method(inst)
        raise Exception("[ERROR] notfound module: {}.{}".format(path, method))