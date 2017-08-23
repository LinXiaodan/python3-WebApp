#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-23
# Author: LXD

import yaml
import os


def get_config():
    configs = yaml.load(open('../config.yml')) if os.path.exists('../config.yml') \
        else yaml.load(open('../config_default.yml'))
    return configs

if __name__ == '__main__':
    print(get_config())