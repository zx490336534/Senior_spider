# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirQualityItem(scrapy.Item):
    '''
    日期
    城市
    空气质量指数
    质量等级
    pm2.5
    pm10
    so2
    co
    no2
    o3
    '''
    date = scrapy.Field()
    city = scrapy.Field()
    aqi = scrapy.Field()
    leave = scrapy.Field()
    pm2_5 = scrapy.Field()
    pm10 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o3 = scrapy.Field()
