#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.spiders import Rule

from sr_test.items import SrTestItem

__author__ = 'Terry'

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
class DingdianSpider(RedisCrawlSpider):

    name = 'dingdian'

    # start_urls = ['http://www.23us.so/']

    rules = (
        Rule(LinkExtractor(allow='/list/\d+_\d+.html'), follow=True),
        Rule(LinkExtractor(allow='/xiaoshuo/\d+.html'), callback='parse_item')
    )

    def parse_item(self, response):
        auth = response.xpath('//*[@id="at"]/tr[1]/td[2]/text()').extract_first()
        last_update_time = response.xpath('//*[@id="at"]/tr[2]/td[3]/text()').extract_first()
        url = response.url

        item = SrTestItem()
        item['auth'] = auth
        item['last_update_time'] = last_update_time
        item['url'] = url

        return item