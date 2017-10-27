# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:56:58 2017

@author: Brianzhu
"""

import jieba,nltk
import codecs   

#加载自定义分词
jieba.load_userdict("newdict.txt")  


def cut_sentence(sentence): 
    stopwords = []  
    delstopwords = {}
    strs=jieba.cut(sentence)
    fd=nltk.FreqDist(strs)
    keys=fd.keys()
    item=fd.iteritems()
    dicts=dict(item)
    st = codecs.open('./stopwords.txt', 'rb',encoding='utf-8')  
    for line in st:  
        line = line.strip() 
        stopwords.append(line)

    #过滤停用词
    for word in keys:  
        word = word.strip()
        if word not in stopwords:  
#            if word >= u'\u4e00' and word <= u'\u9fa5':#判断是否是汉字
                if word in dicts.keys():
                    delstopwords[word]=dicts[word]

    return delstopwords