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
    try:
        db=fenxi_mysql.dbmysql()
        ob_data=[]
        fx_bugid=[]
        fx_bugstatus=[]
        fx_bugsub_type=[]
        fx_bugdate=[]
        fx_jk=db.fx_sel_jenkins(date)
        fx_bug=db.fx_sel_bug(date)
        bug_close_id=''
        bug_new_id=''
        bug_fix_id=''
        datetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    
    #    assert fx_bug !=0
        cn=len(fx_jk)
        cn_bug=len(fx_bug)
        for i in range(cn):
         #   print fx_jk[i][1],type(fx_jk[i][1].encode('utf-8'))
            ob_data.append(fx_jk[i][1].encode('utf-8'))
        ob_data=pd.DataFrame({'ob_data':ob_data})
        print ob_data
        ob_data_distinct = ob_data.drop_duplicates() 
        
        cn1=len(ob_data_distinct)
        
        #所有BUG数据变为list
        for x in range(cn_bug):
    
    #          if  fx_bug[x][1].encode('utf-8') == '完成':
        #              print fx_jk[j][1]
                      fx_bugid.append(fx_bug[x][0].encode('utf-8'))
                      fx_bugstatus.append(fx_bug[x][1].encode('utf-8'))
                      fx_bugsub_type.append(fx_bug[x][2].encode('utf-8'))
                      fx_bugdate.append(str(fx_bug[x][3])) 
    
    
        bug_data=pd.DataFrame({'fx_bugid':fx_bugid,'fx_bugstatus':fx_bugstatus,'fx_bugsub_type':fx_bugsub_type,'fx_bugdate':fx_bugdate})
        bug_data_cn=bug_data["fx_bugid"].count()
        
        
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
              ob_id=type_data[x]
              print '############################################'
              print startdate,enddate,ob_id
    
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
              bug_data_cn=int(bug_data_cn)
              #选取和统计bug数
              if bug_data_cn > 0:
    #              print "bug 数量：",bug_data_cn
                  bug_data1=bug_data[(bug_data['fx_bugdate'] >=startdate) & (bug_data['fx_bugdate'] < enddate) & (bug_data['fx_bugsub_type'] == ob_id)]
                  #if bug_data1["fx_bugid"].count() != '0':            
                  bug_close_cn=bug_data1[bug_data1['fx_bugstatus'].str.contains('完成')].count()
                  bug_new_cn=bug_data1[bug_data1['fx_bugstatus'].str.contains('新建')].count()
                  bug_fix_cn=bug_data1[bug_data1['fx_bugstatus'].str.contains('已提交')].count()
                  bug_new=bug_new_cn['fx_bugid']
                  bug_fix=bug_fix_cn['fx_bugid']
                  bug_close=bug_close_cn['fx_bugid']
                  
                  if bug_close !='0':
                      bugid_close=bug_data1[bug_data1['fx_bugstatus'].str.contains('完成')]
                      bug_close_id=str(list(bugid_close['fx_bugid'])).replace("[","").replace("]","").replace("'","")
                  if bug_new !='0':
                      bugid_new=bug_data1[bug_data1['fx_bugstatus'].str.contains('新建')]
                      bug_new_id=str(list(bugid_new['fx_bugid'])).replace("[","").replace("]","").replace("'","")
                  if bug_fix !='0':
                      bugid_fix=bug_data1[bug_data1['fx_bugstatus'].str.contains('已提交')]
                      bug_fix_id=str(list(bugid_fix['fx_bugid'])).replace("[","").replace("]","").replace("'","")
                      
              db.fx_changename_save(ob_data,ob_id,startdate,enddate,bug_new,bug_fix,bug_close,date,add_count,del_count,bug_new_id,bug_fix_id,bug_close_id)
    except UnboundLocalError,e:
            print e
        
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
    print fx_change_name1_distinct  
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
        if changename_data == 'file:/VideoServer/src/main/java/xiaohulu/dao/LiveShowSqlDao.java':
           print  changename_data1['fx_add_count']
           print '#####################################'
           print changename_data1['fx_add_count'].sum()
           print '####################################'
           print add_count,del_count,result_count
           print '####################################'
        if result_count == 0:
            if new_bug_count >= 0 and new_bug_count <= 5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻1",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)
            if new_bug_count >5 and new_bug_count <= 10:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中1",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                
            if new_bug_count >10:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重1",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                
                
#            break
        if (result_count > 0 and result_count <= 20) or (result_count < 0 and result_count >= -20):
            if new_bug_count >= 0 and new_bug_count <= 5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻2",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)
            if new_bug_count >5 and new_bug_count <= 10:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中2",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                                
            if new_bug_count >10:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重2",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                
                
#            break
        if (result_count > 20 and result_count <= 100) or (result_count < -20 and result_count >= -100):
            if new_bug_count >= 0 and new_bug_count <= 5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻3",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)                
            if new_bug_count >5 and new_bug_count <= 15:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中3",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                                
            if new_bug_count >15:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重3",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                                
#            break
        if  result_count > 100  or result_count < -100:
            if new_bug_count >= 0 and new_bug_count <= 5:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻4",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"轻",date)                
            if new_bug_count >5 and new_bug_count <= 20:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中4",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"中",date)                                
            if new_bug_count >20:
#                print changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重4",date
                db.fx_changename_level_save(changename_data,object_id,add_count,del_count,result_count,new_bug_count,"重",date)                
                
#            break
                     
if __name__ == '__main__':
   starttime=datetime.datetime.now()
    #
#   date = datetime.date.today()
#   date = str(date)+' 23:00:00'
#   print date
   date='2017-09-27'
   print "---day_commitcode---开始时间--------------",starttime,"---------------------------------"
   day_commitcode(date)
   print "----day_changename--开始时间--------------",starttime,"---------------------------------"
   day_changename(date)
   print "---day_changename_bug_probability---开始时间--------------",starttime,"---------------------------------"
   day_changename_bug_probability(date)
   print "--day_changename_topkeyword----开始时间--------------",starttime,"---------------------------------"
   day_changename_topkeyword(date)
   print "--day_changename_bug_level----开始时间--------------",starttime,"---------------------------------"
   day_changename_bug_level(date)
   endtime=datetime.datetime.now()
#   endtime=datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
   print endtime
#   rtime=(endtime - starttime).seconds
   if starttime > endtime:
       rtime=endtime - starttime
       print "------结束时间-------------",endtime,"------------------------------------"
       print "------运行耗时-------------",rtime,"----------------------------------------"
    #:print rtime 
