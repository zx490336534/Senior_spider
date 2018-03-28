#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import os

import aiohttp
import time

import urllib3

from h1.baidu_img.baidu_img_url import get_img

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
    print('aiohttp方式下载 %s 张图片 ，耗时： %s 秒' % (len(img_list), end-start))


if __name__ == '__main__':
    img_list = get_img('python', 10)
    print(len(img_list))

    file_path = os.path.join(os.getcwd(), 'img2/')
    download_img_aiohttp(img_list, file_path)

    '''
        aiohttp方式下载 93 张图片 ，耗时： 0.8583126068115234 秒
        
        aiohttp方式下载 310 张图片 ，耗时： 1.9394474029541016 秒
    '''




