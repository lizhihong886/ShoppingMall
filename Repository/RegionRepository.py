#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Model.Region import IProvinceRepository,ICityRepository,ICountryRepository
from Repository.DbConnection import DbConnection
class ProvinceRepository(IProvinceRepository):
    def __init__(self):
        self.db_conn=DbConnection()
    def fetch_province_count(self):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from Province"""
        cursor.execute(sql)
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result["count"]
    def fetch_province(self):
        cursor=self.db_conn.connect()
        sql="""select nid,caption from province"""
        effect_rows=cursor.execute(sql)
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def fetch_province_by_page(self,start,rows):
        cursor=self.db_conn.connect()
        sql="""select nid,caption from province order by nid desc limit %s offset %s"""
        cursor.execute(sql,(rows,start))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result

    def add_province(self,caption):
        cursor=self.db_conn.connect()
        sql="""insert into Province (caption) VALUES (%s)"""
        effect_rows=cursor.execute(sql,(caption,))
        self.db_conn.close()
        return effect_rows

    def delete_province(self,nid):
        cursor=self.db_conn.connect()
        sql="""delete from Province WHERE nid=%s"""
        effect_rows=cursor.execute(sql,(nid,))
        self.db_conn.close()
        return effect_rows

    def update_province(self,nid,caption):
        cursor=self.db_conn.connect()
        sql="""update Province set caption=%s where nid=%s"""
        effect_rows=cursor.execute(sql,(caption,nid))
        self.db_conn.close()
        return effect_rows

    def is_exist(self,caption):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from Province WHERE caption=%s"""
        cursor.execute(sql,(caption,))
        db_result=cursor.fetchone()
        ret=db_result['count']
        self.db_conn.close()
        return ret

class CityRepository(ICityRepository):
    def __init__(self):
        self.db_conn=DbConnection()
    def fetch_city(self):
        cursor=self.db_conn.connect()
        sql="""SELECT city.nid,
                      city.caption,
                      city.province_id, 
                      province.caption as province 
                      FROM city 
                      LEFT JOIN province 
                      on city.province_id=province.nid"""
        effect_rows=cursor.execute(sql)
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def fetch_city_by_province(self,province_id):
        cursor=self.db_conn.connect()
        sql="""SELECT nid,caption from city WHERE province_id=%s"""
        effect_rows=cursor.execute(sql,(province_id,))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_city_count(self):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from city"""
        effect_rows=cursor.execute(sql)
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result['count']
    def fetch_city_by_page(self,start,rows):
        cursor=self.db_conn.connect()
        sql = """select city.nid,
                              city.caption,
                              city.province_id,
                              province.caption as province 
                              FROM city 
                              LEFT JOIN province 
                              on city.province_id=province.nid
                              ORDER BY city.nid desc 
                              LIMIT %s OFFSET %s """
        effect_rows=cursor.execute(sql,(rows,start))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def add_city(self,caption,province_id):
        cursor=self.db_conn.connect()
        print(caption,province_id)
        sql="""insert into city (caption,province_id) VALUES (%s,%s)"""
        effect_rows=cursor.execute(sql,(caption,province_id))
        self.db_conn.close()
        return effect_rows

    def update_city(self,nid,caption,province_id):
        cursor=self.db_conn.connect()
        sql="""update city set caption=%s,province_id=%s WHERE nid=%s"""
        effect_rows=cursor.execute(sql,(caption,province_id,nid))
        self.db_conn.close()
        return effect_rows
    def delete_city(self,nid):
        cursor=self.db_conn.connect()
        sql="delete from city WHERE nid=%s"
        effect_rows=cursor.execute(sql,(nid,))
        self.db_conn.close()
        return effect_rows

    def is_exist(self,caption,province_id):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from city WHERE caption=%s AND province_id=%s"""
        cursor.execute(sql,(caption,province_id))
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result["count"]

class CountryRepository(ICountryRepository):
    def __init__(self):
        self.db_conn=DbConnection()
    def fetch_country_count(self):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from country"""
        cursor.execute(sql)
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result["count"]
    def fetch_country_by_page(self,start,rows):
        cursor=self.db_conn.connect()
        sql="""SELECT country.nid,
                country.caption,
                country.city_id,
                city.caption as city,
                city.province_id as province_id,
                province.caption as province 
                FROM country 
                LEFT JOIN city 
                ON country.city_id=city.nid 
                LEFT JOIN province 
                ON city.province_id=province.nid 
                ORDER BY country.nid DESC limit %s offset %s"""
        cursor.execute(sql,(rows,start))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def fetch_country_by_city(self, city_id):
        cursor=self.db_conn.connect()
        sql="""select nid,caption from country WHERE city_id=%s"""
        cursor.execute(sql,(city_id,))
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result
    def add_country(self,caption,city_id):
        cursor=self.db_conn.connect()
        sql="""insert into country (caption,city_id) VALUES (%s,%s)"""
        effect_rows=cursor.execute(sql,(caption,city_id))
        self.db_conn.close()
        return effect_rows
    def update_country(self,nid,caption,city_id):
        cursor=self.db_conn.connect()
        sql="""update country set caption=%s,city_id=%s WHERE nid=%s"""
        effect_rows=cursor.execute(sql,(caption,city_id,nid))
        self.db_conn.close()
        return effect_rows
    def delete_country(self,nid):
        cursor=self.db_conn.connect()
        sql="""delete from country WHERE nid=%s"""
        effect_rows=cursor.execute(sql,(nid,))
        self.db_conn.close()
        return effect_rows

    def is_exist(self,caption,city_id):
        cursor=self.db_conn.connect()
        sql="""select count(1) as count from country WHERE caption=%s and city_id=%s"""
        cursor.execute(sql,(caption,city_id))
        db_result=cursor.fetchone()
        self.db_conn.close()
        return db_result["count"]
