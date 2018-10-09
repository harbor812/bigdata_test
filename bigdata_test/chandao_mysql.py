# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:06:01 2018

@author: Brianzhu
"""

import MySQLdb as mdb

class zd_dbmysql(object):
#    localhost='127.0.0.1'
#    user='root'
#    passwd='rp1qaz@WSX'
#    databases='test_bigdata'
    localhost='192.168.120.120'
    user='qa'
    passwd='kyEg9psMQ3pG'
    databases='zentao'
    def bug_sel(self,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select id,title,status,assignedDate,resolvedBy,openedBy,closedBy,openedDate,resolvedDate,closedDate from zt_bug where assignedDate >='"+date+"'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()