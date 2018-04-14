# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
from tenCent.items import TencentItem,PositionItem


class TencentPipeline(object):

    def open_spider(self,spider):
        self.client = pymongo.MongoClient('127.0.0.1',27017)
        self.db = self.client['tencent']
        self.collection = self.db['tencent']


    def process_item(self, item, spider):
        if isinstance(item,TencentItem):
            self.collection.insert(dict(item))
        return item


class PositionPipline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('127.0.0.1', 27017)
        self.db = self.client['tencent']
        self.collection = self.db['tencent']

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            self.collection.insert(dict(item))
        return item
