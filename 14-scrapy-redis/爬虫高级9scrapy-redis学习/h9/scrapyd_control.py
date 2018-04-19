#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import requests


ip = 'localhost'
port = 6800

def schedule(project, spider):
    url = f'http://{ip}:{port}/schedule.json'
    # url = 'http://{}:{}/schedule.json'.format(project, spider)
    params = {
        "project": project,
        "spider": spider
        # '_version': version
    }
    # 一定切记，尽管是post请求，不能使用 json=params，
    # 这里提交的参数，可以使用 params=params 或 data=params 中！！！！！！！！！
    r = requests.post(url, data=params)

    return r.json()

def listjobs(project):
    url = f'http://{ip}:{port}/listjobs.json?project={project}'
    r = requests.get(url)
    return r.json()

def cancel(project, job):
    url = f'http://{ip}:{port}/cancel.json?project={project}&job={job}'
    r = requests.post(url)
    return r.json()

if __name__ == '__main__':
    # 部署命令： python scrapyd-deploy 127 -p taobao --version v108
    project = 'dingdian'

    # 启动项目
    # schedule(project, 'dingdian')
    # #
    # # # 获取所有jobs
    # j = listjobs(project)
    # print(j)

    # 停止项目
    job = '9c8b182e418311e897d258fb8457c654'
    j = cancel(project, job)
    print(j)