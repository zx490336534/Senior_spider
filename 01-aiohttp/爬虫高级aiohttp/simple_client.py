#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.baidu.com')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())