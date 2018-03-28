#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import aiohttp
import asyncio


# 所有 协程 的函数 用 async
async def fetch(client):
    # 所有 协程 的上下文管理器 调用都使用  async with
    async with client.get('https://www.baidu.com') as resp:
        # 所有协程函数的调用 都使用 await
        return await resp.text()


async def main():
    # 构建一个用于访问http的 clientsession
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)


# 定义一个循环管理
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
