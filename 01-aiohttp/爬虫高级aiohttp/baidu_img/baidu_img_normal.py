#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
import time

import urllib3

from h1.baidu_img.baidu_img_url import get_img

urllib3.disable_warnings()

__author__ = 'Terry'


def download_img_normal(img_list, file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    start = time.time()
    # for d in img_list:
    # 枚举，可以得到list的 下标 和 值
    for i, d in enumerate(img_list):
        # dict的get方法， 第一个参数是 key， 第二个参数是 默认值 ，没有找到前面的key，则返回这个值
        url = d.get('thumbURL', '')
        if url:
            r = requests.get(url, verify=False)
            file = file_path + str(i+1) + '.jpg'
            with open(file, 'wb') as f:
                f.write(r.content)

    end = time.time()
    print('普通方式下载 %s 张图片 ，耗时： %s 秒' % (len(img_list), end-start))


if __name__ == '__main__':
    img_list = get_img('python', 10)
    print(len(img_list))

    file_path = os.path.join(os.getcwd(), 'img1/')
    download_img_normal(img_list, file_path)

    '''
        普通方式下载 93 张图片 ，耗时： 3.5958898067474365 秒
        
        普通方式下载 310 张图片 ，耗时： 13.790303468704224 秒
    '''


