# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:30:41 2019

@author: Brianzhu
"""

import gevent
from gevent.queue import Queue
from gevent import monkey; monkey.patch_all()
 
def func():
     i=0
     for i in range(10):
 
         print("int the func")
         t='test:%s'%(i)
#         print t
         q.put(t)
         gevent.sleep(0.5)
 
def func2():
     for i in range(10):
         print("int the func2")
         res = q.get()
         print("--->",res)
 
q = Queue()
gevent.joinall(
     [
         gevent.spawn(func2),
         gevent.spawn(func),
     ]
 )