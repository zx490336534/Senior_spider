#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from json import JSONDecodeError
from urllib import parse

import scrapy
from scrapy.spiders import Rule

from taobao.items import TaobaoItem
from scrapy.linkextractor import LinkExtractor
__author__ = 'Terry'

class TaobaoSpider(scrapy.Spider):

    # 爬虫的名字，必须唯一
    name = 'taobao'

    base_url = 'https://s.taobao.com/search?q={}&ie=utf8&sort=sale-desc&p4ppushleft=%2C{}&s={}'

    # 单独本 spider 的配置项，区别与 全局的 settings.py 文件
    # custom_settings = {
    # }

    # 允许访问的 域名 的范围，在我们这里，我们只访问淘宝的商品页面，
    # 不是去爬取整个站点信息，不需要配置！！！
    # allow_domains = []

    # 入口方法
    def start_requests(self):
        key_words = self.settings['KEY_WORDS']
        key_words = parse.quote(key_words, safe=' ').replace(' ', '+')

        page_num = self.settings['PAGE_NUM']
        one_page_count = self.settings['ONE_PAGE_COUNT']

        for i in range(page_num):
            url = self.base_url.format(key_words, one_page_count, i*one_page_count)
            yield scrapy.Request(url, callback=self.parse)

    # 第一层解析 response 的 方法
    def parse(self, response):
        try:
            p = 'g_page_config = ({.*?});'
            # scrapy 支持的 selector， 支持re、xpath、css,
            # re 得到的是一个 list
            g_page_config = response.selector.re(p)[0]
            # 转化为dict
            g_page_config = json.loads(g_page_config)
            # 获取到 数据的 字典
            auctions = g_page_config['mods']['itemlist']['data']['auctions']

            for auction in auctions:
                item = TaobaoItem()
                item['user_id'] = auction['user_id']
                item['nid'] = auction['nid']
                item['nick'] = auction['nick']
                item['title'] = auction['raw_title']
                item['price'] = auction['view_price']
                item['loc'] = auction['item_loc']
                item['sales'] = auction['view_sales']
                item['detail_url'] = auction['detail_url']

                # 不在 pipeline 中实现，就在sipder中实现，也是可以的
                # 不建议！！！！！！！
                # loc = item.pop('loc')
                # loc_l = loc.split(' ')
                # item['province'] = loc_l[0]
                # if len(loc_l) == 1:
                #     item['city'] = ''
                # else:
                #     item['city'] = loc_l[1]
                # 替换 sales 中的 人收货
                # item['sales'] = item['sales'].replace('人收货', '')


                # 必须使用 yield，不能使用return
                # 使用 return 获取到第一个 item，就直接返回了，后面的43个都不处理
                yield item
        except JSONDecodeError as e:
            # print(response.text)
            # print(response.url)
            # 一定要捕获特定错误，才能这样去写，不然会线程无限死循环！！！！
            yield scrapy.Request(response.url, callback=self.parse)
        except:
            # print(response.text)
            # 实际项目中，出现错误是要做相应的处理的！！最少也要输出日志
            print(response.url)


class DingdianSpider(scrapy.spiders.CrawlSpider):
    name = 'dingdian'

    start_urls = ['http://www.23us.so/']

    rules = (
        Rule(LinkExtractor(allow='/list/\d+_\d+.html'), follow=True),
        Rule(LinkExtractor(allow='/xiaoshuo/\d+.html'), callback='parse_item')
    )

    # 这个 默认 的 parse 函数 不能实现！！！
    # def parse(self):

    def parse_item(self, response):
        """ 处理 xiaoshuo 这个页面

        :param response:
        :return:
        """

        """
        # 在scrapy中会把 诸如 tbody, thead 等标签自动忽略掉。
        # 会导致在浏览器中copy的xpath匹配不到值，
        # 大家断点查看 response.txt 即可看到实际的数据中没有 tbody 这个标签了
        """
        # auth = response.xpath('//*[@id="at"]/tbody/tr[1]/td[2]/text()').extract_first()
        auth = response.xpath('//*[@id="at"]/tr[1]/td[2]/text()').extract_first()

        print(auth)
