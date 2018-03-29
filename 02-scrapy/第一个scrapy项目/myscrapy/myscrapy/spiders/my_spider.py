#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy

__author__ = 'Terry'

class QuotesSpider(scrapy.Spider):
    # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    name = "quotes"
    # start_urls= [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]

    def start_requests(self):
        # 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。
        # 后续的URL则从初始的URL获取到的数据中提取。
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            # 必须使用 yield
            # Request 是 scrapy 自定义的类
            # callback， 获取到response 之后的 回调函数
            yield scrapy.Request(url=url, callback=self.parse)

    # 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)




class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    # 允许访问的域名，可以不写
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)