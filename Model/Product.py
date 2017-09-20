#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import time,json
#模型
class ProductModel:
    pass

#接口
class IProductRepository:
    def fetch_count_by_merchant(self,merchant_id):
        raise Exception("NotImplementException")
    def get_page_by_merchant_id(self, merchant_id, start, rows):
        raise Exception("NotImplementException")

    def get_product_by_id(self, merchant_id,product_id):
        raise Exception("NotImplementException")

    def create_product(self,product_dict,detail,img_list):
        raise Exception("NotImplementException")

    def delete_product(self, product_id):
        raise Exception("NotImplementException")

    def get_price_by_product_id(self, merchant_id, product_id):
        raise Exception("NotImplementException")

    def get_product_detail(self,product_id):
        raise Exception("NotImplementException")

    def create_price(self,price_dict):
        raise Exception("NotImplementException")

    def update_price(self, merchant_id, product_id, nid, input_dict):
        raise Exception("NotImplementException")
    def fetch_price_count(self,product_id):
        raise Exception("NotImplementException")
    def get_upv(self, merchant_id, product_id):
        raise Exception("NotImplementException")

    def create_puv(self, product_id, ip):
        raise Exception("NotImplementException")

    def fetch_index_product(self):
        raise Exception("NotImplementException")

    def fetch_detail_list(self, product_id, price_id):
        raise Exception("NotImplementException")



#调用者
class ProductService:
    def __init__(self,product_repository):
        self.product_repository=product_repository
    def fetch_count_by_merchant_id(self,merchant_id):
        db_result=self.product_repository.fetch_count_by_merchant(merchant_id)
        return db_result
    def get_page_by_merchant_id(self,merchant_id,start,rows):
        count=self.fetch_count_by_merchant_id(merchant_id)
        db_result=self.product_repository.get_page_by_merchant_id(merchant_id,start,rows)
        return count,db_result,
    def get_product_by_id(self,merchant_id,product_id):
        db_result=self.product_repository.get_product_by_id(merchant_id,product_id)
        return db_result
    def create_product(self,merchant_id,input_dict):
        product_dict={
            "merchant_id":merchant_id,
            "title":input_dict["title"],
            "img":input_dict["img"],
            "category_id":1,
            "ctime":time.strftime("%Y-%m-%d")
        }
        detail_list=json.loads(input_dict["detail_list"])
        img_list=json.loads(input_dict["img_list"])
        self.product_repository.create_product(product_dict,detail_list,img_list)

    def delete_product(self,product_id):
        # 删除商品
        db_result=self.product_repository.delete_product(product_id)
        return db_result
    def get_price_by_product_id(self,merchant_id,product_id):
        total=self.product_repository.fetch_price_count(product_id)
        db_result=self.product_repository.get_price_by_product_id(merchant_id,product_id)
        return total,db_result
    def get_product_detail(self,merchant_id,product_id):
        db_result=self.product_repository.fetch_detail_list(merchant_id,product_id)
        return db_result
    def create_price(self,merchant_id,product_id,input_dict):
        #检查当前用户是否有权限为该商品增加规格
        is_valid=self.product_repository.get_product_by_id(merchant_id,product_id)
        if not is_valid:
            raise Exception("无权创建规格")
        self.product_repository.create_price(input_dict)
    def update_price(self,merchant_id,product_id,nid,input_dict):
        pass
    def get_upv(self,merchant_id,product_id):
        pass
    def create_puv(self,product_id,ip):
        pass
    def fetch_index_product(self):
        pass
    def fetch_product_detail(self,product_id,price_id):
        pass
