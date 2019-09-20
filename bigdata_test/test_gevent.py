# -*- coding: utf-8 -*-
"""
Created on Wed May 29 19:36:10 2019

@author: Brianzhu
"""

from gevent import monkey;monkey.patch_all()#会把python标准库当中一些阻塞操作变成非阻塞

import gevent
def test1():
    i=0
    for i in range(10):
        print "test1:%s"%(i)
        gevent.sleep(2)#模拟爬虫请求阻塞
def test2():
    j=2
    for j in range(10):
        print "test2:%s"%(j)
        gevent.sleep(4)#模拟爬虫请求阻塞
gevent.joinall([gevent.spawn(test1),gevent.spawn(test2)])
