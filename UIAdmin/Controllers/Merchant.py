#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import tornado.web
import json
from Model.Merchant import MerchantService
from UIAdmin.Forms.Merchant import MerchantForm
from pymysql import IntegrityError

class MerchantManagerHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render("Merchant/merchantManager.html")

class MerchantHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        req_type = self.get_argument('type', None)
        if req_type == 'pagination':
            ret = {'status': False, 'message': '', 'total': 0, 'rows': []}
            try:
                page = int(self.get_argument('page', 1))
                rows = int(self.get_argument('rows', 10))
                start = (page - 1) * rows
                service = MerchantService()
                ret['total']=service.fetch_merchant_count()
                ret['rows'] = service.fetch_merchant_by_page(start, rows)
                ret['status'] = True
            except Exception as e:
                ret['message'] = str(e)
            self.write(json.dumps(ret))
            return
        self.render('Merchant/merchantManager.html')

class MerchantEdit(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        error_summary=""
        merchant_id=self.get_argument("nid",None)
        if not merchant_id:
            crumbs="添加商户"
            form=MerchantForm()
            method="POST"
        else:
            crumbs="编辑商户"
            form=MerchantForm()
            #根据ID获取用户信息
            service=MerchantService()
            detail=service.fetch_merchant_detail_by_nid(merchant_id)

            country_caption=detail.pop("country_caption")
            country_id=detail.get("country_id")
            form.country_id.widget.choices.append({"value":country_id,"text":country_caption})
            method="put"
            form.init_value(detail)
        self.render("Merchant/merchantEdit.html",form=form,crumbs=crumbs,method=method,summary=error_summary,nid=merchant_id)

    def post(self, *args, **kwargs):
        """创建商户
        """
        method=self.get_argument("_method",None)
        if  method=="put":
            return self.put(self,*args,**kwargs)
        error_summary=""
        form=MerchantForm()
        try:
            is_valid=form.valid(self)
            print(form._value_dict)
            if is_valid:
                if form._value_dict["country_id"]=="0":
                    form._error_dict["country_id"]="请选择县区"
                else:
                    del form._value_dict["nid"]
                    del form._value_dict["city_id"]
                    del form._value_dict["province_id"]
                    # 添加到数据库
                    service=MerchantService()
                    service.add_merchant(**form._value_dict)
                    self.redirect("merchantManager.html")
                    return
            else:
                form.init_value(form._value_dict)
        except IntegrityError as e:
            error_summary="商户名称或登录用户必须唯一"
        except Exception as e:
            error_summary=str(e)
        self.render("Merchant/merchantEdit.html",form=form,crumbs="添加商户",method="post",summary=error_summary,nid=None)

    def put(self,*args,**kwargs):
        """修改商户"""
        error_summary=""
        form=MerchantForm()
        merchant_id=self.get_argument("nid",None)

        try:
            is_valid=form.valid(self)
            if is_valid:
                if form._value_dict["country_id"]=="0":
                    form._error_dict["country_id"]="请选择县(区)ID"
                else:
                    nid=form._value_dict.pop("nid")
                    del form._value_dict["city_id"]
                    del form._value_dict["province_id"]
                    # 添加到数据库
                    service=MerchantService()
                    db_result=service.update_merchant(nid,**form._value_dict)
                    print(db_result)
                    if db_result:
                        self.redirect("merchantManager.html")
                        return
                    else:
                        error_summary="更新失败"
            else:
                form.init_value(form._value_dict)
        except Exception as e:
            error_summary=str(e)
        service=MerchantService()
        detail=service.fetch_merchant_detail_by_nid(merchant_id)
        country_caption=detail.pop("country_caption")
        country_id=detail.get("country_id")
        form.country_id.widget.choices.append({
            "value":country_id,"text":country_caption
        })
        self.render("Merchant/merchantEdit.html",form=form,crumbs="编辑商户",method="put",summary=error_summary,nid=merchant_id)

    def delete(self, *args, **kwargs):
        ret={"message":"","status":False}
        nid=self.get_argument("nid",None)
        print(nid)
        if nid:
            try:
                service=MerchantService()
                db_result=service.delete_merchant(nid)
                if db_result:
                    ret["message"]="删除成功"
                    ret['status']=True
                else:
                    ret["message"]="删除失败"
            except Exception as e:
                ret["message"]=str(e)
        else:
            ret["message"]="请选择要删除的行"
        self.write(json.dumps(ret))



