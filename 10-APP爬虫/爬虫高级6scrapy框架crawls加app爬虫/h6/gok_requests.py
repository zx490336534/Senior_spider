#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Terry'

import requests

# 标准的构造我们的 requests 的session
s = requests.session()
s.trust_env = False
s.verify = False
s.headers = {
    'Accept-Charset': 'UTF-8;',
    'Accept-Encoding': 'gzip,deflate',
    'Content-type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.1; MI 6 MIUI/V9.2.4.0.NCACNEK)',
    # 'Host': 'gamehelper.gm825.com', # 这个 一定要删除，这里注释掉提示大家一定记得删除 Host
    'Connection': 'Keep-Alive'
}

url = 'http://gamehelper.gm825.com/wzry/hero/ranking?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.2.0.1&version_code=12201&cuid=559649C74CA93E75A8D328E0797678F7&ovr=7.1.1&device=Xiaomi_MI+6&net_type=1&client_id=c1uYGXluwjTh5e2NCXy9Jg%3D%3D&info_ms=%2BsDuon4TQ%2FohxVyJ5XgvZw%3D%3D&info_ma=Ax7x%2F%2BHQLCEI2EuUAo%2BgPpmL1vfhOApBdv3jflaCrwI%3D&mno=0&info_la=5kkYPqJY%2F%2BojZKFRdmp0sw%3D%3D&info_ci=5kkYPqJY%2F%2BojZKFRdmp0sw%3D%3D&mcc=0&clientversion=12.2.0.1&bssid=BDwn9VpvWlGlejslbWyGoWQ9BwkR29ifXKDZoaS8v8I%3D&os_level=25&os_id=ba2a10c82341ade3&resolution=1080_1920&dpi=480&pdunid=aa4184'
# 这个 get 参数不需要处理，直接原样提交就好
# params = {
#     'channel_id': '90009a',
#     'app_id': 'h9044j',
#     'game_id': '7622',
#     'game_name': '王者荣耀',
#     'vcode': '12.2.0.1',
#     'version_code': '12201',
#     'cuid': '559649C74CA93E75A8D328E0797678F7',
#     'ovr': '7.1.1',
#     'device': 'Xiaomi_MI 6',
#     'net_type': '1',
#     'client_id': 'c1uYGXluwjTh5e2NCXy9Jg==',
#     'info_ms': '+sDuon4TQ/ohxVyJ5XgvZw==',
#     'info_ma': 'Ax7x/+HQLCEI2EuUAo+gPpmL1vfhOApBdv3jflaCrwI=',
#     'mno': '0',
#     'info_la': '5kkYPqJY/+ojZKFRdmp0sw==',
#     'info_ci': '5kkYPqJY/+ojZKFRdmp0sw==',
#     'mcc': '0',
#     'clientversion': '12.2.0.1',
#     'bssid': 'BDwn9VpvWlGlejslbWyGoWQ9BwkR29ifXKDZoaS8v8I=',
#     'os_level': '25',
#     'os_id': 'ba2a10c82341ade3',
#     'resolution': '1080_1920',
#     'dpi': '480',
#     'pdunid': 'aa4184',
# }
r = s.get(url)
json_data = r.json()

ranking_list = json_data['ranking_list']
for i, ranking in enumerate(ranking_list):
    print('排名：', i+1, '英雄名：', ranking['name'])

    hero_id  = ranking['hero_id']
    url = 'http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.2.0.1&version_code=12201&cuid=559649C74CA93E75A8D328E0797678F7&ovr=7.1.1&device=Xiaomi_MI+6&net_type=1&client_id=c1uYGXluwjTh5e2NCXy9Jg%3D%3D&info_ms=%2BsDuon4TQ%2FohxVyJ5XgvZw%3D%3D&info_ma=Ax7x%2F%2BHQLCEI2EuUAo%2BgPpmL1vfhOApBdv3jflaCrwI%3D&mno=0&info_la=5kkYPqJY%2F%2BojZKFRdmp0sw%3D%3D&info_ci=5kkYPqJY%2F%2BojZKFRdmp0sw%3D%3D&mcc=0&clientversion=12.2.0.1&bssid=BDwn9VpvWlGlejslbWyGoWQ9BwkR29ifXKDZoaS8v8I%3D&os_level=25&os_id=ba2a10c82341ade3&resolution=1080_1920&dpi=480&client_ip=192.168.0.101&pdunid=aa4184'
    r = s.get(url.format(hero_id))

    json_data = r.json()
    # 铭文
    rec_inscriptions = json_data['info']['rec_inscriptions']
    print(rec_inscriptions)
    # 大神出装
    equip_choice = json_data['info']['equip_choice']
    print(equip_choice)


def save_mongdb():
    pass
