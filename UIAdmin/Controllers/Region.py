#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import tornado.web
import json
from Model.Region import ProvinceService,CityService,CountryService

class Province(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("province")

        self.render("Region/province.html")

class Province_data(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        if self.get_argument("type",None)=="all":
            ret={"status":False,"rows":"","summary":''}
            try:
                service_province=ProvinceService()
                data=service_province.fetch_province()
                ret['status']=True
                ret["rows"]=data
            except Exception as e:
                ret["summary"]=str(e)
            self.write(json.dumps(ret))
        else:
            page=int(self.get_argument("page",1))
            rows=int(self.get_argument("rows",10))
            start=(page-1)*rows
            service_province=ProvinceService()
            total=service_province.fetch_province_count()
            data_list=service_province.fetch_province_by_page(start,rows)
            data_list=list(data_list)
            data={"total":total,"rows":data_list}
            self.write(json.dumps(data))

    def post(self, *args, **kwargs):
        """
        添加
        :param args: 
        :param kwargs: 
        :return: 
        """
        ret={'status':False,"summary":""}
        caption=self.get_argument("caption")
        if not caption:
            ret['summary']="省份不能为空"
        else:
            try:
                service_province=ProvinceService()
                result=service_province.add_province(caption)
                if not result:
                    ret['summary'] = "该省份已存在"
                else:
                    ret['status']=True
            except Exception as e:
                print(str(e))
                ret['summary']=str(e)
        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        ret={"status":False,"summary":""}
        nid=self.get_argument("nid",None)
        caption=self.get_argument("caption",None)
        if not nid:
            ret["summary"]="请选择要编辑的行"
        else:
            try:
                service_province=ProvinceService()
                result=service_province.update_province(nid,caption)
                if result:
                    ret["status"]=True
                else:
                    ret["summary"]="该省份已存在"
            except Exception as e:
                ret["summary"]=str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        ret={'statue':False,"summary":""}
        nid=self.get_argument("nid")
        if not nid:
            ret['summary']="请选择要删除的行"
        else:
            try:
                # 如果删除失败，则显示错误信息
                service_province=ProvinceService()
                service_province.delete_province(nid)
                ret["status"] = True
            except Exception as e:
                ret["summary"]=str(e)
        self.write(json.dumps(ret))

class City(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("Region/city.html")
class City_data(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        type=self.get_argument("type",None)
        if type=="province":
            ret={"message":"","status":False,"rows":""}
            try:
                province_id=self.get_argument("province_id")
                service_city=CityService()
                data=service_city.fetch_city_by_province(province_id)
                ret["status"]=True
                ret["rows"]=data
            except Exception as e:
                ret["message"]=str(e)
            self.write(json.dumps(ret))
        else:
            page=int(self.get_argument('page',1))
            rows=int(self.get_argument("rows",10))
            start = (page - 1)*rows
            service_city = CityService()
            total = service_city.fetch_city_count()
            data = service_city.fetch_city_by_page(start,rows)
            ret = {"total": total, "rows": data}
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        """
        添加: 
        """
        ret={"summary":"","status":False}
        caption = self.get_argument("caption", None)
        province_id = self.get_argument("province_id", None)
        if caption:
            try:
                service_city=CityService()
                db_result=service_city.add_city(caption,province_id)
                if db_result:
                    ret["status"]=True
                else:
                    ret["summary"]='该城市已存在'
            except Exception as e:
                print(e)
                ret["summary"]="添加失败"
        else:
            ret["summary"]="城市不能为空"
        self.write(json.dumps(ret))

    def put(self,*args,**kwargs):
        ret = {"summary": "","status":False}
        nid=self.get_argument("nid",None)
        caption=self.get_argument("caption",None)
        province_id=self.get_argument("province_id",None)
        print(province_id)
        if caption:
            try:
                service_repository=CityService()
                db_result=service_repository.update_city(nid,caption,province_id)
                if db_result:
                    ret["status"]=True
                else:
                    ret["summary"]="该城市已存在"
            except Exception as e:
                print(e)
                ret["summary"]="修改失败"
        else:
            ret['summary']='城市不能为空'
        self.write(json.dumps(ret))

    def delete(self,*args,**kwargs):
        ret={"summary":"","status":False}
        nid=self.get_argument("nid",None)
        if nid:
            try:
                service_repository=CityService()
                db_result=service_repository.delete_city(nid)
                ret["status"]=True
            except Exception as e:
                print(e)
                ret["summary"]="删除失败"
        else:
            ret["summary"]="请选择要删除的行"
        self.write(json.dumps(ret))


class Country(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("Region/country.html")
class Country_data(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        type=self.get_argument("type",None)
        if type=="city":
            ret={"message":"","status":False,"rows":[]}
            try:
                city_id=self.get_argument("city_id",None)
                service=CountryService()
                rows=service.fetch_country_by_city(city_id)
                ret["rows"]=rows
                ret["status"]=True
            except Exception as e:
                ret["message"]=str(e)
            self.write(json.dumps(ret))
        else:
            page=int(self.get_argument("page",1))
            rows=int(self.get_argument("rows",10))
            start=(page-1)*rows
            service_country=CountryService()
            total=service_country.fetch_country_count()
            data=service_country.fetch_country_by_page(start,rows)
            ret={"total":total,"rows":data}
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        ret = {"summary": "", "status": False}
        caption=self.get_argument("caption",None)
        city_id=int(self.get_argument("city_id",None))
        if caption:
            try:
                service_country=CountryService()
                db_result=service_country.add_country(caption,city_id)
                if db_result:
                    ret["status"]=True
                else:
                    ret['summary']="该县（区）已存在"
            except Exception as e:
                ret["summary"] = str(e)
        else:
            ret["summary"]="县(区)不能为空"
        self.write(json.dumps(ret))


    def put(self, *args, **kwargs):
        ret={"summary":"","status":False}
        nid=self.get_argument("nid",None)
        caption=self.get_argument("caption",None)
        city_id=self.get_argument("city_id",None)
        if caption:
            try:
                service_country=CountryService()
                db_result=service_country.update_country(nid,caption,city_id)
                if db_result:
                    ret["status"]=True
                else:
                    ret["summary"]="该县区已存在"
            except Exception as e:
                ret["summary"]=str(e)
        else:
            ret["summary"]="县区不能为空"
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        ret={"summary":"","status":False}
        nid=self.get_argument("nid",None)
        print(nid)
        if nid:
            try:
                service_country=CountryService()
                db_result=service_country.delete_country(nid)
                print(db_result)
                if db_result:
                    ret['status']=True
                else:
                    ret["summary"]="删除失败"
            except Exception as e:
                ret["summary"]=str(e)
        else:
            ret['summary']="请选择要删除的行"
        self.write(json.dumps(ret))





