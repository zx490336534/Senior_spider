# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #vertical_src
    image_link =  scrapy.Field()
    #图片保存的文件路径
    image_path =  scrapy.Field()
    #nickname
    nick_name =  scrapy.Field()
    #room_id
    room_id =  scrapy.Field()
    #anchor_city
    city =  scrapy.Field()
    # online
    online =  scrapy.Field()

    # 数据源
    source = scrapy.Field()
