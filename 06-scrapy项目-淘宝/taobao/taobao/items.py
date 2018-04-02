# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    '''
    价格:view_price
    收货人数:view_sales
    商品名:raw_title
    店铺名:nick
    发货地址:item_loc
    详情链接：detail_url
    '''
    price = scrapy.Field()
    sales = scrapy.Field()
    title = scrapy.Field()
    nick = scrapy.Field()
    loc = scrapy.Field()
    detail_url = scrapy.Field()
