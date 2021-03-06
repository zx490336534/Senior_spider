#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
# loop.run_until_complete(print_sum(1, 2))
loop.run_until_complete(asyncio.gather(*[print_sum(i, i+1) for i in range(100)]))
loop.close()
