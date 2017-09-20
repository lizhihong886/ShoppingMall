#!/usr/bin/env/ python
# -*-coding:utf-8 -*-

import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        #调用协调者
        self.render("index.html")

class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        from Model.User import UserService
        from Repository.UserRepository import UserRepository
        service=UserService() #依赖注入已自动把UserRepository()传递进去
        obj=service.check_login(user=None,email=None,pwd=None)
        print(obj.username)
        print(obj.vip_obj.caption)
        print(obj.vip_obj.nid)

