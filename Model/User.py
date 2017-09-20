
#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
class UserTypeModel:
    USER_TYPE = (
        {"nid": 1, 'caption': "用户"},
        {"nid": 2, "caption": "商户"},
        {"nid": 3, 'caption': "管理员"},
    )

    def __init__(self, vip_id):
        self.nid = vip_id
    @property
    def caption(self):
        for item in UserTypeModel.USER_TYPE:
            if item['nid'] == self.nid:
                return item['caption']

class VipModel:
    VIP_TYPE = (
        {"nid": 1, "caption": "铜牌"},
        {"nid": 2, "caption": "银牌"},
        {"nid": 3, "caption": "金牌"},
        {"nid": 4, "caption": "铂金"},
    )
    def __init__(self,vip_id):
        self.nid=vip_id

    @property
    def caption(self):
        for item in VipModel.VIP_TYPE:
            if item['nid']==self.nid:
                return item['caption']

#模型
class UserModel:
    def __init__(self,nid ,username,email,last_login,vip_obj,user_type_obj):
        self.nid=nid
        self.username=username
        self.email=email
        self.last_login=last_login
        self.vip_obj=vip_obj
        self.user_type_obj=user_type_obj


#接口
class IUserRepository:
    def fetch_one_by_user_pwd(self,user,pwd):
        """
        根据用户名和密码获取对象
        :param user: 
        :param pwd: 
        :return: 
        """
        raise Exception("NotImplementedException")
    def fetch_one_by_email_pwd(self,email,pwd):
        """
        根据邮箱密码获取对象
        :param email: 
        :param pwd: 
        :return: 
        """
        raise Exception("NotImplementedException")

    def get_user_to_select(self):
        """获取用户"""
        raise Exception("NotImplementedException")

from Infrastructure.DI.DI import MetaClass

#协调者
class UserService(metaclass=MetaClass): #依赖注入
    def __init__(self,user_repository):
        """
        :param user_repository: 数据仓库对象
        """
        self.userRepository=user_repository

    def check_login(self,user,email,pwd):
       if user:
           m=self.userRepository.fetch_one_by_user_pwd(user,pwd)
       else:
           m=self.userRepository.fetch_one_by_email_pwd(email,pwd)
       return m
    def get_user_to_select(self):
        db_result=self.userRepository.get_user_to_select()
        return db_result


