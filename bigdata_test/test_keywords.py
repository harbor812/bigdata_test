# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:39:35 2018

@author: Brianzhu
"""
import MySQLdb as mdb
import db_mysql

class dbmysql1(object):
    localhost='127.0.0.1'
    user='root'
    passwd='rp1qaz@WSX'
    databases='test_bigdata'
#    localhost='localhost'
#    user='root'
#    passwd='zwg123456'
#    databases='test_bigdata'

    def levelwords_selname(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select keyword from day_keywords"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
        


db=db_mysql.dbmysql()       
db1=dbmysql1()

kw1=db1.levelwords_selname()
kw1con=len(kw1)

for i in range(kw1con):  
    kw=kw1[i][0]
    kwcount=db.levelwords_count(kw)
    kwcount=kwcount[0]
    
    if kwcount ==0:
        db.levelwords_insert(kw,'1')