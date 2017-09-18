# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:50:28 2017

@author: Administrator
"""
import MySQLdb as mdb


def save(objectname,date,change,name,commitcode):
    conn = mdb.connect('localhost','root','zwg123456','test_bigdata')
    cursor=conn.cursor()          #定义连接对象
    sql = "INSERT into jenkins_source (objectname,change_name,change_source,date,commitcode)VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql,(objectname,name,change,date,commitcode))
    conn.commit()
    cursor.close()
    conn.close()
    




