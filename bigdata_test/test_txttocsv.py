# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:07:00 2019

@author: Brianzhu
"""

import csv
fh = open(r'text\中国天气网城市代码.csv',"w+",newline='')
writer = csv.writer(fh)
writer.writerow(["城市代码","城市名称"])
data = open(r'text\中国天气网城市代码.txt')
res = []
for i in data:
    d = [x for x in i.strip().split('=')]
    res.append(d)
print(res)
writer.writerows(res)
data.close()
fh.close()
