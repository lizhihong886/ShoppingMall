#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
#模型
class ProductModel:
    pass

#接口
class IProductRepository:
    def fetch_count_by_merchant(self,merchant_id):
        raise Exception("NotImplementException")
    def get_page_by_merchant_id(self, merchant_id, start, rows):
        raise Exception("NotImplementException")

    def get_product_by_id(self, product_id):
        raise Exception("NotImplementException")

    def create_product(self,product_dict,detail,img_list):
        raise Exception("NotImplementException")

    def get_price_by_product_id(self, merchant_id, product_id):
        raise Exception("NotImplementException")

    def get_product_detail(self, merchant_id, product_id):
        raise Exception("NotImplementException")

    def create_price(self,price_dict):
        raise Exception("NotImplementException")

    def update_price(self, merchant_id, product_id, nid, input_dict):
        raise Exception("NotImplementException")

    def get_upv(self, merchant_id, product_id):
        raise Exception("NotImplementException")

    def create_puv(self, product_id, ip):
        raise Exception("NotImplementException")

    def fetch_index_product(self):
        raise Exception("NotImplementException")

    def fetch_product_detail(self, product_id, price_id):
        raise Exception("NotImplementException")



#调用者
class ProductService:
    def __init__(self,product_repository):
        self.product_repository=product_repository
    def fetch_count_by_merchant(self,merchant_id):
        db_result=self.product_repository.fetch_count_by_merchant(merchant_id)
        return db_result
    def get_page_by_merchant_id(self,merchant_id,start,rows):
        count=self.fetch_count_by_merchant(merchant_id)
        db_result=self.product_repository.get_page_by_merchant_id(merchant_id,start,rows)
        return db_result,count
    def get_product_by_id(self,product_id):
        pass
    def create_product(self,merchant_id,input_dict):
        pass
    def get_price_by_product_id(self,merchant_id,product_id):
        pass
    def get_product_detail(self,merchant_id,product_id):
        pass
    def create_price(self,merchant_id,product_id,input_dict):
        pass
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
