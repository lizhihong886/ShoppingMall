#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Infrastructure.Form.Forms import  BaseForm
from Infrastructure.Form.Fields import IntegerField,StringField
from Infrastructure.Form import Widget
from Model.User import UserService

class MerchantForm(BaseForm):
    def __init__(self):
        self.nid = IntegerField(required=False,widget=Widget.InputText(attributes={"class":"hide"}))
        self.name=StringField(custom_error_dict={"required":"名称不能为空","valid":"名称格式错误"})
        self.domain=StringField(custom_error_dict={"required":"域名不能为空","valid":"域名格式错误"})
        self.business_mobile=StringField(custom_error_dict={"required":"业务电话不能为空","valid":"业务电话格式错误"})
        self.business_phone=StringField(custom_error_dict={"required":"业务手机不能为空","valid":"业务手机格式错误"})
        self.qq=StringField(custom_error_dict={"required":"QQ不能为空","valid":"QQ格式错误"})
        self.address=StringField(widget=Widget.TextArea(attributes={"class":"address"}),custom_error_dict={"required":"地址信息不能为空","valid":"地址格式错误"})
        self.backend_mobile=StringField(custom_error_dict={"required":"负责人电话不能为空","valid":"负责人电话格式错误"})
        self.backend_phone=StringField(custom_error_dict={"required":"负责人电话不能为空","valid":"负责人电话格式错误"})
        self.user_id=IntegerField(widget=Widget.Select(attributes={},choices=UserService().get_user_to_select()),custom_error_dict={"required":"请选择登录用户","valid":"选择登录用户错误"})
        self.province_id=IntegerField(widget=Widget.Select(attributes={"id":"my_province"},choices=[{"value":0,"text":"请选择省份"}]),custom_error_dict={"required":"请选择省","valid":"省选择错误"})
        self.city_id=IntegerField(widget=Widget.Select(attributes={"id":"my_city"},choices=[{"value":0,"text":"请选择市"}]),custom_error_dict={"required":"请选择市","valid":"市选择错误"})
        self.country_id=IntegerField(widget=Widget.Select(attributes={"id":"my_country"},choices=[{"value":0,"text":"请选择县(区)"}]),custom_error_dict={"required":"请选择县(区)","valid":"县(区)选择错误"})
        super(MerchantForm,self).__init__()


