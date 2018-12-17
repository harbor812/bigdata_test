# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:54:18 2018

@author: Brianzhu
"""

import threading
import redis
import Queue
#redis链接
rpool = redis.ConnectionPool(host='192.168.120.132', port=6379,db=0)
rconn = redis.Redis(connection_pool=rpool)
q = Queue.Queue() #用来存放线程间共享的自增值
thread_num = 10 #线程数
#xqtoken写入
def set_redis_xq_token():
    while not q.empty():
        i = q.get()#获取队列里的一个元素
        token = "token_"+str(i)
        unionid = "unionid_"+str(i)
        rconn.set(token,str(i),ex=3600000)
        rconn.set(unionid,str(i),ex=3600000)
#mptoken写入
def set_redis_mp_token():
    while not q.empty():
        i = q.get()
        token = "token_mp_"+str(i)
        unionid = "unionid_mp_"+str(i)
        rconn.set(token,str(i))
        rconn.set(unionid,str(i))
if __name__=="__main__":
    threads = []
    for i in range(100001,200001):
        q.put_nowait(i)
    for t in range(thread_num):
        thread = threading.Thread(target=set_redis_mp_token) #线程建立并执行目标函数
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()