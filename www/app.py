#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-17
# Author: LXD

import logging
logging.basicConfig(level=logging.INFO)

import asyncio
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(init(loop))
loop.run_forever()