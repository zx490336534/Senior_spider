# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from job.items import JobItem

'''
创建爬虫：
scrapy genspider -t crawl 51job "search.51job.com"
'''

class A51jobSpider(CrawlSpider):
    name = '51job'
    # allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?']
    show_one = LinkExtractor(allow=r'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,\d+.html.*')
    show_two = LinkExtractor(allow=r'https://jobs.51job.com/.*?/\d+.html?')
    rules = (
        Rule(show_one, callback='parse_one', follow=True),
        # Rule(show_two,callback='parse_detail',follow=False)
    )

    def parse_one(self, response):
        i = JobItem()
        name1_list = response.xpath('//div[@class="el"]/span/a/@title').extract()
        for name1 in name1_list:
            print(name1)

        return i
