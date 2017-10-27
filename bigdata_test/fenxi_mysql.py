# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:30:42 2017

@author: Brianzhu
"""

import MySQLdb as mdb

class dbmysql(object):
#    localhost='127.0.0.1'
#    user='root'
#    passwd='rp1qaz@WSX'
#    databases='test_bigdata'
    localhost='localhost'
    user='root'
    passwd='zwg123456'
    databases='test_bigdata'
    def fx_sel_bug(self,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_id,bug_status,sub_type from bug where date >='"+date+"'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def fx_sel_jenkins(self,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select commitcode,change_name,object_id,change_source,date from jenkins_source where date >='"+date+"'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close() 
    def fx_sel_bug_count(self,date,date1,sub_type):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from bug where date >='"+date+"' and date < '"+date1+"' and bug_status='完成' and sub_type = '"+sub_type+"'"
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
#res=dbmysql().bug_sel_bugid("1","2017-09-13","接口")
#if res != ():
#    print res
#res=dbmysql().fx_sel_jenkins("2017-09-13")
#if res != ():
#    print res

