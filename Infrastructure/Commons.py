#!/usr/bin/env/ python
# -*-coding:utf-8 -*-
import hashlib
import time
import random

def random_code():
    code=""
    for i in range(4):
        current=random.randrange(0,4)
        if current!=i:
            temp=chr(random.randint(65,90))
        else:
            temp=random.randint(0,9)
        code+=str(temp)
    return code

def generate_md5(value):
    r=str(time.time())
    obj=hashlib.md5(r.encode("utf-8"))
    obj.update(value.encode("utf-8"))
    return obj.hexdigest()
