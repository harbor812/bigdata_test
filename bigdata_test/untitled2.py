# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:48:12 2019

@author: Brianzhu
"""

import redis
import json
import db_mysql
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

def pop_redis(ip,port,key):
    task=""
    pool = redis.ConnectionPool(host=ip, port=port, db=5)    
    r=redis.Redis(connection_pool=pool)

    #r.hset("test1", "k1", "v1")
    #
    #
    #print r.hget('test1',"k1")
    
    #r.lpush("test2","123","456","678","000")
    
    #task = r.brpop('test2')  
    #print 'pro1 get task:' + task[1];
    
    while True:
        task = r.blpop(key)
        if task[1] == '100000000450':
            print task[1]
            break
#            dict1 = json.loads(task[1],strict=False)
         

if __name__ == '__main__':
   #读取 redis 配置文件
    config=configparser.ConfigParser()
    config.read("redis_config.ini")
    
    env="test"
    ip=config.get(env,"IP")
    port=config.get(env,"port")
    key=config.get(env,"key")
   #记录开始时间，开始读取redis数据
    starttime=datetime.datetime.now()
    print "---pop_redis---开始时间--------------",starttime,"---------------------------------"
    print ip,port,key
    pop_redis(ip,port,'author_201_20190603')