#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-17
# Author: LXD

import asyncio
import logging
logging.basicConfig(level=logging.INFO)
import aiomysql


@asyncio.coroutine
def create_pool(loop, **kwargs):
    """
    连接池
    :param loop: 
    :param kwargs: 
    :return: 
    """
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kwargs.get('host', 'localhost'),
        port=kwargs.get('port', 3306),
        user=kwargs['user'],
        password=kwargs['password'],
        db=kwargs['db'],
        charset=kwargs.get('charset', 'utf8'),
        autocommit=kwargs.get('autocommit', True),
        maxsize=kwargs.get('maxsize', 10),
        minsize=kwargs.get('minsize', 1),
        loop=loop
    )