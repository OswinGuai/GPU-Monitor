#
# Xlearn
# Author: peizhongyi(peizhyi@gmail.com)
# Initial Date: 2018.06.20
#
# Title: Wrapper for REST API
#
# Version 0.1

from flask import jsonify, make_response
class JSONWrapper(object):

    @staticmethod
    def fill_result(data, status, msg):
        result = {
                'data': data,
                'status': status,
                'msg': msg
                }
        return jsonify(result)


    @staticmethod
    def success(data='', msg='success', status=0):
        ret = make_response(JSONWrapper.fill_result(data, status, msg))
        ret.headers['Access-Control-Allow-Origin']='*'
        ret.headers['Access-Control-Allow-Methods']='GET,OPTIONS,POST,DELETE,PUT'
        ret.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
        return ret


