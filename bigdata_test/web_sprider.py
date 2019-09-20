# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:29:17 2017

@author: Brianzhu
"""

#import re
import urllib2,re,time,datetime
import json
from ntlm import HTTPNtlmAuthHandler
import logging
from cookielib import CookieJar
import db_mysql,basic_data,chandao_mysql


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='web_sprider.log',
                filemode='w')
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def get_message(): 
    try:
        #获取token###############################################################
        user = 'BRIANZHU-PC\weigangzhu'   
        password = "123qwe"   
        url = "http://180.166.104.154:18080/tfs/"   
           
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()   
        passman.add_password(None, url, user, password)   
        # create the NTLM authentication handler   
        auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)   
           
        # create and install the opener   
        opener = urllib2.build_opener(auth_NTLM)   
        urllib2.install_opener(opener)   
#        response = urllib2.urlopen(url).read()
#        print opener
#        response = opener.open(url).read()

        ###############################################################################

        html=[]
        #大数据
#        html.append("http://180.166.104.154:18080/tfs/DefaultCollection/baa53168-8d92-4fa2-aada-020a50f4244c/2ca57eaf-de46-41d8-a039-dc771c14373f/_api/_backlog/GetBoard?__v=5&hubCategoryReferenceName=Microsoft.RequirementCategory")
        #泡面番
#        html.append("http://180.166.104.154:18080/tfs/DefaultCollection/baa53168-8d92-4fa2-aada-020a50f4244c/c43eae63-58c2-494d-9640-f52d5ebdaf69/_api/_backlog/GetBoard?__v=5&hubCategoryReferenceName=Microsoft.RequirementCategory")
        #区块链
        html.append("http://180.166.104.154:18080/tfs/DefaultCollection/baa53168-8d92-4fa2-aada-020a50f4244c/3d4f1612-335f-4985-9d16-1f212d66a385/_api/_backlog/GetBoard?__v=5&hubCategoryReferenceName=Microsoft.RequirementCategory")
        htcn=len(html)
        for x in range(htcn):
            dict1=json.loads(urllib2.urlopen(html[x]).read())
#            dict1=json.loads(opener.open(html[x]).read())
            to_mysql(dict1)
            logging.info("执行完毕：%s"%html[x])     
    except urllib2.HTTPError as e:
        logging.error(e.code)
        logging.error(e.reason)
        
def to_mysql(dict1):
#    dic=list(dict1.keys())

#    print json.dumps(object2)
    try:
        title=''
        dt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        if "itemSource" in dict1.keys():
    #        global title
            objectid=dict1["itemSource"]
            objectid1=objectid["payload"]
            objectid2=objectid1["rows"]
            cn1=len(objectid2)
            db=db_mysql.dbmysql()
    #        dt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #        oj33="暂无"
            for j in range(cn1):
                objectid3=objectid2[j]
                            
                if objectid3[5] == "Bug":
    #               print("-----------------------------------------------------")
    #               print objectid3[0] #BUGID
    #               print objectid3[4] #bugname
    #               print objectid3[1].encode("utf-8") #bugstatus
    #               print objectid3[7] #完成时间
    #               print objectid3[3] #完成人
    #               print objectid3[2] #父目录
    #               print objectid3[8] #子目录
    #               print objectid3[6] #创建时间
                   if objectid3[1].encode("utf-8") == "新建":
                       c_user=objectid3[15].split("<")[0]                   
    #                   print objectid3[15].split("<")[0] #创建时间
                   else: 
                       c_user=objectid3[3]                   
    #                   print objectid3[3] #创建时间
    #               title=0
                   ob38=objectid3[8].split("\\")
                   obj7=str(objectid3[7])
                   obj6=str(objectid3[6])
                   obj34=objectid3[4].encode("utf-8")
                   sub_type=basic_data.basic_project(obj34)
#                   print objectid3[0],obj34,sub_type
#    #               print ob38[1]
#    #               print sub_type
                   if obj7 !='None': ##获取完成时间并且把时间戳格式化成date
                      token=str(re.findall(r'\d+\.?\d',obj7,re.S)) 
                      timestamp=int(token[2:12])
                      time_local = time.localtime(timestamp)
                      dt = str(time.strftime("%Y-%m-%d %H:%M:%S",time_local))
    #                  print "完成时间显示 转换前：%s,转换后：%s"%(obj7,dt)
                   if obj7 =='None' and obj6 !='None': ##获取完成时间并且把时间戳格式化成date
                      token=str(re.findall(r'\d+\.?\d',obj6,re.S)) 
                      timestamp=int(token[2:12])
                      time_local = time.localtime(timestamp)
                      dt = str(time.strftime("%Y-%m-%d %H:%M:%S",time_local))
    #                  print "创建时间显示 转换前：%s,转换后：%s"%(obj6,d
                   if "（线上）" in obj34:
                       is_miss=1
                   else:
                       is_miss=0
                   if ")" in obj34:
                       bugname1=obj34.split(")")
                       title1=bugname1[0].split("(")
                       title=title1[1]
                       bugname2=bugname1[1].split("(")
                       bugname=bugname2[0]
                   elif "）" in obj34:
                       bugname1=obj34.split("）")
                       title1=bugname1[0].split("（")
                       title=title1[0]
                       bugname2=bugname1[1].split("(")
                       bugname=bugname2[0]
                   elif "】" in obj34:
                       bugname1=obj34.split("】")
    #                   title1=bugname1[0].split("(")
    #                   title=title1[0]
                       bugname2=bugname1[1].split("(")
                       bugname=bugname2[0] 
                   else:
                       bugname=obj34
    #               print "#############################"
#                   print title,bugname1[0],title1[1]
#    #               print "#############################"
#    #               print bugname
#    #               print objectid3[0],bugname,objectid3[1],dt,c_user],ob38[1],sub_type,is_miss
                   cn=db.bug_sel(objectid3[0],objectid3[1])
    #               print cn
                   cn=int(cn[0])
                   if cn == 0:
                        sub_type=basic_data.basic_project(title)
                        db.bug_save(objectid3[0],bugname,objectid3[1],dt,c_user,ob38[1],sub_type,is_miss,title)

    except UnboundLocalError,e:
            print e        
def day_bug_level(date):
    db=db_mysql.dbmysql()
    bug_level=db.bug_levelwords_sel()
    bug_level_cn=len(bug_level)
#    level_id=[]
#    object_id=[]
#    level_word=[]
#    print bug_level
    for x in range(bug_level_cn):
        object_id=bug_level[x][0]
        level_word=bug_level[x][1].encode('utf-8')
        level_id=bug_level[x][2] 
        print level_id,level_word
        db.buglevel_update(object_id,level_id,level_word,date)

def zentao_get_message(date):
    try:
        db1=chandao_mysql.zd_dbmysql()
        db=db_mysql.dbmysql()
        bug_list=db1.bug_sel(date)
        print bug_list
        sub_type=99
        title=''
        type='应用中心系统'
        for i in range(len(bug_list)):            
            if   bug_list[i][10]==1:
                 sub_type=25
            if   bug_list[i][10]==3:
                 sub_type=26
    #        print bug_list[i][0],bug_list[i][1],bug_list[i][2],bug_list[i][3],bug_list[i][4]
            print "##################################################"
            if   bug_list[i][2]=='active':
                 bug_status='新建'
            if   bug_list[i][2]=='resolved':
                 bug_status='已提交'
            if   bug_list[i][2]=='closed':
                 bug_status='完成'
            date=str(bug_list[i][3])
            cn=db.bug_sel_tandao(bug_list[i][0],bug_status,sub_type,date)
            cn=int(cn[0])
            if cn == 0:
               obj34=bug_list[i][1].encode('utf-8')
               if "（线上）" in obj34:
                       is_miss=1
               else:
                       is_miss=0
            if ")" in obj34:
               bugname1=obj34.split(")")
               title1=bugname1[0].split("(")
               title=title1[1]
               bugname2=bugname1[1].split("(")
               bugname=bugname2[0]
            elif "）" in obj34:
               bugname1=obj34.split("）")
#                   title1=bugname1[0].split("(")
#                   title=title1[0]
               bugname2=bugname1[1].split("(")
               bugname=bugname2[0]
            elif "】" in obj34:
               bugname1=obj34.split("】")
#                   title1=bugname1[0].split("(")
#                   title=title1[0]
               bugname2=bugname1[1].split("(")
               bugname=bugname2[0] 
            else:
               bugname=obj34
    #           date=str(bug_list[i][3])
               if bug_status=='新建':
                    user_name=bug_list[i][5].encode('utf-8')
                    date1=bug_list[i][7]
               elif bug_status=='已提交':
                    user_name=bug_list[i][4].encode('utf-8')
                    date1=bug_list[i][8]
    
               elif bug_status=='完成':
                    user_name=bug_list[i][6].encode('utf-8')
                    date1=bug_list[i][9]
               else:
                    user_name=''
                    date1=date
               print bug_list[i][0],bugname,bug_status,date1,user_name,type,sub_type,is_miss
               db.bug_save(bug_list[i][0],bugname,bug_status,date1,user_name,type,sub_type,is_miss,title)   
    except UnboundLocalError,e:
            print e                   
if __name__ == '__main__':
#    date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        date=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
        print date
    #    print date
        date='2019-03-25 01:06:37'
        get_message()
#        zentao_get_message(date)
    #    day_bug_level(date)

        