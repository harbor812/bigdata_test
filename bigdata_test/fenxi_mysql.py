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
        sql = "select bug_id,bug_status,sub_type,date from bug where date >='"+date+"'"
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
    def fx_changename_save(self,change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date,add_count,del_count,bug_new_id,bug_fix_id,bug_close_id):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into changename_statistics (change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date,add_count,del_count,bug_new_id,bug_fix_id,bug_close_id)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date,add_count,del_count,bug_new_id,bug_fix_id,bug_close_id))
        conn.commit()
        cursor.close()
        conn.close()
    def day_statistics_save(self,date,object_id,commit_count,change_count,change_totlecount,add_count,del_count,bug_new_count,bug_fix_count,bug_close_count):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into day_statistics (date,object_id,commit_count,change_count,change_totlecount,add_count,del_count,bug_new_count,bug_fix_count,bug_close_count)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(date,object_id,commit_count,change_count,change_totlecount,add_count,del_count,bug_new_count,bug_fix_count,bug_close_count))
        conn.commit()
        cursor.close()
        conn.close()
    def fx_changename_statistics_sel(self):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select change_name,object_id,starttime,new_bug_count,add_count,del_count from changename_statistics  where DATE_SUB(CURDATE(), INTERVAL 90 DAY) <=date(starttime) and  change_name not like '%.css'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def fx_changename_bug_probability_save(self,change_name,object_id,sum_bug,count_changename,bug_probability,create_date):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into changename_bug_probability (change_name,object_id,sum_bug,count_changename,bug_probability,create_date)VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(change_name,object_id,sum_bug,count_changename,bug_probability,create_date))
        conn.commit()
        cursor.close()
        conn.close()
    def fx_changename_Topkeyword_sel(self):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = """select js.change_name,kws.object_id,kws.keyword,sum(kws.count_num)  from keywords kws,jenkins_source js 
                where kws.COMMITcode=js.COMMITcode and  kws.object_id=js.object_id and  DATE_SUB(CURDATE(), INTERVAL 90 DAY) <=date(kws.startdate)
                GROUP BY js.change_name,kws.object_id,kws.keyword """
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def fx_changename_Topkeyword_save(self,change_name,object_id,keyword,keyword_count,create_date):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into changename_topkeyword (change_name,object_id,keyword,keyword_count,create_date)VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(change_name,object_id,keyword,keyword_count,create_date))
        conn.commit()
        cursor.close()
        conn.close()
    def fx_data_del(self,data):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "delete from "+data+""
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    def fx_changename_level_save(self,change_name,object_id,add_count,del_count,result_count,bug_count,level_name,create_date):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into changename_level (change_name,object_id,add_count,del_count,result_count,bug_count,level_name,create_date)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(change_name,object_id,add_count,del_count,result_count,bug_count,level_name,create_date))
        conn.commit()
        cursor.close()
        conn.close()
#res=dbmysql().bug_sel_bugid("1","2017-09-13","接口")
#if res != ():
#    print res
#res=dbmysql().fx_sel_jenkins("2017-09-13")
#if res != ():
#    print res

