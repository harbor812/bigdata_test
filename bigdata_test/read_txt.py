# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 13:59:13 2018

@author: Brianzhu
"""


f=open(r"D:\git\bigdata_test\bigdata_test\redis_config.txt","r")
line=f.readline()
data=[]

while line:
    data.append(line)
    line=f.readline()



#data=dict(data)
print data