# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:27:28 2018

@author: Brianzhu
"""

import paramiko
import datetime
import db_mysql,db_redis
import json


class get_php(object):
    
    db=db_mysql.dbmysql()
    dbr=db_redis.dbredis()
    
    def exec_command(self,comm):
    #    starttime = datetime.datetime.now()
    #    print (comm,starttime)
        rs=[[] for i in range(7)]
    
        username = 'root'
        password = 'qa334455@QA'
    
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('113.107.160.93',22,username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(comm)
        result = stdout.readlines()
        ssh.close()
        result_cn=len(result)
        # print ("###########查询结果######################")
        if result_cn==0:
            result=0
            return result
    #    print (len(result))
        for i in range(result_cn):
            if_cn=0
            for_cn=0
            switch_cn=0
            while_cn=0
            j=0
    #         print result[i]
            if ' * ' in result[i]:
                rs1=result[i].split("*")
                if rs1[1] !='':                
                   rs[0].append(rs1[1].strip())
                   rs[1].append(i)
                   rs[2].append('0')
                   rs[3].append(if_cn)
                   rs[4].append(for_cn)
                   rs[5].append(switch_cn)
                   rs[6].append(while_cn)
            if 'function' in result[i]:
                rs1=result[i].split("function")
                rs2=rs1[1].split("(")
                j=i
                if rs2[0] !='' and i !=result_cn:
                  while True:
    #                  print "jin"
                      result1=result[j].replace(' ','')
                      if 'if(' in result1 and '//' not in result1:
                          if_cn=if_cn+1
                      if  ('for(' in result1 or 'foreach(' in result1) and '//' not in result1 and '/*' not in result1:
                          for_cn=for_cn+1
                      if 'switch(' in result1 and '//' not in result1 and '/*' not in result1:
                          switch_cn=switch_cn+1
                      if 'while(' in result1 and '//' not in result1 and '/*' not in result1:
                          while_cn=while_cn+1
                      j=j+1
                      if j == result_cn:
                          break
                      if 'function' in result[j]:
                          break
                print if_cn,for_cn,switch_cn,while_cn
                rs[0].append(rs2[0].strip())
                rs[1].append(i)
                rs[2].append('1')
                rs[3].append(if_cn)
                rs[4].append(for_cn)
                rs[5].append(switch_cn)
                rs[6].append(while_cn)
    
    #    if rs !=[[], []]:
        result=rs
        return result

    def to_mysql(self,comm,ob_id,comm1,date):
        comm2=comm.split(":")[1]
        i=0
        print "#############################################"
        if ob_id == 21:
            comm3='cat /work/www/html/xq.xiaohulu.com'+comm2
            result=self.exec_command(comm3)
    #        if result !=[[], []] and result !=0:
    ##            print result
    ###        ss=result[0]
    ###        if ss != '':
    #          for i in range(len(result[0])):
    #            print result[0][i]
    #            print result[1][i]
            if result !=[[], []] and result !=0:
                self.db.change_comment_del(comm,ob_id)
    #            print len(result)
                for i in range(len(result[0])):
    #                print result[i][0]
                      if result[0][i] !='' and result[0][i] !='Class Host' and  '@' not in result[0][i] and '$' not in result[0][i] and '(' not in result[0][i] and ';' not in result[0][i] and ':' not in result[0][i] and 'To change' not in result[0][i] and 'Description' not in result[0][i] and 'and open' not in result[0][i] and 'data params' not in result[0][i] and 'Created by PhpStorm' not in result[0][i] and '?' not in result[0][i] and 'from ' not in result[0][i] and 'FROM ' not in result[0][i]:
    #                      print comm,ob_id,result[i],date,i
                          line_num=int(result[1][i])+1
                          self.db.change_comment_insert(comm,ob_id,result[0][i],date,line_num,result[2][i],result[3][i],result[4][i],result[5][i],result[6][i])
    #            print comm,comm1,ob_id
    #            db.change_comment_insert(comm,ob_id,comm1,date,i)
                
        if ob_id==30:
            comm3='cat /work/www/html/mpxq.xiaohulu.com'+comm2
            result=self.exec_command(comm3)
    #        print result
            if result !=[[], []] and result !=0:
                self.db.change_comment_del(comm,ob_id)
                print len(result)
                for i in range(len(result[0])):
    #                print result[i][0]
                      if result[0][i] !='' and result[0][i] !='Class Host' and  '@' not in result[0][i] and '$' not in result[0][i] and '(' not in result[0][i] and ';' not in result[0][i] and ':' not in result[0][i] and 'To change' not in result[0][i] and 'Description' not in result[0][i] and 'and open' not in result[0][i] and 'data params' not in result[0][i] and 'Created by PhpStorm' not in result[0][i] and '?' not in result[0][i] and 'from ' not in result[0][i] and 'FROM ' not in result[0][i]:
    #                      print comm,ob_id,result[i],date,i
    #                      print comm,ob_id,result[i],date,i
                          line_num=int(result[1][i])+1
                          self.db.change_comment_insert(comm,ob_id,result[0][i],date,line_num,result[2][i],result[3][i],result[4][i],result[5][i],result[6][i])
    #            print comm,comm1,ob_id
    #            db.change_comment_insert(comm,ob_id,comm1,date,i)
    def run_get(self):
        starttime = datetime.datetime.now()+datetime.timedelta(seconds=-60)
        starttime = starttime.strftime("%Y-%m-%d %H:%M:%S")
        
        endtime=datetime.datetime.now()+datetime.timedelta(days=1)
        endtime=endtime.strftime("%Y-%m-%d %H:%M:%S")
    
#        starttime ='2018-08-01'
#        endtime='2018-08-02'
        jk_source=self.db.change_name_sel(starttime,endtime)
    #    print jk_source
        for i in range(len(jk_source)): 
            if ".php" in  jk_source[i][0] or ".js" in  jk_source[i][0]:          
                comm=jk_source[i][0]
                comm1=comm.split("/")[-1]
                comm1=comm1.split(".")[0]
                ob_id=int(jk_source[i][1])
    #            print comm,ob_id,comm1
                self.to_mysql(comm,ob_id,comm1,starttime)
                
    def change_function(self):
        starttime = datetime.datetime.now()+datetime.timedelta(seconds=-120)
        starttime = starttime.strftime("%Y-%m-%d %H:%M:%S")

    
        starttime ='2019-01-18 16:16:08'
#        endtime='2018-08-02'
        jk_source=self.db.bug_sel_commitcode(starttime)
        #获取更新的代码信息
        for j in range(len(jk_source)):
            commitcode=jk_source[j][0]
            objectid=jk_source[j][2]
            changename=jk_source[j][1]
    #        print jk_source[2][0]
    #        print "############################"
    #        print jk_source[2][1]
    #        print "############################"
    #        print jk_source[2][2]
#            print "############################"        
#            print jk_source[j][3]
#            print "############################" 
            change_source=str(jk_source[j][3]).split('\',')
            #对每条更新的内容进行拆解
            for i in range(len(change_source)):
                  #提取增减代码起始行数
                  if 'u\'num:' in change_source[i]:
                      cs_add_comment=0
                      cs_add_line_num=0
                      cs_del_comment=0
                      cs_del_line_num=0
                      cs_num_del=0
                      cs_num_add=0
#                      print change_source[i]
                      cs=change_source[i].split('u\'num:')
                      cs=cs[1].replace('-','').split('+')
                      cs_num=cs[0].split(',')
                      cs_num1=cs[1].split(',')
                      cs_num_del=int(cs_num[0])
                      cs_num_add=int(cs_num1[0])
                      if cs_num_del !=0 and cs_num_del !='':
#                             print cs_num_del
                             cs_del=self.db.change_bugid_limit(objectid,changename,cs_num_del)
                             if cs_del !=None:
                                 cs_del_comment=cs_del[0]
                                 cs_del_line_num=cs_del[1]
                      if cs_num_add !=0 and cs_num_add !='':
                             cs_add=self.db.change_comment_limit(objectid,changename,cs_num_add)
                             if cs_add !=None:
                                 cs_add_comment=cs_add[0]
                                 cs_add_line_num=cs_add[1]
                      print commitcode,objectid,changename,cs_num_del,cs_del_comment,cs_del_line_num,cs_num_add,cs_add_comment,cs_add_line_num,starttime
                      self.db.change_function_insert(commitcode,objectid,changename,cs_num_del,cs_del_comment,cs_del_line_num,cs_num_add,cs_add_comment,cs_add_line_num,starttime)
                  #删除行数 = 增加行数
#                  if cs_num_del == cs_num_add:                      
#                     print "####"+cs_num[0],cs_num1[0]
#                  #删除行数 少于 增加行数   
#                  if cs_num_del < cs_num_add:                      
#                     print cs_num[0],cs_num1[0]
#                  #删除行数 多于  增加行数   
#                  if cs_num_del > cs_num_add:                      
#                     print "___"+cs_num[0],cs_num1[0]
                  
    #    print jk_source
    def change_deladd(self):
        starttime = datetime.datetime.now()+datetime.timedelta(seconds=-180)
        starttime = starttime.strftime("%Y-%m-%d %H:%M:%S")

        starttime ='2019-01-17 16:16:08'
        change_fun=self.db.change_funciotn_sel(starttime)
#        print change_fun
        cn=len(change_fun)
        i=0
        json_1={}
#        json_2={}

        for i in range(cn):
            change_name=change_fun[i][1].split('file:')
            change_name=change_name[1].split('.php')
#            j=","
            if change_fun[i][2] !='0':
                json_1.setdefault("ob_id",[]).append(change_fun[i][0])
                json_1.setdefault("change_name",[]).append(change_name[0])
                json_1.setdefault("comment",[]).append(change_fun[i][2])
#                json_1="{"+"ob_id:" +change_fun[i][0]+", change_name:"+change_name[1] +", comment:"+change_fun[i][2]+"}" + j + json_1
            if change_fun[i][3] !='0':
                json_1.setdefault("ob_id",[]).append(change_fun[i][0])
                json_1.setdefault("change_name",[]).append(change_name[0])
                json_1.setdefault("comment",[]).append(change_fun[i][3])
#                json_1="{"+"ob_id:" +change_fun[i][0]+", change_name:"+change_name[1] +", comment:"+change_fun[i][3]+"}" + j + json_1
#            print json_1
#        json_1=json_1.replace(",","",-1)
        if json_1 !={}:            
            print "###############################"
            json_1=json.dumps(json_1)
            print json_1
            self.dbr.push(json_1)

   
if __name__ == '__main__':
    
    get_php().change_deladd()
#    db=db_mysql.dbmysql()
#    starttime = datetime.datetime.now()+datetime.timedelta(seconds=-300)
#    starttime = starttime.strftime("%Y-%m-%d %H:%M:%S")
#    
#    endtime=datetime.datetime.now()+datetime.timedelta(days=1)
#    endtime=endtime.strftime("%Y-%m-%d %H:%M:%S")
#
#    starttime ='2018-08-01'
#    endtime='2018-08-02'
#    jk_source=db.change_name_sel(starttime,endtime)
##    print jk_source
#    for i in range(len(jk_source)): 
#        if ".php" in  jk_source[i][0] or ".js" in  jk_source[i][0]:          
#            comm=jk_source[i][0]
#            comm1=comm.split("/")[-1]
#            comm1=comm1.split(".")[0]
#            ob_id=int(jk_source[i][1])
##            print comm,ob_id,comm1
#            to_mysql(comm,ob_id,comm1,starttime)
##    print starttime,endtime
