#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

__author__ = 'Terry'

import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(random.random())
    return x + y


async def print_sum(x, y, sem):
    # 这里控制并发的任务数
    async with sem:
        result = await compute(x, y)
        print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
# 控制并发数
sem = asyncio.Semaphore(5)
loop.run_until_complete(asyncio.gather(*[print_sum(i, i + 1, sem) for i in range(100)]))
loop.close()


# 疑问，为什么每次都是5个一组