# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tenCent.items import TencentItem
from tenCent.items import PositionItem


class TencentCrawlSpider(CrawlSpider):
    name = 'tencent_crawl'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']
    page_lx = LinkExtractor(allow=(r'start=\d+'))
    position = LinkExtractor(allow=(r'position_detail\.php\?id=\d+'))

    rules = (
        Rule(page_lx, callback='parseContent', follow = True),
        Rule(position,callback='parse_position',follow = False)
    )

    def parseContent(self, response):
        items = TencentItem()
        node_list = response.xpath('//*[@class="even"]|//*[@class="odd"]')
        for node in node_list:
            items['name'] = node.xpath('./td[1]/a/text()').extract_first()
            items['positionInfo'] = node.xpath('./td[2]/text()').extract_first()
            items['peopleNumber'] = node.xpath('./td[3]/text()').extract_first()
            items['workLocation'] = node.xpath('./td[4]/text()').extract_first()
            items['publishTime'] = node.xpath('./td[5]/text()').extract_first()
            yield items

    def parse_position(self,response):
        item = PositionItem()
        item['position_zhize'] = ''.join(response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())
        item['position_yaoqiu'] = ''.join(response.xpath('//ul[@class="squareli"]')[1].xpath('./li/text()').extract())
        yield item





