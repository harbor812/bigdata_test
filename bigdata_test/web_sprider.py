# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:29:17 2017

@author: Brianzhu
"""

#import re
import urllib2,re,time
import json
from ntlm import HTTPNtlmAuthHandler
import logging
from cookielib import CookieJar
import db_mysql,basic_data


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
        url = "http://124.74.40.26:18080/tfs/"   
           
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()   
        passman.add_password(None, url, user, password)   
        # create the NTLM authentication handler   
        auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)   
           
        # create and install the opener   
        opener = urllib2.build_opener(auth_NTLM)   
        urllib2.install_opener(opener)   
#        response = urllib2.urlopen(url).read()
#        response = opener.open(url).read()

        ###############################################################################

        html=[]
        #大数据
        html.append("http://124.74.40.26:18080/tfs/DefaultCollection/baa53168-8d92-4fa2-aada-020a50f4244c/2ca57eaf-de46-41d8-a039-dc771c14373f/_api/_backlog/GetBoard?__v=5&hubCategoryReferenceName=Microsoft.RequirementCategory")
        #泡面番
        html.append("http://124.74.40.26:18080/tfs/DefaultCollection/baa53168-8d92-4fa2-aada-020a50f4244c/c43eae63-58c2-494d-9640-f52d5ebdaf69/_api/_backlog/GetBoard?__v=5&hubCategoryReferenceName=Microsoft.RequirementCategory")
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

    if "itemSource" in dict1.keys():
        objectid=dict1["itemSource"]
        objectid1=objectid["payload"]
        objectid2=objectid1["rows"]
        cn1=len(objectid2)
        db=db_mysql.dbmysql()
        dt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print dt
#        oj33="暂无"
        for j in range(cn1):
            objectid3=objectid2[j]            
            if objectid3[5] == "Bug":
#               print("-----------------------------------------------------")
#               print objectid3[0] #BUGID
#               print objectid3[4] #bugname
#               print objectid3[1] #bugstatus
#               print objectid3[7] #完成时间
#               print objectid3[3] #完成人
#               print objectid3[2] 
#               print objectid3[8] 
               ob38=objectid3[8].split("\\")               
               obj7=str(objectid3[7])
               obj34=objectid3[4].encode("utf-8")
               sub_type=basic_data.basic_project(obj34)
               if obj7 !='None': ##获取完成时间并且把时间戳格式化成date
                  token=str(re.findall(r'\d+\.?\d',obj7,re.S)) 
                  timestamp=int(token[2:12])
                  time_local = time.localtime(timestamp)
                  dt = str(time.strftime("%Y-%m-%d %H:%M:%S",time_local))
                  #print "时间显示 转换前：%s,转换后：%s"%(obj7,dt)
            cn=db.bug_sel(objectid3[0],objectid3[1])
            cn=int(cn[0])
            if cn == 0:
                db.bug_save(objectid3[0],objectid3[4],objectid3[1],dt,objectid3[3],ob38[1],sub_type)


                                        
if __name__ == '__main__':
    get_message()