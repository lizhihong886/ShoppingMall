#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Model.User import IUserRepository,VipModel,UserTypeModel,UserModel
from Repository.DbConnection import DbConnection


#实现业务接口
class UserRepository(IUserRepository):
    def __init__(self):
        self.db_conn=DbConnection()
    def fetch_one_by_user_pwd(self,user,pwd):
        cursor=self.db_conn.connect()
        sql="""select nid ,username,email,last_login,vip,user_type from UserInfo WHERE username=%s AND pwd=%s"""
        cursor.execute(sql,(user,pwd))
        db_result=cursor.fetchone()
        self.db_conn.close()
        if db_result:
            obj=UserModel(
                nid=db_result['nid'],
                username=db_result['username'],
                email=db_result["email"],
                last_login=["last_login"],
                vip_obj=VipModel(db_result["vip"]),
                user_type_obj=UserTypeModel(db_result['"user_type'])
            )
            return obj

    def fetch_one_by_email_pwd(self,email,pwd):
        cursor = self.db_conn.connect()
        sql = """select nid ,username,email,last_login,vip,user_type from UserInfo WHERE email=%s AND pwd=%s"""
        cursor.execute(sql, (email, pwd))
        db_result = cursor.fetchone()
        self.db_conn.close()
        if db_result:
            obj = UserModel(
                nid=db_result['nid'],
                username=db_result['username'],
                email=db_result["email"],
                last_login=["last_login"],
                vip_obj=VipModel(db_result["vip"]),
                user_type_obj=UserTypeModel(db_result['"user_type'])
            )
            return obj
    def get_user_to_select(self):
        cursor=self.db_conn.connect()
        sql="""select nid as value,username as text from userinfo"""
        cursor.execute(sql)
        db_result=cursor.fetchall()
        self.db_conn.close()
        return db_result


            #实现sql语句