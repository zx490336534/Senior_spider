# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    positionInfo = scrapy.Field()
    peopleNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()
    duty = scrapy.Field()
    Requirement = scrapy.Field()
    detail_url = scrapy.Field()

class PositionItem(scrapy.Item):
    position_zhize = scrapy.Field()
    position_yaoqiu = scrapy.Field()

