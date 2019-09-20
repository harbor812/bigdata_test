# -*- coding: utf-8 -*-


import re,json
import requests
import time,datetime
import db_redis
from gevent import monkey;monkey.patch_all()#会把python标准库当中一些阻塞操作变成非阻塞

import gevent


def test_requests(url,data,method,key,date):
    is_sucess=1
    ct=''
    if method == 'post' or method == 'POST':
        response = requests.post(url,data=data)
        content = response.text
#        print(content)
#        result = re.search(r'"access_token":"(.+?)"', content)
#        print("access_token:",result.group(1))
    elif method == 'get' or method == 'GET':
        response = requests.get(url,params=data)
#        print response.text
        content = response.text
#        print key
#        print content
#        print "=============================="
        dict1 = json.loads(content,strict=False)
        list1=dict1['resultList']
        list_len=len(list1)
#        print list_len
        if list_len == 0:
            print "返回结果为空"
            return False
            
        else:
            for i in range(list_len):
#                print "=============================="
#                print "开始匹配"
#                print list1[i]['content']
#                print i,list_len
                content1=list1[i]['content'].encode("utf-8")
                sendtime=list1[i]['sendTime']
                ct='%s//%s'%(ct,content1)
    #            key=key.encode("utf-8")  
                
    #            print type(key),type(content1)
                if content1 == key:
                    sendtime=list1[i]['sendTime']
#                    print "成功"
#                    print key + "---成功，sendTime：" + str(sendtime) + "---请求中的startTime："+ str(date) + "---匹配时间："+ str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    is_sucess=1
                    return 1
                    break
#                    print "=============================="
    #                print content
                else:
                    is_sucess=0

        if is_sucess==0:
              print "=============================="
#              print ct
              print "#####"
              print '%s---失败，sendTime：%s---请求中的startTime：%s---匹配时间：%s' % (key,str(sendtime),str(date),str(datetime.datetime.now()))
              return 0
    else:
        print "null"
        return False

def douyu_danmu(dr,sucess,usucess):
    #    for i in range(1):
    while True:
        key=dr.pop('douyu_danmu')
        if key !=None:
            key=key.split(',')
        else:
            break
#        print key[0],key[1]
        date = datetime.datetime.now()+datetime.timedelta(seconds=-20)
#        startdate = int(time.mktime(date.timetuple()))
#        date=date.strftime('%Y-%m-%d %H:%M:%S')
        
#        print startdate,enddate
#        print key
        url = 'http://113.107.166.14:8085/getRoomContentInfo'
        data = {'platID': '2', 'roomID': '2311698', 'fromID': key[1],'startTime': '1559037623', 'endTime': '1559059200', 'page': '1', 'limit': '10700'}
        method = 'get'
        # method = 'post'
#        print data
        if key !=None:
            tt=test_requests(url,data,method,key[0],date)
            if tt==1:
                sucess=sucess+1
            if tt==0:
                usucess=usucess+1
    totle=int(sucess)+ int(usucess)
    print "斗鱼：%s,%s"%(sucess,totle)
    print  float(format(int(sucess)/int(totle)* 100,'.2f'))
    
def huya_danmu(dr,sucess,usucess):
    #    for i in range(1):
    while True:
        key=dr.pop('huya_danmu')
        if key !=None:
            key=key.split(',')
        else:
            break
#        print key[0],key[1]
        date = datetime.datetime.now()+datetime.timedelta(seconds=-20)
#        startdate = int(time.mktime(date.timetuple()))
#        date=date.strftime('%Y-%m-%d %H:%M:%S')
        
#        print startdate,enddate
#        print key
        url = 'http://113.107.166.14:8085/getRoomContentInfo'
        data = {'platID': '1', 'roomID': '2311698', 'fromID': key[1],'startTime': '1559037623', 'endTime': '1559059200', 'page': '1', 'limit': '10700'}
        method = 'get'
        # method = 'post'
#        print data
        if key !=None:
            tt=test_requests(url,data,method,key[0],date)
            if tt==1:
                sucess=sucess+1
            if tt==0:
                usucess=usucess+1
    totle=int(sucess)+ int(usucess)
    print "虎牙：%s,%s"%(sucess,totle)
    print  float(format(int(sucess)/int(totle)* 100,'.2f'))



if __name__=='__main__':

#    date1 = datetime.datetime.now()+datetime.timedelta(seconds=3600)
    
    startdate = datetime.datetime.now()
    dr=db_redis.dbredis()
    time.sleep(1)
    sucess,usucess =0,0
#    for i in range(1):
    gevent.joinall([gevent.spawn(douyu_danmu(dr,sucess,usucess)),gevent.spawn(huya_danmu(dr,sucess,usucess))])
    enddate = datetime.datetime.now()
    rtime=(enddate - startdate).seconds
    print "------结束时间-------------",enddate,"------------------------------------"
    print "------运行耗时-------------",rtime,"----------------------------------------"        
    
