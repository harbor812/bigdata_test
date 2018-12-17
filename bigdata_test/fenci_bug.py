# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:03:18 2017

@author: Brianzhu
"""


import json 
import db_mysql
import datetime,time
import cut_sentence as cs

#import pandas as pd

if __name__ == '__main__':
     starttime=datetime.datetime.now()
     db=db_mysql.dbmysql()
     bugname=[]
     bugname1=[]
     bugnameall_list=[]
     bugnameall_datas=[]
     #获取所有commintcode 信息
#     date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = datetime.date.today() 
     yesterday = date - datetime.timedelta(days=1)
#     print date,yesterday
     date='2018-04-01'
     subtype=db.bug_sel_subtype(date)
     subtype_cn=len(subtype)
     i=0
     x=0
     j=0
     try:
         for i in range(subtype_cn):
             #获取commitcode 对应的bugname
    
             res=db.bug_sel_bugname_daykeywrods(subtype[i],date)
             #bugname 不为空 做词频统计和排序
             if res != ():
    #              print (res)
    #                  print "#####################################################"
                  if ')' in res:
                      i=res.split(")")
                      res=i[1].encode('utf-8')
                  if '）' in res:
                      i=res.split("）")
                      res=i[1].encode('utf-8')
    #              print res
                  strs=str(res).decode("unicode-escape")
    #                  strs=str(res)
                  dicts=cs.cut_sentence(strs)
                  sort_dict=sorted(dicts.iteritems(),key=lambda d:d[1],reverse=True)
                  key_dict=json.dumps(sort_dict,encoding="utf-8",ensure_ascii=False)
                  key_dict=key_dict.replace("\",",":")
                  dd=key_dict.replace("[","").replace("]","").replace("\"","")
                  dd=dd.split(",")
                  #合并有效数据，插入数据库
                  for x in range(len(dd)):
                      dt=dd[x].split(":")
                      date1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                      
                      if dt[1] != '':
                         #转译词频词并且去除空格
                         kw=dt[0].encode('utf-8').strip()
    #                         kw=dt[0]
                         if kw !='\\':
                             bugid=db.bug_sel_bugid_daykeyword(subtype[i],date,kw)
                             sub_type=str(subtype[i]).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
                             ob_id1=db.main_object_id_sel(sub_type)
                             ob_id=ob_id1[0]
    #                             print ob_id1
                             bugid=str(bugid).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
    #                         ob_id=ob_id1[0]
    #                         print "##########################"
    #                         print sub_type
    #                         print ob_id1[0]
                         print date,ob_id,kw,dt[1],date1,bugid
#                  j=x+x
#                  
#         print "======================================================"
#         print j
#                         print kw,dt[1]
#                             db.bug_keyword_save(date,subtype[i],kw,dt[1],date1,bugid)                    
#    #                     print kw
#    #                     time.sleep(1)
#                             if dt[1] > 1:
#                                 kwcount=db.levelwords_count(kw)
#                                 kwcount=kwcount[0]
#        #                     print kwcount
#                             #如果bug_levelwords 表没有 就插入
#                                 if kwcount ==0:
#                                     db.levelwords_insert(kw,'1')
#                             db.bug_keyword_del()
     except Exception,e:
         print e.message
                              
     endtime=datetime.datetime.now()
     rtime=(endtime - starttime).seconds 
     print rtime
