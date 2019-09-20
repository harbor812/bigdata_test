# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:43:16 2019

@author: Brianzhu
"""

#from hdfs import Client
#
#import pandas as pd
#
# 
#
#HDFSHOST = "http://192.168.120.160:50070"
#
#FILENAME = "/user/spark/parquet/douyin/comment/plat=201/group=999/part-00146-6e90e3d2-443f-42e0-acd2-5487774966c6.c000.snappy.parquet" #hdfs文件路径
#
#COLUMNNAMES = ['platform_id','cid','video_id','location','context','reply_id','constellation','context_digg_count','from_name','gender','from_id','context_create_time','birthday','room_id']
#
#
#client = Client(HDFSHOST)
#
## 目前读取hdfs文件采用方式：
#
## 1. 先从hdfs读取二进制数据流文件
#
## 2. 将二进制文件另存为.csv
#
## 3. 使用pandas读取csv文件
#
#with client.read(FILENAME) as fs:
#    content = fs.read()
#s = str(content, 'utf-8')
#file = open("D:\data.csv", "w")
#file.write(s)
#df = pd.read_csv("D:\data.csv", names=COLUMNNAMES)
#print df



import parquet
import json

## assuming parquet file with two rows and three columns:
## foo bar baz
## 1   2   3
## 4   5   6

with open("test.parquet") as fo:
   # prints:
   # {"foo": 1, "bar": 2}
   # {"foo": 4, "bar": 5}
   for row in parquet.DictReader(fo, columns=['foo', 'bar']):
       print(json.dumps(row))


with open("test.parquet") as fo:
   # prints:
   # 1,2
   # 4,5
   for row in parquet.reader(fo, columns=['foo', 'bar]):
       print(",".join([str(r) for r in row]))