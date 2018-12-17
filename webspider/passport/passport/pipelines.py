# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
import redis


class passportPipeline(object):
####json 存储    
#    def __init__(self):
#        self.filename = open("passport.json", "w")
#
#    def process_item(self, item, spider):
#        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
#        self.filename.write(text.encode("utf-8"))
#        return item
#
#    def close_spider(self, spider):
#        self.filename.close()
###mysql 存储    
     def __init__(self):
          dbargs = dict(
             host = 'localhost',
             db = 'test_bigdata',
             user = 'root', #replace with you user name
             passwd = 'zwg123456', # replace with you password
             charset = 'utf8',
             cursorclass = MySQLdb.cursors.DictCursor,
             use_unicode = True,
             )    
          self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)
         
     def process_item(self, item,spider):
              res = self.dbpool.runInteraction(self.insert_into_table,item)
              res.addCallback(self.handle_error)
#              return item
     ###for url in df['url'].get_values():  # 把每一条的值写入key的字段
     def insert_into_table(self,conn,item):
                conn.execute('insert into passport_spider(name,sex,passwd,newpasswd) values (%s,%s,%s,%s)',(item['leir'],item['leir2'],item['passwd'],item['newpasswd']))
#                 conn.execute('insert into passport_spider(name,sex) values (%s,%s)',(item['leir'],item['leir2']))
#                 conn.execute('insert into passport_spider(passwd,newpasswd) values (%s,%s)',(item['passwd'],item['newpasswd']))

#                 conn.commit()
     def handle_error(self,failure):
         if failure:
            print failure# 打印错误信息
###redis 存储
#    def __init__(self):
#        pool = redis.ConnectionPool(host='113.107.166.5', port=16379, db=1)    
#        self.r=redis.Redis(connection_pool=pool)
#    def process_item(self,item):
#        self.r.lpush("passport",item['leir'])
        
        
        
        
        
        
        
        
        