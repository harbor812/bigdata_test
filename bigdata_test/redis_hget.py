# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:44:57 2019

@author: Brianzhu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 13:40:51 2018

@author: Brianzhu
"""

import redis
import json
#import db_mysql
import logging
#import basic_data
import datetime
import configparser  #ini配置文件




logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapi.log',
                filemode='w')
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

#print dir(redis)

def hget_redis(ip,port,key):
    task=[]
    i=0
    pool = redis.ConnectionPool(host=ip, port=port, db=4)    
    r=redis.Redis(connection_pool=pool)
    pipe = r.pipeline()
    
    pipe.hkeys(key)
    task=list(pipe.execute())
    tk=task[0]
#    print len(tk)
#    for i in range(len(tk)):
    for i,tk_i in enumerate(tk):#zip()
#        print tk_i
        msg=json.loads(r.hget(key,tk_i),strict=False)
#        print msg
#        break
        print 'from_id:%s,room_id%s'%(msg["from_id"],msg["room_id"])

def hgetall_redis(ip,port,key):

    pool = redis.ConnectionPool(host=ip, port=port, db=4)    
    r=redis.Redis(connection_pool=pool)
    pipe = r.pipeline()
    
    pipe.hgetall(key)
    print pipe.execute()
    
def zadd_redis(ip,port,key):#　　在集合的基础上，为每元素排序，元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。
    pool = redis.ConnectionPool(host=ip, port=port, db=6)    
    r=redis.Redis(connection_pool=pool)
#    pipe = r.pipeline()
    
#    print r.zadd("testzwg1",one1=1,one2=2)
    print r.zadd("testzwg1","a1", 6, "a2", 2,"a3",5)
#    print pipe.execute()
  

if __name__ == '__main__':
   #读取 redis 配置文件
    config=configparser.ConfigParser()
    config.read("redis_config.ini")
    
    env="test1"
    ip=config.get(env,"IP")
    port=config.get(env,"port")
    key=config.get(env,"key")
   #记录开始时间，开始读取redis数据
    starttime=datetime.datetime.now()
    print "---pop_redis---开始时间--------------",starttime,"---------------------------------"
    print ip,port,key
#    hget_redis(ip,port,key)
    zadd_redis(ip,port,key)
#    hgetall_redis(ip,port,key)