# items.py

# -*- coding: utf-8 -*-

import scrapy

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaItem(scrapy.Item):
    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    # subFilename = scrapy.Field()

    sonUrls = scrapy.Field()

    head = scrapy.Field()
    content = scrapy.Field()
