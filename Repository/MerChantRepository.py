#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Model.Merchant import IMerchantRepository
from Repository.DbConnection import DbConnection

class MerchantRepository(IMerchantRepository):
    def __init__(self):
        self.db_conn=DbConnection()
    def fetch_merchant_count(self):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from merchant"""
        cursor.execute(sql)
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result["count"]
    def fetch_merchant_by_page(self,start,rows):
        cursor=self.db_conn.connect()
        sql="""select nid,name,domain from merchant ORDER BY nid DESC limit %s offset %s"""
        cursor.execute(sql,(rows,start))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def fetch_merchant_detail_by_nid(self,nid):
        cursor=self.db_conn.connect()
        sql="""select 
                 merchant.nid as nid,
                 domain,
                 business_mobile,
                 qq,
                 backend_mobile,
                 country_id,
				 country.caption as country_caption,
                 user_id,
				 userinfo.username as user_name,
                 name,
                 business_phone,
                 backend_phone,
                 address
                from
                merchant
                LEFT JOIN userinfo ON 
                merchant.user_id=userinfo.nid
                LEFT JOIN country ON 
                merchant.country_id=country.nid
                WHERE merchant.nid=%s"""
        cursor.execute(sql,nid)
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result

    def add_merchant(self,**kwargs):
        cursor=self.db_conn.connect()
        sql="""insert into merchant(%s) values(%s)"""
        key_list=[]
        value_list=[]
        for k,v in kwargs.items():
            key_list.append(k)
            value_list.append("%%(%s)s"%k)
        sql=sql%(','.join(key_list),",".join(value_list))
        effect_rows=cursor.execute(sql,kwargs)
        self.db_conn.close()
        return effect_rows


    def update_merchant(self,nid,**kwargs):
        cursor=self.db_conn.connect()
        sql="""update merchant set %s WHERE 
nid=%s"""
        value_list=[]
        print(kwargs)
        for k,v in kwargs.items():
            value_list.append("%s=%%(%s)s"%(k,k))
        sql=sql%(",".join(value_list),nid)
        effect_rows=cursor.execute(sql,kwargs)
        self.db_conn.close()
        return effect_rows
    def delete_merchant(self, nid):
        cursor=self.db_conn.connect()
        sql="""delete from merchant  where nid=%s"""
        effect_row=cursor.execute(sql,(nid,))
        self.db_conn.close()
        print(effect_row)
        return effect_row


