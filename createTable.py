#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column,Integer,String,UniqueConstraint,Index,VARCHAR,ForeignKey,DateTime,CHAR,TEXT,Date,BIGINT,DECIMAL
from sqlalchemy.orm import sessionmaker ,relationship


engine=create_engine('mysql+pymysql://root:a741258963@localhost:3306/shoppingdb?charset=utf8',echo=True,max_overflow=5, encoding='utf-8')
#如果有中文需加上charset=utf8
#echo=True 执行时输出由类创表时翻译成的sql语句,
#max_overflow 表示最大连接数
Base=declarative_base() #生成一个SQLORM基类


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

drop_db()
init_db()