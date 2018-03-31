#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy import Request

from dingdian_scrapy.items import DingdianScrapyItem

__author__ = 'Terry'

class DingdianSpider(scrapy.Spider):

    name = 'dingdian'

    def start_requests(self):
        base_url = 'http://www.23us.so/list/%s_1.html'

        for i in range(1, 10):
            url = base_url % i
            yield Request(url, callback=self.parse)

    def parse(self, response):
        max_num = response.xpath('//a[@class="last"]/text()').extract_first()
        url = response.url
        url_pre = url[:-6]
        '''
        第一页是 http://www.23us.so/list/1_1.html
        第二页是 http://www.23us.so/list/1_2.html
        第180页是 http://www.23us.so/list/1_180.html
        得出结论：
        不同页码，就是在 1_%s.html 中，替换这个 %s 
        先通过 url[:-6]  取到 http://www.23us.so/list/1_
        然后在 这个 url 后面 拼接  %s.html 
        '''
        #  记得将  max_num  进行 int() 包裹
        # 翻页
        for i in range(1, int(max_num)+1):
            url = url_pre + str(i) + '.html'
            yield Request(url, callback=self.parse_page)

    def parse_page(self, response):
        # trs = response.xpath('//tr[@bgcolor="#FFFFFF"]')
        # for tr in trs:
        # response.xpath('//*[@id="content"]/dd[1]/table/tbody/tr[2]/td[1]/a')

        text = response.text
        soup = BeautifulSoup(text)
        trs = soup.find_all('tr', bgcolor='#FFFFFF')
        for tr in trs:
            url_a = tr.find('a')
            url = url_a['href']
            book_name = url_a.get_text()
            new_chapter = tr.find_all('a')[1].get_text()
            meta = {
                'book_name':book_name,
                'new_chapter':new_chapter
            }
            yield Request(url, callback=self.parse_detail, meta=meta)

    def parse_detail(self, response):
        soup = BeautifulSoup(response.text)
        table = soup.find('table')
        trs = table.find_all('tr')
        auth = trs[0].find_all('td')[1].get_text().replace('\xa0', '')  # \xa0 就是 html 中的 &nbsp;
        status = trs[0].find_all('td')[2].get_text().replace('\xa0', '')
        words = trs[1].find_all('td')[1].get_text().replace('\xa0', '')
        last_time = trs[1].find_all('td')[2].get_text().replace('\xa0', '')

        item = DingdianScrapyItem()
        item['book_name'] = response.meta['book_name']
        item['new_chapter'] = response.meta['new_chapter']
        item['auth'] = auth
        item['status'] = status
        item['words'] = words
        item['last_time'] = last_time

        return item

