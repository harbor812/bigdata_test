# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:50:28 2017

@author: Administrator
"""
import MySQLdb as mdb


def save(objectname,date,change,name):
    conn = mdb.connect('localhost','root','123456','zwgtest')
    cursor=conn.cursor()          #定义连接对象
    sql = "INSERT into jenkins_source VALUES (%s,%s,%s,%s)"
    cursor.execute(sql,(objectname,change,date,name))
    conn.commit()
    cursor.close()
    conn.close()
    




