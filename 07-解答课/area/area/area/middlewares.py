# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import scrapy
from scrapy import signals
from selenium import webdriver
import time

class AreaSpiderMiddleware(object):
    def process_request(self,request,spider):
        self.driver = webdriver.Chrome()
        if request.url != "https://www.aqistudy.cn/historydata/":
            self.driver.get(request.url)
            time.sleep(1.5)
            html = self.driver.page_source
            self.driver.quit()
            return scrapy.http.HtmlResponse(url=request.url,body=html.encode("utf-8"),
                                            encoding="utf-8",request=request)
