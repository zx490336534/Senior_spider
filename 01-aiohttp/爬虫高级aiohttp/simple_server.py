#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app, host='127.0.0.1', port=8080)