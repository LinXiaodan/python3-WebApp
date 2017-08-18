#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-18
# Author: LXD

from orm import Model, StringField, IntegerField


class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)     # id为主键
    name = StringField()                    # name为stirng类型