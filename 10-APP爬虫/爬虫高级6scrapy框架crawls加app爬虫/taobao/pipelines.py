# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


# class TaobaoHandle2PipeLine(object):
#
#     def process_item(self, item, spider):
#         pass

class TaobaoHandlePipeline(object):
    def process_item(self, item, spider):
        # 将类似 '浙江 杭州' 的发货地址，分割成2个 地址：省会和城市，直辖市只有一个省，市=''
        loc = item.pop('loc')
        loc_l = loc.split(' ')
        item['province'] = loc_l[0]
        if len(loc_l) == 1:
            item['city'] = ''
        else:
            item['city'] = loc_l[1]

        # 替换 sales 中的 人收货
        item['sales'] = int(item['sales'].replace('人收货', ''))

        item['price'] = float(item['price'])

        return item



class TaobaoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
         #  必须在settings中 配置 MONGO_URI 和 MONGO_DATABASE
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        '''
            实例化 MongoClient
        :param spider:
        :return:
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        '''
            关闭 client
        :param spider:
        :return:
        '''
        self.client.close()

    def process_item(self, item, spider):
        '''
            将 item 插入到 数据库
        :param item:
        :param spider:
        :return:
        '''
        self.db['items'].insert_one(dict(item))
        return item
