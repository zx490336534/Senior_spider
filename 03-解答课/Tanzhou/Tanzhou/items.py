# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TanzhouItem(scrapy.Item):
    # 课程名称
    title = scrapy.Field()
    # 课程价格
    money = scrapy.Field()
