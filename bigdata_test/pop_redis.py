# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 13:40:51 2018

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
    pool = redis.ConnectionPool(host=ip, port=port, db=0)    
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
            task = r.blpop(key)
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
                       objectid1=db.object_name_sel(objectid[0])
                       objectid1=str(objectid1).decode("unicode-escape")
                       objectid1=objectid1.replace("(u'","").replace(",)","").replace("(","").replace("'","").encode('utf-8')
#                       print objectid1
                       date1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                       url="<a href=changename_analyze/"+ name1 +" target=\"_blank\">查看数据分析详细信息</a>"
                       message=date1+",近90天bug严重的程序-子项目名称："+objectid1+"-程序名："+name1+"- 有更新,"+url
                       logging.info(message)
                    t=t+1
    except :
        error_message=objectid + date[0]+ name1+ commitcode
        logging.error(error_message)         

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
    pop_redis(ip,port,key)
