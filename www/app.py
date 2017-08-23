#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-17
# Author: LXD

# import logging
#
# import asyncio
# from aiohttp import web
#
# logging.basicConfig(level=logging.INFO)
#
#
# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
#
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv
#
# # 获取EventLoop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(init(loop))
# loop.run_forever()

from tornado import web, ioloop
import os
import logging
logging.basicConfig(level=logging.INFO)


class MainHandler(web.RequestHandler):
    def get(self):
        # self.write('hello')
        self.render(
            "index.html",
            users=[]
        )


def make_app():
    return web.Application(
        handlers=[
            (r"/", MainHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static')
    )


def main():
    app = make_app()
    app.listen(8080)
    logging.info('Application is listening at 8080')
    ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()