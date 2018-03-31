# -*- coding: utf-8 -*-
import scrapy
import time
from Tanzhou.items import TanzhouItem

class TanzhouSpider(scrapy.Spider):
    name = 'tanzhou'
    offset = 0
    base_url = "http://www.tanzhouedu.com/mall/course/initAllCourse?params.offset=" + str(offset) + "&params.num=20&keyword=&_=" + str(int(time.time() * 1000))
    allowed_domains = ['tanzhouedu.com']
    start_urls = [base_url]

    def parse(self, response):
        items = TanzhouItem()
        node_list = response.xpath('//div[@id="newCourse"]/div/div/ul/li')
        for node in node_list:
            items['title'] = node.xpath('./a/@title').extract_first()
            items['money'] = node.xpath('./div/span/text()').extract_first()
            yield items
        self.offset += 20
        if node_list == []:
            return
        yield scrapy.Request(url="http://www.tanzhouedu.com/mall/course/initAllCourse?params.offset="+ str(self.offset)+\
                            "&params.num=20&keyword=&_=" + str(int(time.time()*1000)), callback=self.parse)
