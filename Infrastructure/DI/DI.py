#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
#依赖注入（Dependency Injection）又称控制反转（Inversion of Control）主要用来实现不同模块或类之间的解耦，可以根据需要动态地把某种依赖关系注入到对象中，使得模块的设计更加独立
# 依赖注入(自动去传参)
class Mapper():
    #在字典里定义依赖注入关系
    __mapper_relation={}

    #类直接调用注册关系
    @staticmethod
    def register(cls,value):
        Mapper.__mapper_relation[cls]=value
    @staticmethod
    def exist(cls):
        if cls in Mapper.__mapper_relation:
            return True
        return False
    @staticmethod
    def value(cls):
        return Mapper.__mapper_relation[cls]

class MetaClass(type):
    def __call__(self, *args, **kwargs):
        obj=self.__new__(self,*args,**kwargs) #创建对象
        arg_list=list(args)
        if Mapper.exist(self):
            value=Mapper.value(self)
            arg_list.append(value)
        obj.__init__(*arg_list,**kwargs) #初始化
        return obj