#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import pymysql
from Config import PY_MYSQL_CONN_DICT

class DbConnection:
    def __init__(self):
        self.__conn_dict=PY_MYSQL_CONN_DICT
        self.conn=None
        self.cursor=None
    def connect(self,cursor=pymysql.cursors.DictCursor):
        self.conn=pymysql.connect(**self.__conn_dict)
        self.cursor=self.conn.cursor(cursor=cursor)#以字典的形式返回
        return self.cursor
    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
