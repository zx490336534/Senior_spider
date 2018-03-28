#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import time

import urllib3

from h1.baidu_img.baidu_img_url import get_img
from concurrent import futures

urllib3.disable_warnings()

__author__ = 'Terry'



def down_img_thread(url, file_path, i):
    r = requests.get(url, verify=False)
    content = r.content
    file = file_path + str(i + 1) + '.jpg'
    with open(file, 'wb') as f:
        f.write(content)

def download_img_thread(img_list, file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    start = time.time()
    # 多线程
    with futures.ThreadPoolExecutor(max_workers=10) as exec:
        # for d in img_list:
        # 枚举，可以得到list的 下标 和 值
        for i, d in enumerate(img_list):
            # dict的get方法， 第一个参数是 key， 第二个参数是 默认值 ，没有找到前面的key，则返回这个值
            url = d.get('thumbURL', '')
            if url:
                # submit， 第一个参数是多线程执行的函数，后面的参数才是 这个执行函数的参数
                exec.submit(down_img_thread, url, file_path, i)

    end = time.time()
    print('thread方式下载 %s 张图片 ，耗时： %s 秒' % (len(img_list), end-start))


if __name__ == '__main__':
    img_list = get_img('python', 10)
    print(len(img_list))

    file_path = os.path.join(os.getcwd(), 'img3/')
    download_img_thread(img_list, file_path)

    '''
        thread方式下载 31 张图片 ，耗时： 0.22487807273864746 秒
        thread方式下载 310 张图片 ，耗时： 2.262303113937378 秒
    '''


