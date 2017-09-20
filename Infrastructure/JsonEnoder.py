#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import json
from datetime import date
from datetime import datetime
from decimal import Decimal

# json不能序列化datatime、Decimal等数据结构
# 通过自定义处理器来做扩展
class JsonCustomEncoder(json.JSONEncoder):
    def default(self,field):
        if isinstance(field,datetime):
            return field.strftime("%Y-%m-%d %H;%M:%S")
        elif isinstance(field,date):
            return field.strftime("%Y-%m-%d")
        elif isinstance(field,Decimal):
            return str(field)
        else:
            return json.JSONEncoder.default(self,field)
