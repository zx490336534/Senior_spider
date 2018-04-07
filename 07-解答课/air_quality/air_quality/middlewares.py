# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
from scrapy import signals
from selenium import webdriver
import time

class AirQualitySpiderMiddleware(object):
    @classmethod
    def process_request(self,request,spider):
        if request.url != 'https://www.aqistudy.cn/historydata/':
            if  'month=' in request.url:
                self.driver = webdriver.Chrome()
                self.driver.get(request.url)
                # self.driver.maximize_window()
                # self.driver.implicitly_wait(8)
                time.sleep(5)
                html = self.driver.page_source
                self.driver.quit()
                return scrapy.http.HtmlResponse(url=request.url,body=html.encode('utf-8'),encoding='utf-8',request=request)
            else:
                return
        else:
            return