# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 13:40:51 2018

@author: Brianzhu
"""

#import redis
#
#r = redis.redis(host='113.107.166.5',post=6379,db=0)
#r.set('foo', 'bar')
#
#r.get('foo')


#
#print redis


##
import redis
import json
import db_mysql
import logging
import basic_data
import datetime

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

def pop_redis():
    task=""
    pool = redis.ConnectionPool(host='113.107.166.5', port=16379, db=0)    
    r=redis.Redis(connection_pool=pool)
    try:
    #r.hset("test1", "k1", "v1")
    #
    #
    #print r.hget('test1',"k1")
    
    #r.lpush("test2","123","456","678","000")
    
    #task = r.brpop('test2')  
    #print 'pro1 get task:' + task[1];
    
        while True:
            task = r.blpop('ceshi')
#            print task
            dict1 = json.loads(task[1],strict=False)
    #            print dict1
            dic=list(dict1.keys())
         #           logging.info(dic) 
            i=int(len(dict1))
        #        return json.dumps(dict1[dic[i-1]])     ##数组 
        #            
        #        return json.dumps(dict1["file:/ts/inke.ts"])
            j=0
            t=0
            change=[]
            name=[]
            date=""
            db=db_mysql.dbmysql()
            if "objectID" in dict1.keys():
                objectid= dict1["objectID"] 
            if "commentID" in dict1.keys():
                commitcode= dict1["commentID"] 
            if "time" in dict1.keys():
                date= dict1["time"]
            for j in range(i):
                if dic[j]!="time" and dic[j]!="objectID" and dic[j]!="commentID":
                    change.append(dict1[dic[j]])
                    name.append(dic[j])
                    #print date,change[t],name[t]
                    change1=str(change[t])
                    name1=str(name[t])
        #                    print objectid,date[0],change1,name1,commitcode
                    db.save(objectid,date[0],change1,name1,commitcode)
        #                    print "#################"
        #                    print objectid[0],name[t]
                    changename_level_cn=db.changename_level_sel(objectid,name1)
        #                    print "changename_level_cn",int(changename_level_cn[0])
                    if int(changename_level_cn[0]) > 0:
                       objectid1=basic_data.basic_project1(objectid[0])
                       message="近90天bug严重的程序-子项目名称："+objectid1+"-程序名："+name1+"- 有更新"
                       logging.info(message)
                    t=t+1
    except :
        logging.error("error message")         

if __name__ == '__main__':
   starttime=datetime.datetime.now()
   print "---pop_redis---开始时间--------------",starttime,"---------------------------------"
   pop_redis()
