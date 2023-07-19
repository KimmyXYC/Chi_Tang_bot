# -*- coding: utf-8 -*-
# @Time: 2023/7/19 19:13 
# @FileName: Base.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import rtoml


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


class Tool(object):

    def dict_to_obj(self, dict_obj):
        if not isinstance(dict_obj, dict):
            return dict_obj
        d = Dict()
        for k, v in dict_obj.items():
            d[k] = self.dict_to_obj(v)
        return d


class ReadConfig(object):

    def __init__(self):
        self.config = None

    def parse_file(self, paths):
        data = rtoml.load(open(paths, 'r'))
        self.config = Tool().dict_to_obj(data)
        return self.config
