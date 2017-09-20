#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
from Infrastructure.DI.DI import Mapper
from Model.User import UserService
from Repository.UserRepository import UserRepository
from Model.Merchant import MerchantService
from Repository.MerChantRepository import MerchantRepository
from Model.Region import ProvinceService,CountryService,CityService
from Repository.RegionRepository import ProvinceRepository,CountryRepository,CityRepository

#依赖关系
Mapper.register(UserService,UserRepository())
Mapper.register(MerchantService,MerchantRepository())

Mapper.register(ProvinceService,ProvinceRepository())
Mapper.register(CityService,CityRepository())
Mapper.register(CountryService,CountryRepository())