# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:33:57 2019

@author: Brianzhu
"""

import redis
import configparser  #ini配置文件




class dbredis(object):
    #读取 redis 配置文件
    config=configparser.ConfigParser()
    config.read("redis_config.ini")
    
    env="test_get_php"
    ip=config.get(env,"IP")
    port=config.get(env,"port")
    key=config.get(env,"key")
    db=config.get(env,"db")
    pool = redis.ConnectionPool(host=ip, port=port, db=db)    
    r=redis.Redis(connection_pool=pool)
    #r.hset("test1", "k1", "v1")
    #
    #
    def push(self,key,detail):
        self.r.lpush(key,detail)
    def pop(self,key):
        return self.r.rpop(key)
            #r.lpush("test2","123","456","678","000")
            
            
            
if __name__ == '__main__':
    
    dbredis().push('test','1')
    