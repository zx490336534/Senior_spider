# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymongo

class TencentPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient('127.0.0.1',27017)
        self.db = self.client['area']
        self.collection = self.db['area']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
