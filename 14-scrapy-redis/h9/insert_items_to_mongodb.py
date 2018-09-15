#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

__author__ = 'Terry'

import redis
import pymongo

def insert_to_mongo():
    # 创建一个 redis 连接
    r = redis.Redis(host='localhost', port=6379)

    # 创建一个mongodb的连接
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['dd']
    coll = db['dingdian']

    # 死循环进行数据导入
    while True:
        # 从 redis 数据库中获取数据，并且在redis中删除
        source, data = r.blpop(['dingdian:items'])
        # 将 json 字符串 反序列化为 dict
        item = json.loads(data)
        # 将 dict 对象写入到mongodb中
        coll.insert_one(item)
        print('insert mongodb :', item)

if __name__ == '__main__':
    insert_to_mongo()