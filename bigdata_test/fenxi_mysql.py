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
        sql = "select bug_id,bug_status,sub_type,date,bug_name,tag_name,level_id from bug where date >='"+date+"'"
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
                where kws.COMMITcode=js.COMMITcode and  kws.object_id=js.object_id and  DATE_SUB(CURDATE(), INTERVAL 90 DAY) <=date(kws.startdate) and  change_name not like '%.css'
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
    def fx_bug_levelwords_sel(self):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = """select object_id,level_word,level_id,tag_name,ifnull(priority,0) from bug_levelwords where status=0"""
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def fx_buglevel_update(self,level_id,tag_name,bug_id):

            
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "update bug set level_id=%s,tag_name=%s where bug_id=%s "
        cursor.execute(sql,(level_id,tag_name,bug_id))
        conn.commit()
        cursor.close()
        conn.close()
    def fx_buglevel_bugid_sel(self,object_id,level_word,date):
        if object_id == 0:
            object_id=''
        else:
            object_id= "sub_type=\"+object_id+\" and "
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select bug_id from bug where bug_status='新建' and "+object_id+" date >='"+date+"' and bug_name like '%"+level_word+"%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close() 
    def fx_sel_daybug(self,object_id):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select date_format(date,'%y-%m-%d'),count(*) from bug where bug_status='新建' and DATE_SUB(CURDATE(), INTERVAL 10 DAY) <=date(date)  and sub_type='"+object_id+"' GROUP BY date_format(date,'%y-%m-%d')"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close() 
    def bug_objectid_sel(self,objectid,startdate,enddate):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*) from bug where sub_type=%s and date >=%s and date < %s and bug_status='新建'"
        cursor.execute(sql,(objectid,startdate,enddate))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def object_id_sel(self):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select object_id from object_name "
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
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
    def project_stat_save(self,project_name,object_id,start_date,status):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into project_statistics (project_name,object_id,startdate,status)VALUES (%s,%s,%s,%s)"
        cursor.execute(sql,(project_name,object_id,start_date,status))
        conn.commit()
        cursor.close()
        conn.close()
    def project_stat_sel(self,object_id,status):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(*),startdate from project_statistics where object_id=%s and status=%s"
        cursor.execute(sql,(object_id,status))
        results = cursor.fetchone()
        return results
        cursor.close()
        conn.close()
    def project_stat_update(self,total,jk_total,enddate,status1,object_id,status):            
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "update project_statistics set bug_count=%s,commit_count=%s,enddate=%s,status=%s where object_id=%s and status=%s "
        cursor.execute(sql,(total,jk_total,enddate,status1,object_id,status))
        conn.commit()
        cursor.close()
        conn.close()
    def jenkins_source_sel(self,objectid,startdate,enddate):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select count(DISTINCT commitcode) from jenkins_source where object_id in (select object_id from object_name where main_object_id=%s) and date >=%s and date < %s"
        cursor.execute(sql,(objectid,startdate,enddate))
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
    def change_comment_sel(self,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select changename,cc.object_id,comment,obn.main_object_id,cc.line_num,com_type from changename_comment  cc,object_name obn where cc.date >='"+date+"' and cc.object_id=obn.object_id"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
        cursor.close()
        conn.close()
    def changename_bugid_save(self,changename,ob_id,comment,bug_id_list,date,line_num,com_type):
        #print change_name,object_id,starttime,endtime,new_bug_count,fix_bug_count,close_bug_count,create_date
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "INSERT into changename_bugid (changename,object_id,comment,bug_id,date,line_num,com_type)VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(changename,ob_id,comment,bug_id_list,date,line_num,com_type))
        conn.commit()
        cursor.close()
        conn.close()
    def changename_bugid_sel(self,changename,ob_id,date):
        conn = mdb.connect(self.localhost,self.user,self.passwd,self.databases,charset="utf8")
        cursor=conn.cursor()          #定义连接对象
        sql = "select GROUP_CONCAT(DISTINCT bug_id) from changename_bugid where bug_id !='' and changename=%s and object_id=%s and date >=%s"
        cursor.execute(sql,(changename,ob_id,date))
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

