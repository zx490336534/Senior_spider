# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import os
import json
import pymongo

from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE

class ImageSource(object):
    def process_item(self, item, spider):
        item['source'] = spider.name
        return item


class DouyuImagesPipeline(ImagesPipeline):

    # 发送图片链接的请求
    def get_media_requests(self, item, info):
        # 获取item数据的图片链接
        image_link = item['image_link']
        # 发送图片的请求，响应会保存在settings里IMAGES_STORE指定的路径下
        yield scrapy.Request(url = image_link)


    def item_completed(self, results, item, info):
        # 每个results表示一个图片的信息，取出这个图片的原本路径
        image_path = [x['path'] for ok, x in results if ok]

        # 先保存当前图片的路径
        old_name = IMAGES_STORE + image_path[0]

        # 新建的当前图片的路径
        new_name = IMAGES_STORE + item['nick_name'] + ".jpg"

        item['image_path'] = new_name

        # 处理图片重复修改出错的问题
        try:
            # 将原本路径的图片名，修改为新建的图片名
            #/xxx/xxx/xxx.jpg    xxx/123/3212/xx.jpg

            # 如果图片名中间有 / 在保存时会做为目录结点了。
            #"Huawei Meta10 6G/128G xxx.jpg".replace("/", "")

            os.rename(old_name, new_name)
        except:
            print "[INFO]：图片已被修改..."

        return item

class DouyuJsonPipeline(object):
    def open_spider(self, spider):
        self.filename = open("douyu.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        self.filename.write(content)

        return item

    def close_spider(self, spider):
        self.filename.close()


class DouyuMongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host = "127.0.0.1", port = 27017)
        self.db = self.client['Douyu']
        self.collection = self.db['Images']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        return item


"""
results = [

(
    True,
    {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2017/11/14/1405317_20171114122109_big.jpg', 'path': 'full/43ccf64e78902d943cf5fc00b62ea93e1897e2fd.jpg', 'checksum': '84a68c5f4a7f4f237cbdcb9e1ca378f2'}
 )

]
        """
