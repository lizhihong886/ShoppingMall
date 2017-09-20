#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import tornado.web
from Model.Product import ProductService
from Repository.ProductRepository import ProductRepository
import json
from UIAdmin.Forms.Product import JdProductPriceForm,JdProductForm
from Infrastructure.JsonEnoder import JsonCustomEncoder

class JdProductManager(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("Product/productManager.html")

class JdProductHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 根据参数，获取产品信息（type：自营（商户ID），type：所有商品）
        # 后台管理用户登陆成功后，Session中保存自营ID
        # 自营ID＝1
        ret={"status":False,"message":"","total":0,"rows":[]}
        try:
            merchant_id=6
            page=int(self.get_argument("page",1))
            rows=int(self.get_argument("rows",10))
            start=(page-1)*10
            service=ProductService(ProductRepository())
            total,data=service.get_page_by_merchant_id(merchant_id,start,rows)
            ret["status"]=True
            ret["total"]=total
            ret["rows"]=data
        except Exception as e:
            ret["message"]=str(e)
        self.write(json.dumps(ret))

class JdProductEditHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("Product/JdProductEdit.html")

    def post(self,*args,**kwargs):
        ret={"status":False,"summary":"","detail":""}
        form=JdProductForm()
        try:
            is_valid=form.valid(self)
            if is_valid:
                merchant_id=6
                print("data",form._value_dict)
                service=ProductService(ProductRepository())
                service.create_product(merchant_id,form._value_dict)
                ret["status"]=True
            else:
                ret["detail"]=form._error_dict
        except Exception as e:
            ret["summary"]=str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        product_id = self.get_argument("nid")
        print(product_id)
        ret={"summary":"","status":False}
        if product_id:
            try:
                service=ProductService(ProductRepository())
                db_result=service.delete_product(product_id)
                if db_result:
                    ret["status"]=True
                else:
                    raise Exception("删除失败")
            except Exception as e:
                print(e)
                ret["summary"]=str(e)
        else:
            ret["summary"]="请选择要删除的行"
        self.write(json.dumps(ret))

class JdProductPriceManagerHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        ret={"status":False,"summary":"","data":{}}
        try:
            product_id=self.get_argument('product_id',None)
            print(product_id)
            if not product_id:
                raise Exception("请输入产品Id")
            else:
                merchant_id=6
                service=ProductService(ProductRepository())
                data=service.get_product_by_id(merchant_id=merchant_id,product_id=product_id)
                if not data:
                    raise Exception("未获取到商品信息")
                ret["status"]=True
                ret["data"]=data
        except Exception as e:
            ret["summary"]=str(e)

        self.render("Product/JdProductPriceManager.html",**ret)

class JdProdutPriceHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        ret={"status":False,"summary":"","total":0,"row":[]}
        try:
            product_id=self.get_argument("product_id",None)
            if not product_id:
                raise Exception("商品id不能为空")
            merchant_id=6
            service=ProductService(ProductRepository())
            total,result=service.get_price_by_product_id(merchant_id=merchant_id,product_id=product_id)
            ret["total"]=total
            ret['rows']=result
            print(total)
            print("result:",result)
            ret["status"]=True
        except Exception as e:
            print(e)
            ret["summary"]=str(e)
        self.write(json.dumps(ret,cls=JsonCustomEncoder))

    def post(self, *args, **kwargs):
        ret={"status":False,"summary":"","detail":{}}
        try:
            form =JdProductPriceForm()
            is_valid=form.valid(self)
            if is_valid:
                form._value_dict.pop("nid")
                merchant_id=6
                service=ProductService(ProductRepository())
                service.create_price(merchant_id,form._value_dict["product_id"],form._value_dict)
            else:
                ret["detail"]=form._error_dict
                raise Exception("输入内容不合法")
            ret["status"]=True
        except Exception as e:
            ret["summary"]=str(e)
        self.write(json.dumps(ret))

    def put(self,*args,**kwargs):
        ret={"status":False,"summary":"","detail":{}}
        try:
            form=JdProductPriceForm()
            is_valid=form.valid(self)
            if is_valid:
                nid=form._value_dict.pop("nid")
                merchant_id=6
                service=ProductService(ProductRepository())
                service.update_price(merchant_id,form._value_dict["product_id"],nid,form._value_dict)
            else:
                ret["detail"]=form._error_dict
                raise Exception("输入内容不合法")
            ret['status']=True
        except Exception as e:
            ret["summary"]=str(e)
        self.write(json.dumps(ret))

    def delete(self,*args,**kwargs):
        pass

class JdProductDetailHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        merchant_id=6
        product_id=self.get_argument("product_id",None)
        service=ProductService(ProductRepository())
        series=service.get_product_detail(merchant_id,product_id)
        self.render("Product/JdProductDetail.html",series=series)

class JdProductViewHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        ret={"status":False,"summary":"","data":[]}
        try:
            merchant_id=6
            product_id=self.get_argument("product_id",None)
            if not product_id:
                raise Exception("请输入商品ID")
            service=ProductService(ProductRepository())
            series=service.get_upv(merchant_id,product_id)
            ret["data"]=series
            ret["status"]=True
        except Exception as e:
            ret["summary"]=str(e)
        self.write(json.dumps(ret))