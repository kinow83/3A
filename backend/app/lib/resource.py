import json
from flask import request
from flask_restful import Resource
from functools import wraps
from app.lib.ret import OK, FAIL

class DaoResource():
    '''
    DAO
    '''
    def __init__(self, pdict):
        self.p = pdict
        print(self.p)

    def required(self, vars):
        vs = vars
        if type(vars) != list:
            vs = [vars]
        for v in vs:
            if not self.p.get(v):
                return False, v
        return True, ''

    def fail_required(self, cause):
        return FAIL("required parameter: {}".format(cause))

    def fail_unknown(self, name, value):
        return FAIL("unknown {}: {}".format(name, value))

class ApiResource(Resource):
    '''
    API
    '''
    def __init__(self):
        super().__init__()
        self.p = self.parameters()

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
