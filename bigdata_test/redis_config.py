# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 15:03:57 2018

@author: Brianzhu
"""

import configparser


config=configparser.ConfigParser()
config.read("redis_config.ini")


ip=config.get("test","IP")
port=config.get("test","port")


print ip,port