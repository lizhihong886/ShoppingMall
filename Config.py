#!/usr/bin/env/ python
# -*-coding:utf-8 -*-

#DB
PY_MYSQL_CONN_DICT={
    "host":'127.0.0.1',
    "port":3306,
    "user":'root',
    "passwd":'a741258963',
    "db":'ShoppingDB',
    "charset":'utf8',
}



#Session的类型：cache/py_redis/memcached
SESSION_TYPE='redis'
#Session超时时间
SESSION_EXPIRES=60*20
LOGIN_URL='/login'