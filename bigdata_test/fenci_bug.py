# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:03:18 2017

@author: Brianzhu
"""


import json 
import db_mysql
import datetime,time
import cut_sentence as cs


if __name__ == '__main__':
     starttime=datetime.datetime.now()
     db=db_mysql.dbmysql()
     #获取所有commintcode 信息
#     date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     date = datetime.date.today() 
     yesterday = date - datetime.timedelta(days=1)
     print date,yesterday
     date='2017-09-10'
     subtype=db.bug_sel_subtype(date)
     subtype_cn=len(subtype)
     i=0
     for i in range(subtype_cn):
         #获取commitcode 对应的bugname

         res=db.bug_sel_bugname_daykeywrods(subtype[i],date)
         #bugname 不为空 做词频统计和排序
         if res != ():
              strs=str(res).decode("unicode-escape")
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
                  if dt[0]:
                     #转译词频词并且去除空格
                     kw=dt[0].encode('utf-8').strip() 
                     bugid=db.bug_sel_bugid_daykeyword(subtype[i],date,kw)
                     bugid=str(bugid).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
                     print date,subtype[i],kw,dt[1],date1,bugid
                     db.bug_keyword_save(date,subtype[i],kw,dt[1],date1,bugid)
                     db.bug_keyword_del()
     endtime=datetime.datetime.now()
     rtime=(endtime - starttime).seconds 
     print rtime
