# -*- coding: utf-8 -*-
import re
from lxml import etree

import scrapy
from air_quality.items import AirQualityItem

class AreaSpiderSpider(scrapy.Spider):
    name = 'area_spider'
    # allowed_domains = ['aqistudy.cn']
    base_url = 'https://www.aqistudy.cn/historydata/'
    start_urls = [base_url]

    def parse(self, response):
        print('正在爬取城市信息...')
        url_list = response.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a/@href').extract()
        city_list = response.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a/text()').extract()
        for url,city in zip(url_list,city_list):
            url = self.base_url + url
            yield scrapy.Request(url,meta={'city':city},callback=self.parse_month)

        # yield scrapy.Request(self.base_url + url_list, meta={'city': city_list}, callback=self.parse_month)

    def parse_month(self,response):
        print('正在爬取城市月份...')
        p = '<a href="daydata.php\?city=' + response.meta['city'] + '(.*?)">.*?</a></li>'
        html = str(response.text)
        url_list = re.findall(p,html,re.S|re.M)
        # print(url_list)
        for url in url_list:
            url = self.base_url + 'daydata.php?city=' + response.meta['city'] +url
            yield scrapy.Request(url,meta={'city':response.meta['city']},callback=self.parse_day)


    def parse_day(self,response):

        print('正在爬取最终数据')
        item = AirQualityItem()
        print('-' * 100)
        print(response.text)
        print('-' * 100)
        node_list = response.xpath('//tr')

        node_list.pop(0)
        for node in node_list:
            item['city'] = response.meta['city']
            item['date'] = node.xpath('./td[1]/text()').extract_first()
            item['aqi'] = node.xpath('./td[2]/text()').extract_first()
            item['leave'] = node.xpath('./td[3]/span/text()').extract_first()
            item['pm2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['pm10'] = node.xpath('./td[5]/text()').extract_first()
            item['so2'] = node.xpath('./td[6]/text()').extract_first()
            item['co'] = node.xpath('./td[7]/text()').extract_first()
            item['no2'] = node.xpath('./td[8]/text()').extract_first()
            item['o3'] = node.xpath('./td[9]/text()').extract_first()
            yield item

