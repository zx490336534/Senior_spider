# -*- coding: utf-8 -*-
import json

import scrapy
from urllib import parse
from taobao.items import TaobaoItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    base_url = 'https://s.taobao.com/search?q=%s&sort=sale-desc&s=%s'
    #单独本spider的配置，区别于全局setting.py文件
    # custom_settings = {}


    def start_requests(self):
        key_words = self.settings['KEY_WORDS']
        key_words = parse.quote(key_words,' ').replace(' ','+')
        # s = parse.quote_plus(key_words)
        page_num = self.settings['PAGE_NUM']
        one_page_count = self.settings['ONE_PAGE_COUNT']
        for i in range(page_num):
            url = self.base_url % (key_words,i*one_page_count)
            yield scrapy.Request(url,callback=self.parse)


    def parse(self, response):
        p = 'g_page_config = ({.*?});'
        g_page_config = response.selector.re(p)[0]
        g_page_config = json.loads(g_page_config)
        auctions = g_page_config['mods']['itemlist']['data']['auctions']

        for auction in auctions:
            item = TaobaoItem()
            item['price'] = auction['view_price']
            item['sales'] = auction['view_sales']
            item['title'] = auction['raw_title']
            item['nick'] = auction['nick']
            item['loc'] = auction['item_loc']
            item['detail_url'] = auction['detail_url']

            yield item

