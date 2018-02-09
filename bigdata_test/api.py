# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:51:29 2017

@author: Administrator
"""

from flask import Flask,request,json
import db_mysql
import logging
import basic_data

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapi.log',
                filemode='w')
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


app = Flask(__name__)
dic=[]
objectid='test'
commitcode='00000000'
@app.route('/data',methods=['GET','POST'])
def index():
    try:
        if request.method == 'POST':
            a = request.get_data()
#            print a
            dict1 = json.loads(a)
            dic=list(dict1.keys())
 #           logging.info(dic) 
            i=int(len(dict1))
    #        return json.dumps(dict1[dic[i-1]])     ##数组 
    #            
    #        return json.dumps(dict1["file:/ts/inke.ts"])
            j=0
            t=0
            change=[]
            name=[]
            date=""
            db=db_mysql.dbmysql()
            if "objectID" in dict1.keys():
                objectid= dict1["objectID"] 
            if "commentID" in dict1.keys():
                commitcode= dict1["commentID"] 
            if "time" in dict1.keys():
                date= dict1["time"]
            for j in range(i):
                if dic[j]!="time" and dic[j]!="objectID" and dic[j]!="commentID":
                    change.append(dict1[dic[j]])
                    name.append(dic[j])
                    #print date,change[t],name[t]
                    change1=str(change[t])
                    name1=str(name[t])
                    db.save(objectid,date[0],change1,name1,commitcode)
#                    print "#################"
#                    print objectid[0],name[t]
                    changename_level_cn=db.changename_level_sel(objectid,name1)
#                    print "changename_level_cn",int(changename_level_cn[0])
                    if int(changename_level_cn[0]) > 0:
                       objectid1=basic_data.basic_project1(objectid[0])
                       message="近90天bug严重的程序：子项目名称："+objectid1+",程序名："+name1+"， 有更新"
                       logging.info(message)
                    t=t+1
            return json.dumps("ok") 
        else:
            return '请发POST'
    except :
        logging.error("error message") 
 
     
if __name__ == '__main__':
    app.run(host = '0.0.0.0',
        port = 6002,  
        debug = True )