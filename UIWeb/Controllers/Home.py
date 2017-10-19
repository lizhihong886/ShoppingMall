#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Model.Category import CategoryService
from Repository.CategoryRepository import CategoryRepository

import json
from Model.Product import ProductService
from Repository.ProductRepository import ProductRepository

from tornado import escape
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        #获取一级分类
        #循环一级分类，获取二级分类
        #循环二级分类，获取三级分类
        c=CategoryService(CategoryRepository())
        category_list=c.fetch_all_category()
        p=ProductService(ProductRepository())
        product_dict=p.fetch_index_product()