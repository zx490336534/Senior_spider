#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import os

import aiohttp
import requests
import time

import urllib3

from h1.baidu_img.baidu_img_url import get_img
from concurrent import futures

urllib3.disable_warnings()

__author__ = 'Terry'




async def download_img_async(url, file_path, i):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            # clientsession 中 通过 read() 获取bytes ，等同 requests 中的 content
            content = await r.read()
            file = file_path + str(i + 1) + '.jpg'
            with open(file, 'wb') as f:
                f.write(content)

def download_img_aiohttp(img_list, file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    start = time.time()
    # for d in img_list:
    # 枚举，可以得到list的 下标 和 值
    tasks = []
    for i, d in enumerate(img_list):
        # dict的get方法， 第一个参数是 key， 第二个参数是 默认值 ，没有找到前面的key，则返回这个值
        url = d.get('thumbURL', '')
        if url:
            tasks.append(download_img_async(url, file_path, i))

    # 构造一个 时间循环器
    loop = asyncio.get_event_loop()
    # run_until_complete 执行loop中的所有任务
    # asyncio.gather 包裹 协程任务的list
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    end = time.time()

def process_handle(img_list, file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    start = time.time()
    # 多进程
    with futures.ProcessPoolExecutor(max_workers=4) as exec:
        # 没改造完成的，这里传入的 img_list 必须区分
        # 不能执行！！！！！！！！
        exec.submit(download_img_aiohttp, img_list, file_path)

    end = time.time()
    print('process+aiphttp方式下载 %s 张图片 ，耗时： %s 秒' % (len(img_list), end-start))


if __name__ == '__main__':
    img_list = get_img('python', 3)
    print(len(img_list))

    file_path = os.path.join(os.getcwd(), 'img5/')
    process_handle(img_list, file_path)

    '''
        process方式下载 93 张图片 ，耗时： 1.460862636566162 秒
        process方式下载 310 张图片 ，耗时： 2.976684331893921 秒
    '''


