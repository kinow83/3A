import json
import importlib
from flask import request
from flask_restful import Resource
from functools import wraps
from app.lib.ret import OK, FAIL
from app.lib.stringcase import camelcase

class DaoResource():
    '''
    DAO
    '''
    def __init__(self, pdict, dbtype="mysql"):
        self.p = pdict
        self.dbtype = dbtype

    def required(self, vars):
        vs = vars
        if type(vars) != list:
            vs = [vars]
        for v in vs:
            if not self.p.get(v):
                return False, v
        return True, ''
        
    def call(self, path, method):
        '''
        experimentation
        '''
        print("[DAO] input: {}".format(self.p))
        
        try:
            mod = importlib.import_module(path)
        except Exception as e:
            print("[ERROR] call(self, {}, {}): {}".format(path, method, e))
        dao = path.rsplit('.')[-1] # last domain

        cls = getattr(mod, camelcase(dao))
        inst = cls(self.p)
        find_method = getattr(cls, method)
        if find_method:
            return find_method(inst)
        return None

    def fail_duplicated(self, name):
        return FAIL("duplicate: {}".format(name))

    def fail_required(self, cause):
        return FAIL("required parameter: {}".format(cause))

    def fail_unknown(self, name, value):
        return FAIL("unknown {}: {}".format(name, value))

    def fail_message(self, msg):
        return FAIL("FAIL: {}".format(msg))

class ApiResource(Resource):
    '''
    API
    '''
    def __init__(self):
        super().__init__()
        self.p = self.parameters()
        self.dao = DaoResource(self.p)
        self.dao_mapper = {}

        init_method = None
        try:
            init_method = getattr(self, "init")
        except Exception as e:
            print(e)
            pass
        else:
            if init_method:
                init_method()

    def dao_response(self, api):
        path = self.dao_mapper.get(api)
        if path:
            print("[API] {}.{}".format(path, api))
            return self.response(self.dao.call(path, api))
        else:
            defpath = self.dao_mapper.get("default")
            print("[API] {}.{}".format(defpath, api))
            return self.response(self.dao.call(defpath, api))

    def response(self, ok_res):        
        ok = ok_res[0]
        res = ok_res[1]
        if ok:
            http_res = {'result': res}, 200
        else:
            http_res = {'result': res}, 400

        try:
            print(json.dumps(res, indent = 2))
        except Exception as e:
            print("response error: {}".format(e))
        return http_res

    '''
    @deprecared
    def requires_ok(self, vars):
        vs = vars
        if type(vars) != list:
            vs = [vars]
        for v in vs:
            if not self.p.get(v):
                return False, v
        return True, ''
    '''

    def parameters(self):
        parameter = request.args.to_dict() or {}
        for key in request.args.keys():
            mul = request.args.getlist(key)
            if mul:
                if len(mul) == 1:
                    parameter[key] = mul[0]
                elif len(mul) > 1:
                    parameter[key] = mul

        body = self.bodydata()
        if isinstance(body, dict):
            for k, v in body.items():
                parameter.setdefault(k, v)

        return parameter

    def bodydata(self):
        try:
            if request.is_json:
                data = request.get_json()
            elif request.mimetype in ('multipart/form-data', 'application/x-www-form-urlencoded'):
                data = request.form.to_dict()
            else:
                raise ValueError('mimetype is not exists.')
        except Exception as e:
            data = dict()
        return data

    def headdata(self):
        return request.headers

    def client_ip():
        remote_addr = request.headers.get('X-Forwarded-For')
        if remote_addr:
            remote_addr = remote_addr.split(',')[0]    
        if not remote_addr:
            remote_addr = request.headers.get('X-Real-IP')

        return remote_addr
