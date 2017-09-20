#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
# class BaseForm:
#
#     def __init__(self):
#         self._value_dict = {}
#         self._error_dict = {}
#         self._valid_status = True
#         self.initialize()
#
#     def initialize(self):
#         for field_name, field_obj in self.__dict__.items():
#             print(self.__dict__.items())
#             print(field_name,field_obj)
#             if field_name.startswith('_'):
#                 continue
#             field_obj.name = field_name
#             print(field_obj.name)
#             print(field_name)
#
# class UserForm(BaseForm):
#     def __init__(self,nid,username,pwd):
#         self.nid=nid
#         self.username=username
#         self.pwd=pwd
#         super(UserForm,self).__init__()
#
# person=UserForm(nid=1,username="alex",pwd=123456)
def test3(func,**kwargs ):
    print( kwargs)#集合成字典的形式
    print( *kwargs)#all the keys
    print( kwargs['age'])
    func(**kwargs)




# def test4(**kwargs):
#     print("text4")
#     print(kwargs)
#
# test3(test4,name='Mike',age='22',sex='male')
# # test3(**{'name':'Jack','age':30,'sex':'male'})

detail_list=[{'name': 'ad', 'value': '123'},{"name":"ak"}]
add={"province_id":1}
li=[]
for i in detail_list:
    i.update(add)
    li.append(i)
print(li)