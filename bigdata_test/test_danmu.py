# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:24:03 2019

@author: Brianzhu
"""

import sys
import db_redis 

from danmu import DanMuClient

dr=db_redis.dbredis()

def pp(msg):
    print(msg.encode(sys.stdin.encoding, 'ignore').
        decode(sys.stdin.encoding))

dmc = DanMuClient('https://live.bilibili.com/21296161')
if not dmc.isValid(): print('Url not valid')

@dmc.danmu
def danmu_fn(msg):
    pp('[%s] %s' % (msg['NickName'], msg['Content']))
#    pp('%s' % (msg))
    mm=msg['Content']+','+msg[u'uid']
    dr.push('douyu_danmu',mm)

@dmc.gift
def gift_fn(msg):
    pp('[%s]  sent a gift!' % (msg['NickName']))

@dmc.other
def other_fn(msg):
    pp('Other message received')

dmc.start(blockThread = True)