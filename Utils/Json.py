# -*- coding: utf-8 -*-
# @Time: 2023/7/19 20:01 
# @FileName: Json.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import json
import pathlib


def get_config_file():
    with open((str(pathlib.Path.cwd()) + "/Config/fadian.json"), 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        json_file.close()
    return data
