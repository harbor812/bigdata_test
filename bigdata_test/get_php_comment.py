# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:27:28 2018

@author: Brianzhu
"""

import paramiko
import datetime
import db_mysql


def exec_command(comm):
#    starttime = datetime.datetime.now()
#    print (comm,starttime)
    rs=[]
    username = 'root'
    password = 'qa334455@QA'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('113.107.160.93',22,username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(comm)
    result = stdout.readlines()
    ssh.close()
    # print ("###########查询结果######################")
    if len(result)==0:
        result=0
        return result
#    print (len(result))
    for i in range(len(result)):
#         print result[i]
        if ' * ' in result[i]:
            rs1=result[i].split("*")
            if rs1[1].strip() !='':                
               rs.append(rs1[1].strip())
        if 'function' in result[i]:
            rs1=result[i].split("function")
            rs2=rs1[1].split("(")
            if rs2[0].strip() !='':
                rs.append(rs2[0].strip())

    result=rs  
    return result

def to_mysql(comm,ob_id,comm1):
    comm2=comm.split(":")[1]
    if ob_id == 21:
        comm3='cat /work/www/html/xq.xiaohulu.com'+comm2
        result=exec_command(comm3)
#        print result
        if result !=0:
            db.change_comment_del(comm,ob_id)
            for i in range(len(result)):
                  if result[i] !='' and result[i] !='Class Host' and  '@' not in result[i] and '$' not in result[i] and '(' not in result[i] and ';' not in result[i] and ':' not in result[i] and 'To change' not in result[i] and 'Description' not in result[i] and 'and open' not in result[i] and 'data params' not in result[i]:
                      print comm,result[i],ob_id
                      db.change_comment_insert(comm,ob_id,result[i])
            print comm,comm1,ob_id
            db.change_comment_insert(comm,ob_id,comm1)
            
    if ob_id==30:
        comm3='cat /work/www/html/mpxq.xiaohulu.com'+comm2
        result=exec_command(comm3)
#        print result
        if result !=0:
            db.change_comment_del(comm,ob_id)
            for i in range(len(result)):
                  if result[i] !='' and result[i] !='Class Host' and  '@' not in result[i] and '$' not in result[i] and '(' not in result[i] and ';' not in result[i] and ':' not in result[i] and 'To change' not in result[i] and 'Description' not in result[i] and 'and open' not in result[i] and 'data params' not in result[i]:
                      print comm,result[i],ob_id
                      db.change_comment_insert(comm,ob_id,result[i])
            print comm,comm1,ob_id
            db.change_comment_insert(comm,ob_id,comm1)

if __name__ == '__main__':
    db=db_mysql.dbmysql()
    starttime = datetime.datetime.now().strftime("%Y-%m-%d")
    endtime=datetime.datetime.now()+datetime.timedelta(days=1)
    endtime=endtime.strftime("%Y-%m-%d")
    starttime ='2018-08-01'
    endtime='2018-08-02'
    jk_source=db.change_name_sel(starttime,endtime)
#    print jk_source
    for i in range(len(jk_source)): 
        if ".php" in  jk_source[i][0] or ".js" in  jk_source[i][0]:          
            comm=jk_source[i][0]
            comm1=comm.split("/")[-1]
            comm1=comm1.split(".")[0]
            ob_id=int(jk_source[i][1])
#            print comm,ob_id,comm1
            to_mysql(comm,ob_id,comm1)
#    print starttime,endtime
