# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:29:07 2017

@author: Administrator
"""

#import datetime
#from db_mysql import save
import MySQLdb as mdb

import http.client

def save(objectname,date,change,name,commitcode):
#    print objectname
#    print date
#    print change
    print (name)
#    print commitcode
    conn = mdb.connect('localhost','root','zwg123456','test_bigdata')
    cursor=conn.cursor()          #定义连接对象
    sql = "INSERT into jenkins_source(objectname,change_name,change_source,date,commitcode) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql,(objectname,name,change,date,commitcode))
    conn.commit()
    cursor.close()
    conn.close()   

dict1={"file:/ts/inke.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/zhanqi.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/main.ts":["add:var roomInfo = new comm.RoomInfo();","add:let roomUrl","del:let roomUrl","add:roomInfo.room_url = roomUrl","add:result = roomInfo","del:console.log(roomUrl);","add:roomInfo.room_url = roomUrl","add:result = roomInfo","add:roomInfo.room_url = roomUrl","add:result = roomInfo"],"file:/ts/douyu.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl;","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl;"],"file:/ts/wangyicc.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/chushou.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"commentID":["d4755ff006769475923302b3d9223ffea5242aff"],"file:/ts/qqgame.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/longzhu.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/huya.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/yizhibo.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"time":["2017-09-18 17:16:08"],"file:/ts/yy.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"objectID":["1"],"file:/ts/huomao.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/bilibili.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:l","add:roomInfo.room_url = roomUrl"],"file:/ts/huajiao.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/zhangyu.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/panda.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/shihou.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/quanmin.ts":["del:var roomInfo: undefined | comm.RoomInfo = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/momo.ts":["del:var roomInfo : comm.RoomInfo | undefined = undefined","add:var roomInfo : comm.RoomInfo　=　new comm.RoomInfo()","del:roomInfo　=　new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"]}
print type(dict1)
dic=list(dict1.keys())
i=int(len(dict1))
j=0
t=0
change=[]
name=[]
date=""

if "objectID" in dict1.keys():
    objectid= dict1["objectID"] 
#    print objectid
if "commentID" in dict1.keys():
    commitcode= dict1["commentID"]
#    print commitcode
if "time" in dict1.keys():
    date= dict1["time"]
for j in range(i):
    if dic[j]!="time" and dic[j]!="objectID" and dic[j]!="commentID":
        change.append(dict1[dic[j]])
        name.append(dic[j])
        change1=str(change[t])
#        print name[t]
        save(objectid,date[0],change1,name[t],commitcode[0])
        t=t+1

# 发送post请求 获取json数据
def httpConnection_Post_Json(url,url_path,data_dict):
    try:
        conn = http.client.HTTPConnection(url,timeout=15)
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "application/json"}
        payload = urllib.parse.urlencode(data_dict)
        url_path = 'http://' + url + url_path
        conn.request("POST", url_path, payload, headers)
        res = conn.getresponse()
        data = res.read()
        ret = data.decode("utf-8")
        return ret
    except Exception as e:
        payload = urllib.parse.urlencode(data_dict)
        log.e('httpConnection_Post:'+url+url_path+payload)
        return None
        

