#!/usr/bin/env/ python
# -*-coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from UIAdmin.Controllers import Account,Region,Merchant,Product,Image
import BootMapper #导入一下BootMapper使其运行

settings={
    "debug":"True",
    'template_path':'Views' ,
    'static_path':'Statics',
    "static_url_prefix":"/Statics/",
}
#路由映射，路由系统
application = tornado.web.Application([
    (r"/index.html", Account.MainHandler),
    (r"/province.html", Region.Province),
    (r'/provinceManager.html', Region.Province_data),
    (r"/city.html", Region.City),
    (r"/cityManager.html", Region.City_data),
    (r"/country.html", Region.Country),
    (r"/countryManager.html", Region.Country_data),
    (r"/merchant.html", Merchant.MerchantHandler),
    (r"/merchantManager.html",Merchant.MerchantManagerHandler),
    (r"/merchantEdit.html",Merchant.MerchantEdit),
    (r"/productManager.html",Product.JdProductManager),
    (r"/JdProduct.html$",Product.JdProductHandler),
    (r"/JdProductEdit.html$",Product.JdProductEditHandler),
    (r"/UploadImg.html",Image.UploadImageHandler),
    (r"/JdProductPriceManager.html",Product.JdProductPriceManagerHandler),
    (r"/JdProductPrice.html",Product.JdProdutPriceHandler)
] ,**settings)#应用到tornado中，使其生效
# Application对象是负责全局配置的, 包括映射请求转发给处理程序的路由表.

if __name__ == "__main__":
    application.listen(5858)
    tornado.ioloop.IOLoop.instance().start()