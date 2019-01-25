# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:50:28 2017

@author: Administrator
"""
import MySQLdb as mdb

class dbmysql(object):
#    localhost='113.107.166.5'
#    user='root'
#    passwd='rp1qaz@WSX'
#    databases='test_bigdata'
#    port=11606
    localhost='localhost'
    user='root'
    passwd='zwg123456'
    databases='test_bigdata'
    port=3306
    def save(self,objectname,date,change,name,commitcode):
#        print objectname,name,change,date,commitcode
    #    conn = mdb.connect('localhost','root','zwg123456','test_bigdata')
        conn = mdb.connect(host=self.localhost,user=self.user,passwd=self.passwd,db=self.databases,port=self.port,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into jenkins_source (object_id,change_name,change_source,date,commitcode)VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(objectname,name,change,date,commitcode))
        conn.commit()
        cursor.close()
        conn.close()
    def bug_save(self,bug_id,bug_name,bug_status,date,complete_user,ttype,sub_type,is_miss,title):
        if complete_user =="":
            complete_user="暂无"
    #    conn = mdb.connect('localhost','root','zwg123456','test_bigdata')
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into bug (bug_id,bug_name,bug_status,date,complete_user,type,sub_type,is_miss,title)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(bug_id,bug_name,bug_status,date,complete_user,ttype,sub_type,is_miss,title))
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
    def bug_sel_tandao(self,bug_id,bug_status,sub_type,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from bug where bug_id=%s and bug_status=%s and sub_type=%s and date=%s"
        cursor.execute(sql,(bug_id,bug_status,sub_type,date))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def bug_sel_commitcode(self,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select commitcode,change_name,object_id,change_source,date from jenkins_source where date >='"+date+"'"
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
    def bug_sel_bugname(self,object_id,startdate,enddate):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_name from bug where sub_type=%s and date >=%s and date <=%s and bug_status='新建'"
        cursor.execute(sql,(object_id,startdate,enddate))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def bug_sel_bugname_daykeywrods(self,object_id,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_name from bug where sub_type=%s and date >=%s and bug_status='完成'"
        cursor.execute(sql,(object_id,date))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def bug_sel_subtype(self,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select DISTINCT sub_type from bug where date >='"+date+"' and bug_status='完成'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close() 
    def bug_sel_bugid(self,object_id,startdate,enddate,keyword):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_id from bug where sub_type=%s and date >=%s and date <=%s and bug_status='完成' and bug_name like '%%"+keyword+"%%'"
        cursor.execute(sql,(object_id,startdate,enddate))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def bug_sel_bugid_daykeyword(self,object_id,date,keyword):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_id from bug where sub_type=%s and date >=%s and bug_status='新建' and bug_name like '%%"+keyword+"%%'"
        cursor.execute(sql,(object_id,date))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def keyword_save(self,commitcode,object_id,keyword,count_num,startdate,enddate,bug_id):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into keywords (commitcode,object_id,keyword,count_num,startdate,enddate,bug_id)VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(commitcode,object_id,keyword,count_num,startdate,enddate,bug_id))
        conn.commit()
        cursor.close()
        conn.close()
    def bug_keyword_save(self,date,object_id,keyword,count_num,create_date,bug_id):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into day_keywords (day,object_id,keyword,count_num,create_date,bug_id)VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(date,object_id,keyword,count_num,create_date,bug_id))
        conn.commit()
        cursor.close()
        conn.close()
    def keyword_del(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "delete from keywords where keyword ='' or bug_id=''"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    def bug_keyword_del(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "delete from day_keywords where keyword =''or bug_id=''"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    def testcase_sel(self,caseid,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from test_case where case_id=%s and creation_date=%s"
        cursor.execute(sql,(caseid,date))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()  
    def testcase_save(self,case_id,case_name,create_name,modification_name,creation_date,updater_date,typename):
        if modification_name =="":
            modification_name="无"
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into test_case (case_id,case_name,create_name,modification_name,creation_date,updater_date,type)VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(case_id,case_name,create_name,modification_name,creation_date,updater_date,typename))
        conn.commit()
        cursor.close()
        conn.close() 
    def testcase_update(self,case_id,case_name,modification_name,updater_date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "update test_case set case_name=%s,modification_name=%s,updater_date=%s where case_id=%s"
        cursor.execute(sql,(case_name,modification_name,updater_date,case_id))
        conn.commit()
        cursor.close()
        conn.close()
    def changename_level_sel(self,objectid,change_name):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from changename_level where object_id=%s and change_name=%s and level_name='轻'"
        cursor.execute(sql,(objectid,change_name))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def bug_levelwords_sel(self):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = """select object_id,level_word,level_id from bug_levelwords where status=0 and tag_name is not null"""
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def buglevel_update(self,object_id,level_id,level_word,date):
#        level_id=int(level_id)
        if object_id == 0:
            object_id=''
        else:
            object_id= "sub_type=\"+object_id+\" and "
            
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "update bug set level_id=%s where "+object_id+" date >=%s and bug_name like '%%"+level_word+"%%' and (level_id >=%s or level_id is null)"
        cursor.execute(sql,(level_id,date,level_id))
        conn.commit()
        cursor.close()
        conn.close()
    def bug_sel_allbugname(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_name from bug where bug_status='新建'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def levelwords_count(self,keyword):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from bug_levelwords where level_word='"+keyword+"' "
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def levelwords_insert(self,keyword,status):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into bug_levelwords (object_id,level_word,status)VALUES ('0','"+keyword+"','"+status+"')"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def levelwords_selname(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select level_word from bug_levelwords"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def levelwords_detail(self,keyword):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select level_id,tag_name from bug_levelwords where level_word='"+keyword+"' "
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def levelwords_no_tagname(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select level_word from bug_levelwords where status=1 or (Similarity < 0.8 and Similarity !='')"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def levelwords_update(self,keyword,level_id,tag_name,same_word,Similarity,status):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "update bug_levelwords set level_id=%s,tag_name=%s,same_word=%s,Similarity=%s,status=%s where level_word='"+keyword+"'"
        cursor.execute(sql,(level_id,tag_name,same_word,Similarity,status))
        conn.commit()
        cursor.close()
        conn.close()
    def object_name_sel(self,objectid):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select object_name from object_name where object_id='"+objectid+"'"
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def main_object_id_sel(self,objectid):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select main_object_id from object_name where object_id='"+objectid+"'"
        cursor.execute(sql)
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def change_name_sel(self,startdate,enddate):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select DISTINCT change_name,object_id from jenkins_source where date >=%s and date < %s"
        cursor.execute(sql,(startdate,enddate))
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def change_comment_insert(self,changename,object_id,comment,date,line_num,com_type):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into changename_comment (changename,object_id,comment,date,line_num,com_type)VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(changename,object_id,comment,date,line_num,com_type))
        conn.commit()
        cursor.close()
        conn.close()
    def change_comment_del(self,changename,object_id):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "delete from changename_comment where changename=%s and object_id=%s"
        cursor.execute(sql,(changename,object_id))
        conn.commit()
        cursor.close()
        conn.close()
#res=dbmysql().bug_sel_subtype("2017-09-13")
#if res != ():
#    print res[2]


