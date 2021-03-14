import json
import importlib
from flask import request
from flask_restful import Resource
from functools import wraps
from app.lib.stringcase import camelcase
from app.core.dao import DAO
from app.core.exceptions import api_error_check


class API(Resource):
    def __init__(self):
        '''
        self.p = parameter
        self.m = meta
        '''
        super().__init__()
        self.p = self.__get_parameters()
        self.m = self.__get_meta()
        self.dao = DAO(self.p, self.m)
        self.dao_mapper = {}
        self.init_dao()


    def init_dao(self):
        pass


    @api_error_check
    def call(self, method):
        daos = self.dao_mapper.get(method)
        if not daos:
            daos = self.dao_mapper.get("default")
        if not daos:
            raise Exception("not found DAO of {}".format(method))

        results = []
        if isinstance(daos, str):
            daos = [daos]
        for dao in daos:
            res = self.dao.call(dao, method)
            results.append(res)

        return self.__response(results)
        

    def __response(self, results):
        if len(results) == 1:
            return {"result": results[0]}, 200
        return {"result": results}, 200


    def __get_parameters(self):
        # GET Method parameters
        parameters = request.args.to_dict() or {}
        for key in request.args.keys():
            mul = request.args.getlist(key)
            if mul:
                if len(mul) == 1:
                    parameters[key] = mul[0]
                elif len(mul) > 1:
                    parameters[key] = mul

        # POST Method parameters
        bodydata = self.__get_body_data()
        if isinstance(bodydata, dict):
            for k, v in bodydata.items():
                parameters.setdefault(k, v)

        return parameters


    def __get_body_data(self):
        try:
            if request.is_json:
                data = request.get_json()
            elif request.mimetype in ('multipart/form-data', 'application/x-www-form-urlencoded'):
                data = request.form.to_dict()
            else:
                data = dict()
        except Exception as e:
            data = dict()
        return data


    def __get_header_data(self):
        return request.headers


    def __get_meta(self):
        meta = {}
        meta_func = [self.__get_client_ip]
        for func in meta_func:
            k, v = func()
            meta[k] = v
        return meta


    def __get_client_ip(self):
        remote_addr = request.headers.get('X-Forwarded-For')
        if remote_addr:
            remote_addr = remote_addr.split(',')[0]    
        if not remote_addr:
            remote_addr = request.headers.get('X-Real-IP')

        return ("client_ip", remote_addr)