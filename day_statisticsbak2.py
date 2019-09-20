# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:39:54 2017

@author: Brianzhu
"""


import pandas as pd
import time
import fenxi_mysql
#import json 
#import db_mysql
import datetime
#import cut_sentence as cs
from business_calendar import Calendar
import synonyms

def day_commitcode(date):

    db=fenxi_mysql.dbmysql()
    ob_data=[]
    fx_jxold=([0])
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
      fx_jx=db.main_object_id_sel(ob_data_distinct.iloc[i,0])
#      print fx_jx[0],fx_jxold[0]
      if fx_jx[0] != fx_jxold[0]:

          for j in range(cn):
        #      print ob_data_distinct.iloc[i,0]
              fx_jx1=db.main_object_id_sel(fx_jk[j][2])
              if fx_jx1[0] == fx_jx[0]:
        #              print fx_jk[j][1]
                      cc_data.append(fx_jk[j][0].encode('utf-8'))
                      cn_data.append(fx_jk[j][1].encode('utf-8'))
                      cs_data.append(fx_jk[j][3].encode('utf-8'))    
          #同一个objectid的bug数据，存入对应数据              
          for x in range(cn_bug):
        #      print ob_data_distinct.iloc[i,0]
              if fx_bug[x][2] == fx_jx[0]:
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
          fx_jxold=db.main_object_id_sel(ob_data_distinct.iloc[i,0])
          
#          print date,fx_jx[0],cc_data_distinct_count["cc_data"],cn_data_distinct_count["cn_data"],cn_data_count["cn_data"],add_count,del_count,bug_new,bug_fix,bug_close
          db.day_statistics_save(date,fx_jx[0],cc_data_distinct_count["cc_data"],cn_data_distinct_count["cn_data"],cn_data_count["cn_data"],add_count,del_count,bug_new,bug_fix,bug_close)
 
def day_changename(date):
    db=fenxi_mysql.dbmysql()
    ob_data=[]
#    fx_bugid=[]
#    fx_bugstatus=[]
#    fx_bugsub_type=[]
#    fx_bugdate=[]
    fx_jk=db.fx_sel_jenkins(date)
#    fx_bug=db.fx_sel_bug(date)
    bug_close_id=''
    bug_new_id=''
    bug_fix_id=''
    datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


#    assert fx_bug !=0
    cn=len(fx_jk)
#    cn_bug=len(fx_bug)
    for i in range(cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        ob_data.append(fx_jk[i][1].encode('utf-8'))
    ob_data=pd.DataFrame({'ob_data':ob_data})
#    print ob_data
    ob_data_distinct = ob_data.drop_duplicates() 
    
    cn1=len(ob_data_distinct)
    
    #所有BUG数据变为list
#    for x in range(cn_bug):
#
##          if  fx_bug[x][1].encode('utf-8') == '完成':
#    #              print fx_jk[j][1]
#                  fx_bugid.append(fx_bug[x][0].encode('utf-8'))
#                  fx_bugstatus.append(fx_bug[x][1].encode('utf-8'))
#                  fx_bugsub_type.append(fx_bug[x][2].encode('utf-8'))
#                  fx_bugdate.append(str(fx_bug[x][3])) 
#
#
#    bug_data=pd.DataFrame({'fx_bugid':fx_bugid,'fx_bugstatus':fx_bugstatus,'fx_bugsub_type':fx_bugsub_type,'fx_bugdate':fx_bugdate})
#    bug_data_cn=bug_data["fx_bugid"].count()
    
    
    for i in range(cn1):
      type_data=[]
      cs_data=[]
      j_date=[]
      add_count='0'
      del_count='0'
      fcn='0'
      z=0
      bug_new='0'
      bug_fix='0'
      bug_close='0'
      bug_new_id='0'
      bug_fix_id='0'
      bug_close_id='0'

      ob_data=ob_data_distinct.iloc[i,0]
      #同一个objectid的发布数据，存入对应数据
      for j in range(cn):
          #按 change_name 归类，插入list 
          if fx_jk[j][1] == ob_data:
    #              print fx_jk[j][1]
                  type_data.append(fx_jk[j][2].encode('utf-8'))
                  cs_data.append(fx_jk[j][3].encode('utf-8')) 
                  j_date.append(str(fx_jk[j][4]))
#      print ob_data_distinct.iloc[i,0],cc_data,cn_data,cs_data,j_date
      fcn=len(j_date)
      cs_data=pd.DataFrame({'cs_data':cs_data,'j_date':j_date,'type_data':type_data})
      #分析每个提交程序的bug数
      for x in range(fcn):
          if z < fcn-1:
              z=z+1
              enddate=str(j_date[z])
          else:
              z=z+1
              enddate=datetime
          startdate=str(j_date[x])
          ob_id1=type_data[x]
          ob_id2=db.main_object_id_sel(ob_id1)
          ob_id=ob_id2[0]
#          print '############################################'
#          print startdate,enddate,ob_id

          #选取和统计代码修改数
          cs_data1=cs_data[(cs_data['j_date'] >=startdate) & (cs_data['j_date'] < enddate) & (cs_data['type_data'] == ob_id)]
          cs_data_list=cs_data1['cs_data'].tolist()
          cs_data_s=str(cs_data_list).split(",")
#              cs_data_s=list(cs_data1["cs_data"])
          cs_data2=pd.DataFrame({'cs_data':cs_data_s})
          add_cn=cs_data2[cs_data2['cs_data'].str.contains('add:')].count()
          del_cn=cs_data2[cs_data2['cs_data'].str.contains('del:')].count()
          add_count=add_cn["cs_data"]
          del_count=del_cn["cs_data"]
#          bug_data_cn=int(bug_data_cn)
          #选取和统计bug数
#          if bug_data_cn > 0:
#              print "bug 数量：",bug_data_cn
#              bug_data1=bug_data[(bug_data['fx_bugdate'] >=startdate) & (bug_data['fx_bugdate'] < enddate) & (bug_data['fx_bugsub_type'] == ob_id)]
              #if bug_data1["fx_bugid"].count() != '0':            
#              bug_close_cn=bug_data1[bug_data1['fx_bugstatus'].str.contains('完成')].count()
#              bug_new_cn=bug_data1[bug_data1['fx_bugstatus'].str.contains('新建')].count()
#              bug_fix_cn=bug_data1[bug_data1['fx_bugstatus'].str.contains('已提交')].count()
#              bug_new=bug_new_cn['fx_bugid']
#              bug_fix=bug_fix_cn['fx_bugid']
#              bug_close=bug_close_cn['fx_bugid']
              
#              if bug_close !='0':
#                  bugid_close=bug_data1[bug_data1['fx_bugstatus'].str.contains('完成')]
#                  bug_close_id=str(list(bugid_close['fx_bugid'])).replace("[","").replace("]","").replace("'","")
#              if bug_new !='0':
#                  bugid_new=bug_data1[bug_data1['fx_bugstatus'].str.contains('新建')]
#                  bug_new_id=str(list(bugid_new['fx_bugid'])).replace("[","").replace("]","").replace("'","")
#              if bug_fix !='0':
#                  bugid_fix=bug_data1[bug_data1['fx_bugstatus'].str.contains('已提交')]
#                  bug_fix_id=str(list(bugid_fix['fx_bugid'])).replace("[","").replace("]","").replace("'","")
#          print ob_data,ob_id,startdate,enddate,bug_new,bug_fix,bug_close,date,add_count,del_count,bug_new_id,bug_fix_id,bug_close_id
          #获取对应代码 关联的bug
          changename_bug_list=db.changename_bugid_sel(ob_data,ob_id1,date)
          bug_new_id=changename_bug_list[0]
          if bug_new_id == None:
               bug_new_id=''
          else:
               bug_list1=bug_new_id.split(",")
               bug_new=len(bug_list1)        
      db.fx_changename_save(ob_data,ob_id1,startdate,enddate,bug_new,bug_fix,bug_close,date,add_count,del_count,bug_new_id,bug_fix_id,bug_close_id)

def day_changename_bug_probability(date):
    db=fenxi_mysql.dbmysql()
    fx_change_name=[]
    fx_change_name1=[]
    fx_object_id=[]
    fx_object_id1=[]
#    fx_starttime=[]
    fx_new_bug_count=[]
    db.fx_data_del("changename_bug_probability")
    fx_cns=db.fx_changename_statistics_sel()
#    print  "fx_cns:",fx_cns
    cn_fx_cn=len(fx_cns)
    #获取change_name+object_id，并按照change_name+object_id去重
    for i in range(cn_fx_cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        fx_change_name1.append(fx_cns[i][0].encode('utf-8'))
        fx_object_id1.append(fx_cns[i][1])
    fx_change_name1=pd.DataFrame({'fx_object_id1':fx_object_id1,'fx_change_name1':fx_change_name1})
    fx_change_name1_distinct = fx_change_name1.drop_duplicates()  
#    print fx_change_name1_distinct
    cn1=len(fx_change_name1_distinct)
#    print fx_change_name1_distinct  
    #获取change_name+object_id+new_bug_count
    for x in range(cn_fx_cn):
          fx_change_name.append(fx_cns[x][0].encode('utf-8'))
          fx_object_id.append(fx_cns[x][1])
#          fx_starttime.append(str(fx_cns[x][2]))
          fx_new_bug_count.append(fx_cns[x][3]) 
    #数组保存成DataFrame
    cns_data=pd.DataFrame({'fx_change_name':fx_change_name,'fx_object_id':fx_object_id,'fx_new_bug_count':fx_new_bug_count})


    for i in range(cn1):
#        print '##########################################'
        changename_data=fx_change_name1_distinct.iloc[i,0]
        object_id=fx_change_name1_distinct.iloc[i,1]
#        print changename_data,object_id
#        print '##########################################'
        changename_data1=cns_data[(cns_data['fx_change_name'] == changename_data) &(cns_data['fx_object_id'] == object_id)]
#        print changename_data1
        sum_bug=changename_data1['fx_new_bug_count'].sum()
        count_changename=changename_data1['fx_change_name'].count()
#        print "bug数，提交次数：",sum_bug,count_changename
        bug_probability=format(float(sum_bug)/float(count_changename)* 100,'.2f')
#        print "出现bug概率：",bug_probability
#        print "要插入数据：",changename_data,object_id,sum_bug,count_changename,bug_probability,date
        db.fx_changename_bug_probability_save(changename_data,object_id,sum_bug,count_changename,bug_probability,date)
        
def day_changename_topkeyword(date):
    db=fenxi_mysql.dbmysql()
    fx_change_name=[]
    fx_change_name1=[]
    fx_object_id=[]
    fx_object_id1=[]
    fx_keyword=[]
    fx_keywrod_count=[]
    db.fx_data_del("changename_topkeyword")
    db.fx_data_del("keywords where keyword = '后台' and object_id=2")
    db.fx_data_del("day_keywords where keyword = '后台' and object_id=2")
    db.fx_data_del("keywords where keyword = '泡面番' and object_id=2")
    db.fx_data_del("day_keywords where keyword = '泡面番' and object_id=2")
    db.fx_data_del("keywords where keyword = '数据' and object_id=6")
    db.fx_data_del("day_keywords where keyword = '数据' and object_id=6")
    fx_cns=db.fx_changename_Topkeyword_sel()
#    print  "fx_cns:",fx_cns
    cn_fx_cn=len(fx_cns)
    #获取change_name+object_id，并按照change_name+object_id去重
    for i in range(cn_fx_cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        fx_change_name1.append(fx_cns[i][0].encode('utf-8'))
        fx_object_id1.append(fx_cns[i][1])
    fx_change_name1=pd.DataFrame({'fx_object_id1':fx_object_id1,'fx_change_name1':fx_change_name1})
    fx_change_name1_distinct = fx_change_name1.drop_duplicates()  
#    print fx_change_name1_distinct
    cn1=len(fx_change_name1_distinct)
#    print fx_change_name1_distinct     
    #获取change_name+object_id+new_bug_count
    for x in range(cn_fx_cn):
          fx_change_name.append(fx_cns[x][0].encode('utf-8'))
          fx_object_id.append(fx_cns[x][1])
          fx_keyword.append(fx_cns[x][2].encode('utf-8'))
          fx_keywrod_count.append(fx_cns[x][3]) 
    #数组保存成DataFrame
    cns_data=pd.DataFrame({'fx_change_name':fx_change_name,'fx_object_id':fx_object_id,'fx_keyword':fx_keyword,'fx_keywrod_count':fx_keywrod_count})

    for i in range(cn1):
#        print '##########################################'
        changename_data=fx_change_name1_distinct.iloc[i,0]
        object_id=fx_change_name1_distinct.iloc[i,1]
#        print changename_data,object_id

        changename_data1=cns_data[(cns_data['fx_change_name'] == changename_data) &(cns_data['fx_object_id'] == object_id)]
#        print changename_data1
#        print '##########################################'
        #按照fx_keywrod_count 倒序
        key_order=changename_data1.sort_values(by='fx_keywrod_count',axis = 0,ascending = False)
        #取第一行数据
        changename_1=key_order.iloc[0,0]
        keyword_1=key_order.iloc[0,1]
        keywrod_count_1=key_order.iloc[0,2]
        object_id_1=key_order.iloc[0,3]
#        print key_order
#        print '##########################################'
#        print changename_1,object_id_1,keyword_1,keywrod_count_1,date
        db.fx_changename_Topkeyword_save(changename_1,object_id_1,keyword_1,keywrod_count_1,date)
 
def day_changename_bug_level(date):
    db=fenxi_mysql.dbmysql()
    fx_change_name=[]
    fx_change_name1=[]
    fx_object_id=[]
    fx_object_id1=[]
    fx_new_bug_count=[]
    fx_add_count=[]
    fx_del_count=[]
    add_count=0
    del_count=0
    db.fx_data_del("changename_level")
    fx_cns=db.fx_changename_statistics_sel()
#    print  "fx_cns:",fx_cns
    cn_fx_cn=len(fx_cns)
    #获取change_name+object_id，并按照change_name+object_id去重
    for i in range(cn_fx_cn):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        fx_change_name1.append(fx_cns[i][0].encode('utf-8'))
        fx_object_id1.append(fx_cns[i][1])
    fx_change_name1=pd.DataFrame({'fx_object_id1':fx_object_id1,'fx_change_name1':fx_change_name1})
    fx_change_name1_distinct = fx_change_name1.drop_duplicates()  
#    print fx_change_name1_distinct
    cn1=len(fx_change_name1_distinct)
#    print fx_change_name1_distinct     
    #获取change_name+object_id+new_bug_count
    for x in range(cn_fx_cn):
          fx_change_name.append(fx_cns[x][0].encode('utf-8'))
          fx_object_id.append(fx_cns[x][1])
          fx_new_bug_count.append(fx_cns[x][3])
          fx_add_count.append(fx_cns[x][4]) 
          fx_del_count.append(fx_cns[x][5]) 

    #数组保存成DataFrame
    cns_data=pd.DataFrame({'fx_change_name':fx_change_name,'fx_object_id':fx_object_id,'fx_new_bug_count':fx_new_bug_count,'fx_add_count':fx_add_count,'fx_del_count':fx_del_count})

    for i in range(cn1):
#        print '##########################################'
        changename_data=fx_change_name1_distinct.iloc[i,0]
        object_id=fx_change_name1_distinct.iloc[i,1]
#        print changename_data,object_id
        changename_data1=cns_data[(cns_data['fx_change_name'] == changename_data) &(cns_data['fx_object_id'] == object_id)]
        add_count=int(changename_data1['fx_add_count'].sum())
        del_count=int(changename_data1['fx_del_count'].sum())
        new_bug_count=int(changename_data1['fx_new_bug_count'].sum())
#        print changename_data,object_id,add_count,del_count,new_bug_count
#        print '##########################################'
#        print add_count,del_count
        result_count=add_count-del_count
#        print result_count,new_bug_count
        if result_count == 0:
            if new_bug_count >= 0 and new_bug_count <= 2:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻1",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)
            if new_bug_count >2 and new_bug_count <= 5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中1",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                
            if new_bug_count >5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重1",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                
                
#            break
        if (result_count > 0 and result_count <= 20) or (result_count < 0 and result_count >= -20):
            if new_bug_count >= 0 and new_bug_count <= 3:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻2",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)
            if new_bug_count >3 and new_bug_count <= 10:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中2",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                                
            if new_bug_count >10:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重2",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                
                
#            break
        if (result_count > 20 and result_count <= 100) or (result_count < -20 and result_count >= -100):
            if new_bug_count >= 0 and new_bug_count <= 4:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻3",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)                
            if new_bug_count >4 and new_bug_count <= 12:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中3",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                                
            if new_bug_count >12:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重3",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                                
#            break
        if  result_count > 100  or result_count < -100:
            if new_bug_count >= 0 and new_bug_count <= 5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻4",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)                
            if new_bug_count >5 and new_bug_count <= 15:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中4",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                                
            if new_bug_count >15:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重4",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                
                
#            break

def day_bug_level(date):
    db=fenxi_mysql.dbmysql()
    bug_level=db.fx_bug_levelwords_sel()
    bug_level_cn=len(bug_level)

    buglevel_data=pd.DataFrame({'fx_tag_name':[],'fx_level_id':[],'fx_object_id':[],'fx_bugid':[],'fx_priority':[]})

#    print bug_level
    #合并所有bug+level_id 的数据
    for x in range(bug_level_cn):
        object_id=bug_level[x][0]
        level_word=bug_level[x][1].encode('utf-8')
        level_id=bug_level[x][2]
        tag_name=bug_level[x][3]
	priority=bug_level[x][4]
#        print object_id,level_id,level_word,date
        bugid_list=db.fx_buglevel_bugid_sel(object_id,level_word,date)  
#        print bugid_list
        fx_tag_name=[]
        fx_level_id=[]
        fx_object_id=[]
        fx_bugid=[]
	fx_priority=[]
        #进行数据合并  
        for y in range(len(bugid_list)):
#             print bugid_list[y][0]
             fx_tag_name.append(tag_name)
             fx_level_id.append(level_id)
             fx_object_id.append(object_id)
             fx_bugid.append(bugid_list[y][0])
	     fx_priority.append(priority) 
        buglevel_data1=pd.DataFrame({'fx_tag_name':fx_tag_name,'fx_level_id':fx_level_id,'fx_object_id':fx_object_id,'fx_bugid':fx_bugid,'fx_priority':fx_priority})

        frames=[buglevel_data,buglevel_data1]
        buglevel_data=pd.concat(frames)
#        
#        print buglevel_data
    #获取所有bug_id
    bugid_distinct = buglevel_data.drop_duplicates(['fx_bugid'])
#    print bugid_distinct
    #统计条数
    bugid_cn=bugid_distinct['fx_bugid'].count()
    
    ###对每个BUG 等级和标签 进行分析
    for i in range(bugid_cn):
           bug_id=str(bugid_distinct.iloc[i,0])
#           print type(bug_id)
           #对每个bug_id 进行等级分析#
           buglevel_cn=buglevel_data[(buglevel_data['fx_bugid'] == bug_id)]['fx_bugid'].count()
           buglevel_cn1=buglevel_data[(buglevel_data['fx_bugid'] == bug_id) & (buglevel_data['fx_level_id'] == 1)]['fx_bugid'].count()
           buglevel_cn2=buglevel_data[(buglevel_data['fx_bugid'] == bug_id) & (buglevel_data['fx_level_id'] == 2)]['fx_bugid'].count()
           buglevel_cn3=buglevel_data[(buglevel_data['fx_bugid'] == bug_id) & (buglevel_data['fx_level_id'] == 3)]['fx_bugid'].count()
           buglevel_cn4=buglevel_data[(buglevel_data['fx_bugid'] == bug_id) & (buglevel_data['fx_level_id'] == 4)]['fx_bugid'].count()
#           print "###########################################"
#           print bug_id,buglevel_cn1,buglevel_cn2,buglevel_cn3,buglevel_cn4,buglevel_cn
#           print format(float(buglevel_cn1)/float(buglevel_cn)* 100,'.2f')
#           print format(float(buglevel_cn2)/float(buglevel_cn)* 80,'.2f')
#           print format(float(buglevel_cn3)/float(buglevel_cn)* 40,'.2f')
#           print format(float(buglevel_cn4)/float(buglevel_cn)* 10,'.2f')
#           print "######################################"
           bug1=float(format(float(buglevel_cn1)/float(buglevel_cn)* 500,'.2f'))
           bug2=float(format(float(buglevel_cn2)/float(buglevel_cn)* 70,'.2f'))
           bug3=float(format(float(buglevel_cn3)/float(buglevel_cn)* 30,'.2f'))
           bug4=float(format(float(buglevel_cn4)/float(buglevel_cn)* 400,'.2f'))
           bugformat=pd.DataFrame({'level_id':[1,2,3,4],'level_idcont':[bug1,bug2,bug3,bug4]})
           
           #,ascending=False  降序
           bugorder=bugformat.sort_index(by=['level_idcont'],ascending=False)
#           order1=bugorder.iloc[0,1]
#           order2=bugorder.iloc[1,1]
#           print order2,order1
#           if order1 == order2:
#               levelid=bugorder.iloc[1,0]
#               print levelid
#           else:
#               levelid=bugorder.iloc[0,0]
#               print levelid
#           print "######################################"
#           order1=bugorder.iloc[0,1]
           levelid=bugorder.iloc[0,0]
#           print levelid,order1,bug_id
           print "######################################"
           print bugorder

           #对 每个bug_id 进行标签分析
	   bug_tagname=''
           bug_bugid=buglevel_data[(buglevel_data['fx_bugid'] == bug_id) & (buglevel_data['fx_level_id'] == levelid)  & (buglevel_data['fx_priority'] == 1)]
           bugid_priority_cn=bug_bugid['fx_bugid'].count()
           print "优先级为1的个数###############################################"
           print bugid_priority_cn 
           #tag_name 优先拿优先级高的
           if bugid_priority_cn > 0:
#               print bug_bugid
               bug_tagname=bug_bugid.iloc[0,4]
               print "优先级###############################################"
               print bug_tagname.encode('utf-8')
           else:
               bug_bugid=buglevel_data[(buglevel_data['fx_bugid'] == bug_id) & (buglevel_data['fx_level_id'] == levelid)]
               bugid_tagname_distinct = bug_bugid.drop_duplicates(['fx_tag_name'])
               bugid_tagname_cn=bugid_tagname_distinct['fx_bugid'].count()
               print "###########bug对应分类信息，再筛选###################################################"
	       print bugid_tagname_distinct
               tagname_cn=0
               for z in range(bugid_tagname_cn):
                      bug_tagname1=bugid_tagname_distinct.iloc[z,4]
                      tagname_cn1=int(bug_bugid[(bug_bugid['fx_tag_name'] == bug_tagname1)]['fx_tag_name'].count())
                      print bug_tagname1.encode('utf-8')
                      print tagname_cn1
    
                      if tagname_cn1 > tagname_cn:
                               bug_tagname=bug_tagname1
                               tagname_cn=tagname_cn1
                      if tagname_cn1 == tagname_cn  and bug_tagname != bug_tagname1:
                               if bug_tagname =='':
                                   bug_tagname=bug_tagname1
                               else:
                                   bug_tagname=bug_tagname+','+bug_tagname1
                               tagname_cn=tagname_cn1
           print "#####筛选完毕#################################"                 
           print levelid,bug_tagname.encode('utf-8'),bug_id
           print "#####结束#################################"

           db.fx_buglevel_update(levelid,bug_tagname,bug_id)
def project_stat():
    db=fenxi_mysql.dbmysql()
    objectid=''
    ####今天
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    ##昨天
    date1=datetime.datetime.now()+datetime.timedelta(days=-1)
    date1=date1.strftime("%Y-%m-%d")
    ##前天
    date2=datetime.datetime.now()+datetime.timedelta(days=-2)
    date2=date2.strftime("%Y-%m-%d")
    ##今天结束日
    date00=datetime.datetime.now()+datetime.timedelta(days=1)
    date00=date00.strftime("%Y-%m-%d")
    ##昨天结束日
    date11=datetime.datetime.now().strftime("%Y-%m-%d")
    ##前天结束日
    date22=datetime.datetime.now()+datetime.timedelta(days=-1)
    date22=date22.strftime("%Y-%m-%d")
    #判断是否为工作日,工作日返回true，非工作日返回false
    cal = Calendar()
    if cal.isbusday(date)==True:
        if cal.isbusday(date1)==False or cal.isbusday(date2)==False:
            d1=0
            d2=0
            while cal.isbusday(date1)==False:
                d1=d1+1
                days1=-1-d1
                date1=datetime.datetime.now()+datetime.timedelta(days=days1)
                date11=date1+datetime.timedelta(days=1)
                date1=date1.strftime("%Y-%m-%d")
                date11=date11.strftime("%Y-%m-%d")
            while cal.isbusday(date2)==False :
                d2=d2+1
                days2=-2-d2
                date2=datetime.datetime.now()+datetime.timedelta(days=days2)
                date22=date2+datetime.timedelta(days=1)
                date2=date2.strftime("%Y-%m-%d")
                date22=date22.strftime("%Y-%m-%d")
                if date1 == date2:
                    d2=d2+1
                    days2=-2-d2
                    date2=datetime.datetime.now()+datetime.timedelta(days=days2)
                    date22=date2+datetime.timedelta(days=1)
                    date2=date2.strftime("%Y-%m-%d")
                    date22=date22.strftime("%Y-%m-%d")
    
        print date,date1,date2 
        print date00,date11,date22
    
    ##############################################################################
        objectid=db.object_id_sel()
        objectid_cn=len(objectid)
        i=1
#        status=1
        for i in range(objectid_cn):
            obid=objectid[i][0]
            #今天bug数
            td=int(db.bug_objectid_sel(obid,date,date00)[0])
            #昨天bug数
            zt=int(db.bug_objectid_sel(obid,date1,date11)[0])
            #前天bug数
            qt=int(db.bug_objectid_sel(obid,date2,date22)[0])
            pro_stat=db.project_stat_sel(obid,'0')
            status=int(pro_stat[0])
            stardate=pro_stat[1]
            ##今天有bug
            if td >0:
                print obid
                print td,zt,qt
                #项目进行中
                if status == 1:
                    if zt ==0 and qt ==0:
                        total=int(db.bug_objectid_sel(obid,stardate,date2)[0])
                        jk_total=int(db.jenkins_source_sel(obid,stardate,date2)[0])
                        db.project_stat_update(total,jk_total,date2,'1',obid,'0')
                        print "如果项目进行中，今天无bug,更改项目状态为：结束"
 
                #项目结束        
                if status ==0:
                    bugcn=td-zt
                    if bugcn >= 1:
			obname=db.object_name_sel(obid) 
                        proname=obname[0]+str(date)
                        db.project_stat_save(proname,obid,date,'0')
            #            print obname[0],bugcn
            #今天无bug         
            else:
                #项目进行中
                if status == 1:                    
                    if zt ==0:
                        total=int(db.bug_objectid_sel(obid,stardate,date1)[0])
                        jk_total=int(db.jenkins_source_sel(obid,stardate,date1)[0])
                        db.project_stat_update(total,jk_total,date2,'1',obid,'0')
                        print "如果项目进行中，今天无bug,更改项目状态为：结束"
                print obid
                print td,zt,qt
def day_changename_comment_stat(date):
    db=fenxi_mysql.dbmysql()
    ##获取代码注释内容
    com_list=db.change_comment_sel(date)
    ##获取bug信息
    bugname_list=db.fx_sel_bug(date)
    change_name=[]
    object_id=[]
#    bug_name1=''
#    print com_list
    for i in range(len(com_list)):
     #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
        change_name.append(com_list[i][0])
        object_id.append(com_list[i][1])
    change_name_comment=pd.DataFrame({'change_name':change_name,'object_id':object_id})
#    print change_name_comment
    change_name_comment_distinct = change_name_comment.drop_duplicates()  
#    print change_name_comment_distinct
    for i in range(len(change_name_comment_distinct)):
        changename=change_name_comment_distinct.iloc[i,0]
        ob_id=change_name_comment_distinct.iloc[i,1]
        for j in range(len(com_list)):
             if com_list[j][0] == changename and com_list[j][1] == ob_id:
                 comment=com_list[j][2]
                 bug_id_list1=[]
                 sim2=0.6
                 for x in range(len(bugname_list)):
                     if bugname_list[x][1] == '新建' and bugname_list[x][5] !=None:
                         if bugname_list[x][6] !='4' and '前端' not in bugname_list[x][5]:
#                            if '接口' in bugname_list[x][5]:
#                                sim2=0.8
                            bug_name=bugname_list[x][4].replace(" ","").replace("/","").replace(",","").replace(")","").replace("(","")
                            bug_id=bugname_list[x][0].replace(" ","")
                            cm_cn=int(len(comment))
                            bn_cn=int(len(bug_name))
                            tol_cn=bn_cn-cm_cn
                            print "#######################################"
                            print cm_cn,bn_cn,tol_cn
                            if tol_cn <=0:
                                sim2=1
                            if tol_cn >=1 and tol_cn <=cm_cn:
                                sim2=0.8
                            if tol_cn > cm_cn and tol_cn <=cm_cn * 2:
                                sim2=0.6
                            if tol_cn > cm_cn * 2 and tol_cn <=cm_cn * 4:
                                sim2=0.4 
                            print sim2,cm_cn,tol_cn,bug_id,bug_name,comment
                            print "#######################################"
#                            print comment,len(comment)
#                            print bug_name,len(bug_name)
                            sim1=synonyms.compare(comment, bug_name, seg=False)
                            print sim1
                            if sim1 > sim2:
                               sim2 =sim1
                               bug_id_list1.append(bug_id)
                 bug_id_list=str(bug_id_list1).replace("[","").replace("]","").replace("'","").replace("u","")
#                 print changename,ob_id,commnet,bug_id_list
                 db.changename_bugid_save(changename,ob_id,comment,bug_id_list,date)
              
if __name__ == '__main__':
   starttime=datetime.datetime.now()
   date = datetime.date.today()
   date = str(date)
    #print date
   date='2018-01-27'
#   print "--day_bug_level----开始时间--------------",starttime,"---------------------------------"
#   date1=(datetime.datetime.now()+datetime.timedelta(days=-30)).strftime("%Y-%m-%d")
#   day_bug_level(date1)
#   print "--project_stat----开始时间--------------",starttime,"---------------------------------"
#   project_stat()
   print "--day_changename_comment_stat----开始时间--------------",starttime,"---------------------------------"
   day_changename_comment_stat(date)
#   print "---day_commitcode---开始时间--------------",starttime,"---------------------------------"
#   day_commitcode(date)
#   starttime1=datetime.datetime.now()
#   print "----day_changename--开始时间--------------",starttime1,"---------------------------------"
#   day_changename(date)
#   starttime1=datetime.datetime.now()
#   print "---day_changename_bug_probability---开始时间--------------",starttime1,"---------------------------------"
#   day_changename_bug_probability(date)
#   starttime1=datetime.datetime.now()
#   print "--day_changename_topkeyword----开始时间--------------",starttime1,"---------------------------------"
#   day_changename_topkeyword(date)
#   starttime1=datetime.datetime.now()
#   print "--day_changename_bug_level----开始时间--------------",starttime1,"---------------------------------"
#   day_changename_bug_level(date)
#   starttime1=datetime.datetime.now()
   endtime=datetime.datetime.now()
   rtime=(endtime - starttime).seconds
   print "------结束时间-------------",endtime,"------------------------------------"
   print "------运行耗时-------------",rtime,"----------------------------------------"
