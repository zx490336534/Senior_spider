#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from taobao.spiders.taobao import TaobaoSpider

__author__ = 'Terry'


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import sched

# 获取settings.py模块的设置
settings = get_project_settings()

def start_scrapy():
    process = CrawlerProcess(settings=settings)

    # 可以添加多个spider
    process.crawl(TaobaoSpider)

    # 启动爬虫，会阻塞，直到爬取完成
    process.start()

def get_start_time():
    # 启动时间，从settings中获取
    start_time = settings.get('START_TIME')
    if start_time:
        struct_time = settings['STRUCT_TIME']
        t = time.mktime(time.strptime(start_time, struct_time))
    else:
        t = time.time()

    return t


def sched_start():
    t = get_start_time()

    s = sched.scheduler()
    delay = t - time.time()
    # 定时启动任务
    # delay 是等待多少秒 , 值为 负数 时， 立刻启动
    # 1 是优先级，多个定时任务时起效
    # start_scrapy 就是定时启动的函数
    s.enter(delay, 1, start_scrapy)
    # 启动
    s.run()


def sleep_start():
    """
        通过 sleep 来定时启动
    :return:
    """
    t = get_start_time()

    delay = t - time.time()
    time.sleep(delay)
    start_scrapy()


if __name__ == '__main__':
    sched_start()

