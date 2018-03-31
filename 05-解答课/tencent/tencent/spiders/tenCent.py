# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tenCent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        items = TencentItem()
        node_list = response.xpath('//*[@class="even"]|//*[//@class="odd"]')
        for node in node_list:
            items['name'] = node.xpath('./td[1]/a/text()').extract_first()
            items['positionInfo'] = node.xpath('./td[2]/text()').extract_first()
            items['peopleNumber'] = node.xpath('./td[3]/text()').extract_first()
            items['workLocation'] = node.xpath('./td[4]/text()').extract_first()
            items['publishTime'] = node.xpath('./td[5]/text()').extract_first()

