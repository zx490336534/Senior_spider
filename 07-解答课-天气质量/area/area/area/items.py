# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AreaItem(scrapy.Item):
    # 日期
    date = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 空气质量指数
    aqi = scrapy.Field()
    # 空气质量等级
    level = scrapy.Field()
    # pm2.5
    pm2_5 = scrapy.Field()
    # pm10
    pm10 = scrapy.Field()
    # so2
    so2 = scrapy.Field()
    # co
    co = scrapy.Field()
    # no2
    no2 = scrapy.Field()
    # o3
    o3 = scrapy.Field()
