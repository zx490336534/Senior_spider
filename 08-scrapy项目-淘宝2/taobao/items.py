# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:

    # 价格、收货人数、商品名、商铺名、发货地址、详情链接，useri_id, nid
    user_id = scrapy.Field()
    nid = scrapy.Field()

    nick = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    loc = scrapy.Field()
    sales = scrapy.Field()
    detail_url = scrapy.Field()

    # 需要把地址分开为2个字段存储
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 市
