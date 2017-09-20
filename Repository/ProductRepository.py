#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Repository.DbConnection import DbConnection
from  Model.Product import IProductRepository
class ProductRepository(IProductRepository):
    def __init__(self):
        self.db_conn=DbConnection()
    def fetch_count_by_merchant(self,merchant_id):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from product WHERE merchant_id=%s"""
        effect_rows=cursor.execute(sql,(merchant_id,))
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result["count"]
    def get_page_by_merchant_id(self,merchant_id,start,rows):
        cursor = self.db_conn.connect()
        sql = """select product.nid as nid,title,img,category_id from product where merchant_id=%s order BY nid DESC limit %s offset %s"""
        effect_row=cursor.execute(sql,(merchant_id,rows,start))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def get_product_by_id(self,product_id):
        cursor=self.db_conn.connect()
        sql="""select nid,title,img,category_id from product WHERE nid=%s"""
        cursor.execute(sql,(product_id,))
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result
    def create_product(self,product_dict,detail_list,img_list):
        """
        创建商品
        :param product_dict:商品字典 
        :param detail_list: [{'key': xx, 'value': 'xxx'}]
        :param img_list:  [{'src': 'fa'},{'src': 'fa'}]
        :return: 
        """
        product_sql="""insert into product(%s) value(%s)"""
        p_k_list=[]
        p_v_list=[]
        for k in product_dict.keys():
            p_k_list.append(k)
            p_v_list.append("%%(%s)s"%k)
        product_sql=product_sql%(",".join(p_k_list),",".join(p_v_list))
        cursor=self.db_conn.connect()
        cursor.execute(product_sql,product_dict)
        product_id=cursor.lastrowid
        if detail_list:
            d=map(lambda x:x.update(product_id=product_id),detail_list)
            list(d)
            detail_sql="""insert into product_detail(%s)VALUES (%s)"""
            d_k_list=[]
            d_v_list=[]
            for k in detail_list[0].keys():
                d_k_list.append(k)
                d_v_list.append("%%(%s)s"%k)
            detail_sql=detail_sql%(",".join(d_k_list),",".join(d_v_list),)
            cursor.executemany(detail_sql,detail_list)
        if img_list:
            i=map(lambda x:x.update(product_id=product_id),img_list)
            img_sql="""insert into product_img(%s) VALUES (%s)"""
            i_k_list=[]
            i_v_list=[]
            for k in img_list[0].keys():
                i_k_list.append(k)
                i_v_list.append("%%(%s)s"%k)
            img_sql=img_sql%(",".join(i_k_list),",".join(i_v_list))
            print(img_sql,img_list)
            cursor.executemany(img_sql,img_list)
            self.db_conn.close()
    def get_price_by_product_id(self,merchant_id,product_id):
        cursor=self.db_conn.connect()
        sql="""select price.nid as nid,
        standard,
        price,
        selling_price,
        product_id
        from price
        left JOIN product 
        on price.product_id=product.nid
        WHERE product.merchant_id=%s
        and product_id=%s
        order BY nid desc"""
        cursor.execute(sql,(merchant_id,product_id))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def fetch_detail_list(self,product_id):
        cursor=self.db_conn.connect()
        sql="""select name,value from product_detail WHERE product_detail.product_id=%s"""
        cursor.execute(sql,(product_id,))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def create_price(self,price_dict):
        price_sql="""insert into price(%s)VALUE (%s)"""
        p_k_list=[]
        p_v_list=[]
        for k in price_dict.keys():
            p_k_list.append(k)
            p_v_list.append("%%(%s)s"%k)
        price_sql=price_sql%(",".join(p_k_list),",".join(p_v_list))
        cursor=self.db_conn.connect()
        cursor.execute(price_sql,price_dict)
        self.db_conn.close()
    def update_price(self,nid,price_dict):
        sql="""update price set %s WHERE nid=%s"""
        value_list=[]
        for k,v in price_dict.items():
            value_list.append("%s=%%(%s)s"%(k,k))
        sql=sql%(','.join(value_list),(nid,))
        cursor=self.db_conn.connect()
        cursor.execute(sql,price_dict)
        self.db_conn.close()
    def get_upv(self,merchant_id,product_id):
        pass
    def create_puv(self,product_id,ip):
        pass
    def fetch_index_product(self):
        pass
    def fetch_product_detail(self,product_id,price_id):
        pass