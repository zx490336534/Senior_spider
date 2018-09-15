# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']


    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(url=url,formdata={'email':'15168230644','password':'zx660644'},callback=self.parse)

    def parse(self, response):
        print(response.body.decode())
        name = response.xpath('//a[@class="hd-name"]/text()').extract_first()
        with open('Renren.txt','w') as f:
            f.write(name)
        # print(response.body.decode())
