# -*- coding:utf-8 -*-


class Response(object):
    def __init__(self, code=0, message="", result=""):
        self.Code = code
        self.Message = message
        self.Result = result

    def object_to_dict(self):
        return self.__dict__
