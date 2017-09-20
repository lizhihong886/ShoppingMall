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

class Province(Base):
    """
    省
    """
    __tablename__="province"
    nid=Column(Integer,primary_key=True)
    caption=Column(VARCHAR(16),index=True)

class City(Base):
    """
    市
    """
    __tablename__="city"
    nid=Column(Integer,primary_key=True)
    caption=Column(VARCHAR(16),index=True)
    province_id=Column(Integer,ForeignKey("province.nid"))

class Country(Base):
    """
    县(区)
    """
    __tablename__="country"
    nid=Column(Integer,primary_key=True)
    caption=Column(VARCHAR(16),index=True)
    city_id=Column(Integer,ForeignKey("city.nid"))


class UserInfo(Base):
    """
    用户信息
    """

    __tablename__="userinfo"

    nid=Column(Integer,primary_key=True)

    USER_TYPE=(
        {"nid":1,'caption':"用户"},
        {"nid":2,"caption":"商户"},
        {"nid":3,'caption':"管理员"},
    )
    user_type=Column(Integer)

    VIP_TYPE=(
        {"nid":1,"caption":"铜牌"},
        {"nid":2,"caption":"银牌"},
        {"nid":3, "caption":"金牌"},
        {"nid":4, "caption":"铂金"},
    )
    vip=Column(Integer)

    username=Column(VARCHAR(32))
    password=Column(VARCHAR(64))
    email=Column(VARCHAR(64))

    last_login=Column(DateTime)
    ctime=Column(DateTime)

    __table_arys__=(
        Index("ix_user_pwd","username","password"),
        Index("ix_email_pwd","email","password")
    )

class Merchant(Base):
    """
    商户
    """
    __tablename__='merchant'
    nid=Column(Integer,primary_key=True)
    domain=Column(CHAR(8),unique=True)
    business_mobile=Column(CHAR(11))
    qq=Column(CHAR(16))
    backend_mobile=Column(CHAR(11))
    country_id=Column(Integer,ForeignKey("country.nid"))
    user_id=Column(Integer,ForeignKey("userinfo.nid"),unique=True)
    name=Column(VARCHAR(64),unique=True)
    business_phone=Column(VARCHAR(16))
    backend_phone=Column(VARCHAR(16))
    address=Column(VARCHAR(128))

class SubSite(Base):
    "分站"
    __tablename__="subsite"
    nid=Column(Integer,primary_key=True)
    caption=Column(VARCHAR(8),index=True)

class UperCategory(Base):
    """
    一级分类
    """
    __tablename__="upper_category"
    nid=Column(Integer,primary_key=True)
    caption=Column(VARCHAR(8),index=True)
    favor_id=Column(Integer,ForeignKey("subsite.nid"))

class Category(Base):
    """
    二级分类
    """
    __tablename__="category"
    nid=Column(Integer,primary_key=True)
    name=Column(VARCHAR(8),index=True)
    favor_id=Column(Integer,ForeignKey("upper_category.nid"))

class Product(Base):
    """产品"""
    __tablename__="product"
    nid=Column(Integer,primary_key=True)
    title=Column(VARCHAR(32),index=True)
    img=Column(VARCHAR(128))
    category_id=Column(Integer,ForeignKey("category.nid"))
    merchant_id=Column(Integer,ForeignKey("merchant.nid"))
    ctime=Column(DateTime)
    memo=Column(TEXT)
class ProvinceView(Base):
    """产品UV和PV访问记录"""
    __tablename__="product_view"
    nid=Column(Integer,primary_key=True)
    ip=Column(VARCHAR(32))
    product_id=Column(Integer,ForeignKey("product_id"))
    ctime=Column(Date,index=True)
    timespan=Column(BIGINT)

class ProductDetail(Base):
    """
    产品详细
    """
    __tablename__="product_detail"
    nid=Column(Integer,primary_key=True)
    title=Column(VARCHAR(16))
    content=Column(VARCHAR(32))
    product_id=Column(Integer,ForeignKey("product.nid"))

class ProductImg(Base):
    """产品图片"""
    __tablename__="product_img"
    nid=Column(Integer,primary_key=True)
    product_id=Column(Integer,ForeignKey("product.nid"))
    src=Column(VARCHAR(128))


class Price(Base):
    """产品价格"""
    __tablename__="price"
    nid=Column(Integer,primary_key=True)
    standard=Column(VARCHAR(32))
    price=Column(DECIMAL)
    selling_price=Column(DECIMAL)
    product_id=Column(Integer,ForeignKey("product.nid"))

class SuperProduct(Base):
    __tablename__="super_product"
    nid=Column(Integer,primary_key=True)
    price_id=Column(Integer,ForeignKey("price.nid"))
    super_choice=((1,"新品上市"),
                  (2,"精品推荐"))
    super_type=Column(Integer)



def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

# drop_db()
# init_db()