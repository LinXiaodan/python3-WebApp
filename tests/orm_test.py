#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-18
# Author: LXD

import logging
logging.basicConfig(level=logging.INFO)
from www import orm
import asyncio
from www.orm import Model, StringField, IntegerField


class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)     # id为主键
    name = StringField()                    # name为stirng类型


async def connectDB(loop):
    username = 'root'
    password = 'root'
    dbname = 'pydb'
    await orm.create_pool(loop, user=username, password=password, db=dbname)

async def destroyDB():
    await orm.destroy_pool()

async def test_find(loop):
    await connectDB(loop)
    user = await User.find('123')
    print('user: %s' % user)
    await destroyDB()

async def test_findAll(loop):
    await connectDB(loop)
    userlist = await User.findAll(orderBy="name", limit=100)
    print('all user: %s' % userlist)
    await destroyDB()

async def test_findNumber(loop):
    await connectDB(loop)
    id = await User.findNumber('id')
    name = await User.findNumber('name')
    print('id: %s; name: %s' % (id, name))
    await destroyDB()

async def test_save(loop, id, name):
    await connectDB(loop)
    user = await User.find(id)
    if user is None:
        # 创建实例
        user = User(id=id, name=name)
        # 存入数据库
        await user.save()
    else:
        logging.info('id {} is found in the table'.format(id))
    await destroyDB()

async def test_update(loop):
    await connectDB(loop)
    user = await User.find('123')
    if user is not None:
        user.name = 'update'
        await user.update()
        print('user update: %s' % user)
    await destroyDB()

async def test_remove(loop, id):
    await connectDB(loop)
    user = User(id=id)
    rows = await user.remove()
    await destroyDB()

loop = asyncio.get_event_loop()

loop.run_until_complete(test_save(loop, 2, 'linxiaodan'))

loop.run_until_complete(test_findAll(loop))

loop.run_until_complete(test_remove(loop, 1))

loop.run_until_complete(test_findAll(loop))

loop.run_until_complete(test_findNumber(loop))

loop.run_until_complete(test_find(loop))

loop.run_until_complete(test_update(loop))

loop.close()