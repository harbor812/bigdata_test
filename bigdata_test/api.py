# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:51:29 2017

@author: Administrator
"""

from flask import Flask,request,json
from db_mysql import save
app = Flask(__name__)
dic=[]
objectid='test'
commitcode='00000000'
@app.route('/data',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        a = request.get_data()
        dict1 = json.loads(a)
        dic=list(dict1.keys())
        i=int(len(dict1))
#        return json.dumps(dic[i-1]) ##更新文件名
#        return json.dumps(dict1[dic[i-1]])     ##数组 
            
#        return json.dumps(dict1["file:/ts/inke.ts"])
        j=0
        t=0
        change=[]
        name=[]
        date=""
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
                save(objectid,date[0],change1,name[t],commitcode)
                t=t+1
        return json.dumps("ok") 
    else:
        return '<h1>请发POST</h1>'

if __name__ == '__main__':
    app.run(host = '0.0.0.0',
        port = 6002,  
        debug = True )

