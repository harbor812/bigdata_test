# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:50:28 2017

@author: Administrator
"""
import MySQLdb as mdb

class dbmysql(object):
    localhost='localhost'
    user='root'
    passwd='zwg123456'
    databases='test_bigdata'
    def save(self,objectname,date,change,name,commitcode):
    #    conn = mdb.connect('localhost','root','zwg123456','test_bigdata')
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into jenkins_source (object_id,change_name,change_source,date,commitcode)VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(objectname,name,change,date,commitcode))
        conn.commit()
        cursor.close()
        conn.close()
    def bug_save(self,bug_id,bug_name,bug_status,date,complete_user,ttype,sub_type):
        if complete_user =="":
            complete_user="暂无"
    #    conn = mdb.connect('localhost','root','zwg123456','test_bigdata')
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into bug (bug_id,bug_name,bug_status,date,complete_user,type,sub_type)VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(bug_id,bug_name,bug_status,date,complete_user,ttype,sub_type))
        conn.commit()
        cursor.close()
        conn.close()
    def bug_sel(self,bug_id,bug_status):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from bug where bug_id=%s and bug_status=%s"
        cursor.execute(sql,(bug_id,bug_status))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def bug_sel_commitcode(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select DISTINCT commitcode,date,object_id from jenkins_source"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def bug_sel_keyword_cc(self,commitcode,object_id):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from keywords where commitcode=%s and object_id=%s"
        cursor.execute(sql,(commitcode,object_id))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close() 
    def bug_sel_bugname(self,object_id,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_name from bug where sub_type=%s and date >=%s and bug_status='完成'"
        cursor.execute(sql,(object_id,date))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()        
    def keyword_save(self,commitcode,object_id,keyword,count_num,create_date,bug_id):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into keywords (commitcode,object_id,keyword,count_num,create_date,bug_id)VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(commitcode,object_id,keyword,count_num,create_date,bug_id))
        conn.commit()
        cursor.close()
        conn.close()
    def keyword_del(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "delete from keywords where keyword =''"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    def bug_sel_bugid(self,object_id,date,keyword):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_id from bug where sub_type=%s and date >=%s and bug_status='完成' and bug_name like '%%"+keyword+"%%'"
        cursor.execute(sql,(object_id,date))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()  
#res=dbmysql().bug_sel_bugid("1","2017-09-13","接口")
#if res != ():
#    print res


