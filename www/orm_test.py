#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-18
# Author: LXD

import orm
import asyncio
from user import User

async def connectDB(loop):
    username = 'root'
    password = 'root'
    dbname = 'pydb'
    await orm.create_pool(loop, user=username, password=password, db=dbname)

async def destroyDB():
    await orm.destroy_pool()

async def test_save(loop, id, name):
    await connectDB(loop)
    user = await User.find(id)
    if user is None:
        user = User(id=id, name=name)
        await user.save()
    await destroyDB()

async def test_findAll(loop):
    await connectDB()
    userlist = await User.findAll(orderBy="name", limit=2)
    print('all user: %s' % userlist)
    await destroyDB()

loop = asyncio.get_event_loop()

loop.run_until_complete(test_save(loop, '1', 'linxiaodan'))
loop.run_until_complete(test_save(loop, '2', 'lerrety'))
loop.run_until_complete(test_findAll(loop))