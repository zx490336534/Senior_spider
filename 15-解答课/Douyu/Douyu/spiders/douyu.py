# -*- coding:utf-8 -*-

import scrapy
from Douyu.items import DouyuItem
import json

class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]

    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0

    start_urls = [base_url + str(offset)]


    def parse(self, response):
        # 将响应的json字符串转为Python的数据类型，并取出data键的数据
        node_list = json.loads(response.body)["data"]

        # 当列表为空，if条件不成立
        if not node_list:
            return


        for node in node_list:
            item = DouyuItem()

            item['image_link'] = node['vertical_src']
            item['nick_name'] = node['nickname']
            item['room_id'] = node['room_id']
            item['city'] = node['anchor_city']
            item['online'] = node['online']


            yield item

        self.offset += 20
        yield scrapy.Request(url = self.base_url + str(self.offset), callback = self.parse)




