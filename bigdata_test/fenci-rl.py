# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:13:58 2017

@author: Brianzhu
"""

import jieba,nltk
import json
#import pynlpir  
import codecs  
import math  
  
#pynlpir.open()
def cut_sentence(sentence): 
    stopwords = []  
    delstopwords = {}
    strs=jieba.cut(sentence)
    fd=nltk.FreqDist(strs)
    keys=fd.keys()
    item=fd.iteritems()
    dicts=dict(item)
    st = codecs.open('./stopwords.txt', 'rb',encoding='utf-8')  
#    print st
    for line in st:  
        line = line.strip() 
#        print line
        stopwords.append(line)
#        stopwords=str(stopwords).decode("unicode-escape")
#    print (u'正在过滤停用词......')  
  
#    for singletext_result in keys:  
#        delstopwords_singletxt = [] 
#        print singletext_result
#        for word in singletext_result:  
#            #print word
#            word = word.strip()  
#            if word not in stopwords:  
#                if word >= u'\u4e00' and word <= u'\u9fa5':#判断是否是汉字  
#                    delstopwords_singletxt.append(word) 
#        delstopwords_alltxt.append(delstopwords_singletxt)  
#    return delstopwords_alltxt
    #过滤停用词
    for word in keys:  
        word = word.strip()
        if word not in stopwords:  
#            if word >= u'\u4e00' and word <= u'\u9fa5':#判断是否是汉字
                if word in dicts.keys():
                    delstopwords[word]=dicts[word]

    return delstopwords

strs="静静地坐在秋雨绵绵的窗前，任由茶香袅袅，氤氲心田；任由雨丝纷飞，打湿目光里的风景。心变得安静，变得爱怀想，深深怀念着过去点点滴滴的美好故事。也渐渐明了，之所以贪慕曾经的美好，皆是因为现实的不如意，而延伸出来的一种凄凉的情绪。久而久之，无形中在心里为自己设置了一个无数格子的迷宫，每一个格子里，都布满了忧伤，于是走进哪个格子？都是不快乐的。"

text1=jieba.cut(strs)
print type(text1)
fd=nltk.FreqDist(text1)

keys=fd.keys()
item=fd.iteritems()

print '- '.join(keys)

dicts=dict(item)

sort_dict=sorted(dicts.iteritems(),key=lambda d:d[1],reverse=True)
key_dict=json.dumps(sort_dict,encoding="utf-8",ensure_ascii=False)
key_dict=key_dict.replace("\",",":")
dd=key_dict.replace("[","").replace("]","").replace("\"","")
dd=dd.split(",")

for i in range(len(dd)):
    dt=dd[i].split(":")
    print dt[0],dt[1]

