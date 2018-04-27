# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:13:58 2017

@author: Brianzhu
"""

import pandas as pd
import json,time  
import db_mysql
import datetime
import cut_sentence as cs



def keywords(date):
    db=db_mysql.dbmysql()
    ob_data=[]
    datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
     #获取所有commintcode 信息
    jenkins_source=db.bug_sel_commitcode(date)
    cn=len(jenkins_source)
    fcn=0
    for i in range(cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
       ob_data.append(jenkins_source[i][0].encode('utf-8'))
    ob_data=pd.DataFrame({'ob_data':ob_data})
    ob_data_distinct = ob_data.drop_duplicates()
    cn1=len(ob_data_distinct)
    
    for i in range(cn1):
      type_data=[]
#      cs_data=[]
      j_date=[]
      fcn='0'
      z=0
      ob_data=ob_data_distinct.iloc[i,0]
      #同一个objectid的发布数据，存入对应数据
      for j in range(cn):
          #按 change_name 归类，插入list 
          print "jenkins_source:",jenkins_source[j][0]
          print "ob_data:",ob_data
          if jenkins_source[j][0] == ob_data:
    #              print fx_jk[j][1]
                  type_data.append(jenkins_source[j][2].encode('utf-8'))
#                  cs_data.append(jenkins_source[j][3].encode('utf-8')) 
                  j_date.append(str(jenkins_source[j][4]))
#      print ob_data_distinct.iloc[i,0],cc_data,cn_data,cs_data,j_date
      fcn=len(j_date)
      print fcn
#      cs_data=pd.DataFrame({'cs_data':cs_data,'j_date':j_date,'type_data':type_data})
      #分析每次提交程序的bug
      for x in range(fcn):
          if z < fcn-1:
              z=z+1
              enddate=str(j_date[z])
          else:
              z=z+1
              enddate=datetime
          startdate=str(j_date[x])
          ob_id=type_data[x]
          print startdate,enddate,ob_id
#             
          res=db.bug_sel_bugname(ob_id,startdate,enddate)
             
             
             
#             bugname 不为空 做词频统计和排序
          if res != ():
                 strs=str(res).decode("unicode-escape")
                 dicts=cs.cut_sentence(strs)
                 sort_dict=sorted(dicts.iteritems(),key=lambda d:d[1],reverse=True)
                 key_dict=json.dumps(sort_dict,encoding="utf-8",ensure_ascii=False)
                 key_dict=key_dict.replace("\",",":")
                 dd=key_dict.replace("[","").replace("]","").replace("\"","")
                 dd=dd.split(",")
                 #合并有效数据，插入数据库
                 for i in range(len(dd)):
                    dt=dd[i].split(":")
                    date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    if dt[0]:
                        #转译词频词并且去除空格
                        kw=dt[0].encode('utf-8').strip() 
                        bugid=db.bug_sel_bugid(ob_id,startdate,enddate,kw)
                        bugid=str(bugid).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
                        print ob_data,ob_id,kw,dt[1],startdate,enddate,bugid
                        db.keyword_save(ob_data,ob_id,kw,dt[1],startdate,enddate,bugid)
                        db.keyword_del()
#      endtime=datetime
#      rtime=(endtime - starttime).seconds 
#      print rtime






if __name__ == '__main__':

 starttime=datetime.datetime.now()
#
 date = datetime.date.today()
 date = str(date)
   
#print date
 date='2018-04-11'
 print "------开始时间--------------",starttime,"---------------------------------"
 keywords(date)
 endtime=datetime.datetime.now()
 rtime=(endtime - starttime).seconds
 print "------结束时间-------------",endtime,"------------------------------------"
 print "------运行耗时-------------",rtime,"----------------------------------------"