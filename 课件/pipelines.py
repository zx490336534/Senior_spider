# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
import redis
from datetime import datetime
from scrapy.exporters import CsvItemExporter
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class AreaPipeline(object):
    def process_item(self, item, spider):
        item['source'] = spider.name
        item['utc_time'] = str(datetime.utcnow())
        return item


class AreaJsonPipeline(object):
    def open_spider(self, spider):
        self.filename = open("area.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.filename.write(content)
        return item

    def close_spider(self, spider):
        self.filename.close()

class AreaMongoPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient("127.0.0.1",27017)
        self.db = self.client['areas']
        self.collection = self.db['area']

    def process_item(self,item,spider):
        self.collection.insert(dict(item))
        return item

class AreaRedisPipeline(object):
    def open_spider(self,spider):
        self.client = redis.Redis(host="127.0.0.1",port=6379)

    def process_item(self,item,spider):
        content = json.dumps(dict(item))
        self.client.lpush("AREA_ITEM",content)
        return item

class AreaCsvPipeline(object):
    def open_spider(self,spider):
        self.file = open("aqi.csv", "w")
        # 创建一个csv文件读写对象，参数是需要保存数据的csv文件对象
        self.csv_exporter = CsvItemExporter(self.file)
        # 表示开始进行数据写入
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表示结束数据写入
        self.csv_exporter.finish_exporting()
        self.file.close()