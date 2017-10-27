# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:03:18 2017

@author: Brianzhu
"""


import json,time  
import db_mysql
import datetime
import cut_sentence as cs


if __name__ == '__main__':
#     starttime=datetime.datetime.now()
     db=db_mysql.dbmysql()
     #获取所有commintcode 信息
     #date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     #print date
     date='2017-09-10'
     subtype=db.bug_sel_subtype(date)
     for i in range(len(subtype)):
         #获取commitcode 对应的bugname
         res=db.bug_sel_bugname(subtype[i],date)
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
              for i in range(len(dd)):
                  dt=dd[i].split(":")
                  date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                  if dt[0]:
                     #转译词频词并且去除空格
                     kw=dt[0].encode('utf-8').strip() 
                     bugid=db.bug_sel_bugid(subtype[i],date,kw)
                     bugid=str(bugid).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
                     db.keyword_save(cc[0],cc[2],kw,dt[1],date,bugid)
                     db.keyword_del()
#     endtime=datetime.datetime.now()
#     rtime=(endtime - starttime).seconds 
#     print rtime