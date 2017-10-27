# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:39:54 2017

@author: Brianzhu
"""


import pandas as pd
import time
import fenxi_mysql
import json 
import db_mysql
import datetime
import cut_sentence as cs


def day_commitcode(date):
    db=fenxi_mysql.dbmysql()
    ob_data=[]
    fx_jk=db.fx_sel_jenkins(date)
    fx_bug=db.fx_sel_bug(date)
    
#    assert fx_bug !=0
    cn=len(fx_jk)
    cn_bug=len(fx_bug)
    for i in range(cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        ob_data.append(fx_jk[i][2].encode('utf-8'))
    ob_data=pd.DataFrame({'ob_data':ob_data})
    ob_data_distinct = ob_data.drop_duplicates() 
    
    
    cn1=len(ob_data_distinct)
    for i in range(cn1):
      cc_data=[]
      cn_data=[]
      cs_data=[]
      bugid_data=[]
      bugstatus_data=[]
      bug_new='0'
      bug_fix='0'
      bug_close='0'
      add_count='0'
      del_count='0'
      #同一个objectid的发布数据，存入对应数据
      for j in range(cn):
    #      print ob_data_distinct.iloc[i,0]
          if fx_jk[j][2] == ob_data_distinct.iloc[i,0]:
    #              print fx_jk[j][1]
                  cc_data.append(fx_jk[j][0].encode('utf-8'))
                  cn_data.append(fx_jk[j][1].encode('utf-8'))
                  cs_data.append(fx_jk[j][3].encode('utf-8'))    
      #同一个objectid的bug数据，存入对应数据              
      for x in range(cn_bug):
    #      print ob_data_distinct.iloc[i,0]
          if fx_bug[x][2] == ob_data_distinct.iloc[i,0]:
                  bugid_data.append(fx_bug[x][0].encode('utf-8'))
                  bugstatus_data.append(fx_bug[x][1].encode('utf-8'))
      #拆分change_source
      cs_data_s=str(cs_data).split(",")
    #  print cs_data_s
      #commitcode,change_name 数据转表单格式            
      cc_data=pd.DataFrame({'cc_data':cc_data})
      cn_data=pd.DataFrame({'cn_data':cn_data})
      cs_data=pd.DataFrame({'cs_data':cs_data_s})
      bug_data=pd.DataFrame({'bugid_data':bugid_data,'bugstatus_data':bugstatus_data})
    #  bugstatus_data=pd.DataFrame({'cn_data':bugstatus_data})
      #commitcode,change_name 去重
      cc_data_distinct = cc_data.drop_duplicates() 
      cn_data_distinct = cn_data.drop_duplicates()
      bugid_data_distinct = bug_data.drop_duplicates(['bugid_data']) 
    
      #commitcode,change_name 去重后统计
      #bugid 去重后统计
      cc_data_distinct_count=cc_data_distinct.count()
      cn_data_distinct_count = cn_data_distinct.count()
      bugid_data_distinct_count=bugid_data_distinct.count()
      #change_name 不去重后统计  
      cn_data_count=cn_data.count()
      #新增和删除的代码操作数量
    #  print cs_data
      add_cn=cs_data[cs_data['cs_data'].str.contains('add:')].count()
      del_cn=cs_data[cs_data['cs_data'].str.contains('del:')].count()
      add_count=add_cn["cs_data"]
      del_count=del_cn["cs_data"]  
    
      #统计各个状态的bug数
      if bugid_data_distinct_count["bugid_data"] !=0:
          bugstatus_count=bug_data[bug_data['bugstatus_data'].str.contains('完成')].count()
          bugstatus_count1=bug_data[bug_data['bugstatus_data'].str.contains('新建')].count()
          bugstatus_count2=bug_data[bug_data['bugstatus_data'].str.contains('提交')].count()
          bug_close=bugstatus_count["bugstatus_data"]
          bug_new=bugstatus_count1["bugstatus_data"]
          bug_fix=bugstatus_count2["bugstatus_data"]
      db.day_statistics_save(date,ob_data_distinct.iloc[i,0],cc_data_distinct_count["cc_data"],cn_data_distinct_count["cn_data"],cn_data_count["cn_data"],add_count,del_count,bug_new,bug_fix,bug_close)

def day_changename(date):
    db=fenxi_mysql.dbmysql()
    ob_data=[]
    fx_jk=db.fx_sel_jenkins(date)
    fx_bug=db.fx_sel_bug(date)
    
    assert fx_bug !=0
    cn=len(fx_jk)
    cn_bug=len(fx_bug)
    for i in range(cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        ob_data.append(fx_jk[i][1].encode('utf-8'))
    ob_data=pd.DataFrame({'ob_data':ob_data})
    ob_data_distinct = ob_data.drop_duplicates() 
    
    cn1=len(ob_data_distinct)
    for i in range(cn1):
      cc_data=[]
      cn_data=[]
      cs_data=[]
      j_date=[]
      bugid_data=[]
      bugstatus_data=[]
      bug_new='0'
      bug_fix='0'
      bug_close='0'
      add_count='0'
      del_count='0'
      z=0
      #同一个objectid的发布数据，存入对应数据
      for j in range(cn):
    #      print ob_data_distinct.iloc[i,0]
          if fx_jk[j][1] == ob_data_distinct.iloc[i,0]:
    #              print fx_jk[j][1]
                  cc_data.append(fx_jk[j][0].encode('utf-8'))
                  cn_data.append(fx_jk[j][2].encode('utf-8'))
                  cs_data.append(fx_jk[j][3].encode('utf-8')) 
                  j_date.append(str(fx_jk[j][4]))
      print ob_data_distinct.iloc[i,0],cc_data,cn_data,cs_data,j_date

      fcn=len(j_date)
      for x in range(fcn):
          if z < fcn-1:
              z=z+1
              print j_date[x],j_date[z],cn_data[x]
              bug_cn=db.fx_sel_bug_count(j_date[x],j_date[z],cn_data[x])
              print bug_cn[0]
      break        
      #同一个objectid的bug数据，存入对应数据              
#      for x in range(cn_bug):
#    #      print ob_data_distinct.iloc[i,0]
#          if fx_bug[x][2] == ob_data_distinct.iloc[i,0]:
#                  bugid_data.append(fx_bug[x][0].encode('utf-8'))
#                  bugstatus_data.append(fx_bug[x][1].encode('utf-8'))
#      #拆分change_source
#      cs_data_s=str(cs_data).split(",")
#    #  print cs_data_s
#      #commitcode,change_name 数据转表单格式            
#      cc_data=pd.DataFrame({'cc_data':cc_data})
#      cn_data=pd.DataFrame({'cn_data':cn_data})
#      cs_data=pd.DataFrame({'cs_data':cs_data_s})
#      bug_data=pd.DataFrame({'bugid_data':bugid_data,'bugstatus_data':bugstatus_data})
#    #  bugstatus_data=pd.DataFrame({'cn_data':bugstatus_data})
#      #commitcode,change_name 去重
#      cc_data_distinct = cc_data.drop_duplicates() 
#      cn_data_distinct = cn_data.drop_duplicates()
#      bugid_data_distinct = bug_data.drop_duplicates(['bugid_data']) 
#    
#      #commitcode,change_name 去重后统计
#      #bugid 去重后统计
#      cc_data_distinct_count=cc_data_distinct.count()
#      cn_data_distinct_count = cn_data_distinct.count()
#      bugid_data_distinct_count=bugid_data_distinct.count()
#      #change_name 不去重后统计  
#      cn_data_count=cn_data.count()
#      #新增和删除的代码操作数量
#    #  print cs_data
#      add_cn=cs_data[cs_data['cs_data'].str.contains('add:')].count()
#      del_cn=cs_data[cs_data['cs_data'].str.contains('del:')].count()
#      add_count=add_cn["cs_data"]
#      del_count=del_cn["cs_data"]  
#    
#      #统计各个状态的bug数
#      if bugid_data_distinct_count["bugid_data"] !=0:
#          bugstatus_count=bug_data[bug_data['bugstatus_data'].str.contains('完成')].count()
#          bugstatus_count1=bug_data[bug_data['bugstatus_data'].str.contains('新建')].count()
#          bugstatus_count2=bug_data[bug_data['bugstatus_data'].str.contains('提交')].count()
#          bug_close=bugstatus_count["bugstatus_data"]
#          bug_new=bugstatus_count1["bugstatus_data"]
#          bug_fix=bugstatus_count2["bugstatus_data"]
#      db.day_statistics_save(date,ob_data_distinct.iloc[i,0],cc_data_distinct_count["cc_data"],cn_data_distinct_count["cn_data"],cn_data_count["cn_data"],add_count,del_count,bug_new,bug_fix,bug_close)

def day_bug_cut(date):
     db=db_mysql.dbmysql()
     #获取所有commintcode 信息
     #date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
     #print date
     subtype=db.bug_sel_subtype(date)
     for j in range(len(subtype)):
         #获取commitcode 对应的bugname
         subtype1=str(subtype[j]).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")

         res=db.bug_sel_bugname(subtype1,date)
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
                  date1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                  if dt[0]:
                     #转译词频词并且去除空格
                     kw=dt[0].encode('utf-8').strip() 
                     bugid=db.bug_sel_bugid(subtype1,date,kw)
                     bugid=str(bugid).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
                     db.bug_keyword_save(date,subtype1,kw,dt[1],date1,bugid)
                     db.bug_keyword_del()
                     
if __name__ == '__main__':
#     starttime=datetime.datetime.now()
    #
    #date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #print date
    date='2017-09-10'
#    day_commitcode(date)
    day_changename(date)
#    day_bug_cut(date)
#     endtime=datetime.datetime.now()
#     rtime=(endtime - starttime).seconds 
#     print rtime 