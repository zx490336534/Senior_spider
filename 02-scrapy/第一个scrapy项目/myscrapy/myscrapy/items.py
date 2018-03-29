# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Product(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    age = scrapy.Field()
    sex = scrapy.Field()


class Person(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    age = scrapy.Field()
    sex = scrapy.Field()


person = Person()