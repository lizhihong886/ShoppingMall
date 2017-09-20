#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import os
import json
import tornado.web
from Infrastructure import Commons

class UploadImageHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        ret={"status":False,"data":"","summary":""}
        try:
            file_metas=self.request.files["img"]##获取图片对象
            for meta in file_metas:
                file_name=meta["filename"]
                file_path=os.path.join("Statics","Admin","Upload",Commons.generate_md5(file_name))
                with open(file_path,"wb") as up:
                    up.write(meta["body"])
                ret["status"]=True
                ret["data"]=file_path
        except Exception as e:
            ret["summary"]=str(e)
        self.write(json.dumps(ret))

