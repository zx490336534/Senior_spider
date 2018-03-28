#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from common.util import get_13_time
import urllib3
urllib3.disable_warnings()

__author__ = 'Terry'

def get_img(queryWord, pages=1):
    url = 'https://image.baidu.com/search/acjson'
    page_num = 30
    params = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': queryWord,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'word': queryWord,
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'pn': '0',  # 从第多少个图片开始
        'rn': page_num,  # 获取图片数据的条数，这2个值，相当于mysql数据库中的  limit pn, rn
        'gsm': '1e',
        get_13_time(): '',
    }

    data_list = []

    for i in range(pages):
        params['pn'] = page_num * i
        r = requests.get(url, params=params, verify=False)
        json_text = r.json()
        data = json_text['data']
        data_list.extend(data)
        # append   提交元素， [[data1],[data2]]
        # extent  才是扩展list

    return data_list