#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Infrastructure.DI.DI import MetaClass

#模型

#接口
class IProvinceRepository():
    def __init__(self):
        pass
    def fetch_province_count(self):
        raise Exception("NotImplementedException")
    def fetch_province(self):
        raise Exception("NotImplementedException")
    def fetch_province_by_page(self,start,rows):
        raise Exception("NotImplementedException")
    def add_province(self,caption):
        raise Exception("NotImplementedException")
    def update_province(self,nid,caption):
        raise Exception("NotImplementedException")
    def delete_province(self,nid):
        raise Exception("NotImplementedException")
    def is_exist(self,caption):
        raise Exception("NotImplementedException")

class ICityRepository():
    def __init__(self):
        pass
    def fetch_city_count(self):
        raise Exception("NotImplementedException")
    def fetch_city_by_province(self,province_id):
        raise Exception("NotImplementedException")
    def fetch_city_by_page(self,start,rows):
        raise Exception("NotImplementedException")
    def add_city(self,caption,province_id):
        raise Exception("NotImplementedException")
    def update_city(self,nid,caption,province_id):
        raise Exception("NotImplementedException")
    def delete_city(self,nid):
        raise Exception("NotImplementedException")
    def is_exist(self,caption,province_id):
        raise Exception("NotImplementedException")

class ICountryRepository:
    def fetch_country_count(self):
        raise Exception("NotImplementException")
    def fetch_country_by_page(self,start,rows):
        raise Exception("NotImplementException")
    def add_country(self,caption,city_id):
        raise Exception("NotImplementException")
    def update_country(self,nid,caption,city_id):
        raise Exception("NotImplementException")
    def delete_country(self,nid):
        raise Exception("NotImplementException")
    def is_exist(self,caption,city_id):
        raise Exception("NotImplementException")
    def fetch_country_by_city(self, city_id):
        raise Exception("NotImplementException")


# 协调者
class ProvinceService(metaclass=MetaClass):
    def __init__(self,province_repository):
        self.province_repository=province_repository
    def fetch_province_count(self):
        count=self.province_repository.fetch_province_count()
        return count
    def fetch_province_by_page(self,start,rows):
        db_result=self.province_repository.fetch_province_by_page(start,rows)
        return db_result
    def fetch_province(self):
        db_result=self.province_repository.fetch_province()
        return db_result
    def add_province(self,caption):
        exist=self.province_repository.is_exist(caption)
        if  not exist:
            self.province_repository.add_province(caption)
            return True
    def update_province(self,nid,caption):
        exist=self.province_repository.is_exist(caption)
        if not exist:
            result=self.province_repository.update_province(nid,caption)
            return True
    def delete_province(self,nid):
        result=self.province_repository.delete_province(nid)
        return result

class CityService(metaclass=MetaClass):
    def __init__(self,city_repository):
        self.city_repository=city_repository
    def fetch_city_count(self):
        db_result=self.city_repository.fetch_city_count()
        return db_result
    def fetch_city_by_province(self,province_id):
        db_result = self.city_repository.fetch_city_by_province(province_id)
        return db_result
    def fetch_city_by_page(self,start,rows):
        db_result = self.city_repository.fetch_city_by_page(start,rows)
        return db_result
    def add_city(self,caption,province_id):
        exist=self.city_repository.is_exist(caption,province_id)
        if not exist:
            db_result = self.city_repository.add_city(caption,province_id)
            return True
    def update_city(self,nid,caption,province_id):
        exist=self.city_repository.is_exist(caption,province_id)
        print(exist)
        if not exist:
            db_result = self.city_repository.update_city(nid,caption,province_id)
            return True
    def delete_city(self,nid):
        db_result = self.city_repository.delete_city(nid)
        return db_result
    def is_exist(self,caption,province_id):
        db_result = self.city_repository.is_exist(caption,province_id)
        return db_result

class CountryService(metaclass=MetaClass):
    def __init__(self,country_repository):
        self.country_repository=country_repository
    def fetch_country_count(self):
        db_result=self.country_repository.fetch_country_count()
        return db_result
    def fetch_country_by_page(self, start, rows):
        db_result=self.country_repository.fetch_country_by_page(start,rows)
        return db_result
    def fetch_country_by_city(self,city_id):
        db_result=self.country_repository.fetch_country_by_city(city_id)
        return db_result
    def add_country(self,caption, city_id):
        exist=self.country_repository.is_exist(caption,city_id)
        if not exist:
            print("add")
            db_result=self.country_repository.add_country(caption,city_id)
            return True
    def update_country(self, nid, caption, city_id):
        exist=self.country_repository.is_exist(caption,city_id)
        if not exist:
            db_result=self.country_repository.update_country(nid,caption,city_id)
            return True
    def delete_country(self, nid):
        db_result=self.country_repository.delete_country(nid)
        return True
    def is_exist(self, caption, city_id):
        exist=self.country_repository.is_exist(caption,city_id)
        return exist