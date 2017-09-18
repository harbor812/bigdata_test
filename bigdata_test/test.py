# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 15:29:07 2017

@author: Administrator
"""

#import datetime
#from db_mysql import save
import MySQLdb as mdb

def save(objectname,date,change,name):
    print objectname
    print date
    print change
    print name
    conn = mdb.connect('localhost','root','123456','zwgtest')
    cursor=conn.cursor()          #定义连接对象
    sql = "INSERT into jenkins_source VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,(objectname,change,date,name))
    conn.commit()
    cursor.close()
    conn.close()   

dict1={"file:/ts/inke.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/zhanqi.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/main.ts":["add:var roomInfo = new comm.RoomInfo();","add:let roomUrl","del:let roomUrl","add:roomInfo.room_url = roomUrl","add:result = roomInfo","del:console.log(roomUrl);","add:roomInfo.room_url = roomUrl","add:result = roomInfo","add:roomInfo.room_url = roomUrl","add:result = roomInfo"],"file:/ts/douyu.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl;","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl;"],"file:/ts/wangyicc.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/chushou.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/qqgame.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/longzhu.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/huya.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/yizhibo.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"time":["2017-09-12 13:46:51"],"file:/ts/yy.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/huomao.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/bilibili.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/huajiao.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/zhangyu.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/panda.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/shihou.ts":["del:var roomInfo: comm.RoomInfo | undefined = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/quanmin.ts":["del:var roomInfo: undefined | comm.RoomInfo = undefined","add:var roomInfo: comm.RoomInfo = new comm.RoomInfo()","del:roomInfo = new comm.RoomInfo()","add:roomInfo.room_url = roomUrl","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"],"file:/ts/momo.ts":["del:var roomInfo : comm.RoomInfo | undefined = undefined","add:var roomInfo : comm.RoomInfo　=　new comm.RoomInfo()","del:roomInfo　=　new comm.RoomInfo()","del:roomInfo = undefined","add:roomInfo.room_url = roomUrl"]}
#print dict1
dic=list(dict1.keys())
i=int(len(dict1))
j=0
t=0
change=[]
name=[]
date=""

if "time" in dict1.keys():
    date= dict1["time"]
for j in range(i):
    if dic[j]!="time":
        change.append(dict1[dic[j]])
        name.append(dic[j])
        change1=str(change[t])
        save("test",date[0],change1,name[t])
        t=t+1
        

