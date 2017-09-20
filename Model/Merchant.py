#!/usr/bin/env/ python
# -*-coding:utf-8 -*-

#模型
class MerchantModel:
    pass


#接口
class IMerchantRepository:
    def fetch_merchant_count(self):
        raise Exception("NotImplementedException")
    def fetch_merchant_by_page(self,start,rows):
        raise Exception("NotImplementedException")
    def fetch_merchant_detail_by_nid(self,nid):
        raise Exception("NotImplementedException")
    def add_merchant(self,**kwargs):
        raise Exception("NotImplementedException")
    def update_merchant(self,nid,**kwargs):
        raise Exception("NotImplementedException")
    def get_merchant_detail_by_nid(self, nid):
        raise Exception("NotImplementedException")
    def delete_merchant(self, nid):
        raise Exception("NotImplementedException")

from Infrastructure.DI.DI import MetaClass
#协调者
class MerchantService(metaclass=MetaClass):#依赖注入
    def __init__(self,merchant_repository):
        """
        :param merchant_repository: 数据仓库对象
        """
        self.merchant_repository=merchant_repository

    def fetch_merchant_count(self):
        count=self.merchant_repository.fetch_merchant_count()
        return count
    def fetch_merchant_by_page(self,start,rows):
        data=self.merchant_repository.fetch_merchant_by_page(start,rows)
        return data
    def fetch_merchant_detail_by_nid(self,nid):
        data=self.merchant_repository.fetch_merchant_detail_by_nid(nid)
        return data
    def add_merchant(self,**kwargs):
        ret=self.merchant_repository.add_merchant(**kwargs)
        return ret
    def update_merchant(self,nid,**kwargs):
        ret=self.merchant_repository.update_merchant(nid,**kwargs)
        return ret
    def delete_merchant(self,nid):
        ret=self.merchant_repository.delete_merchant(nid)
        return ret
