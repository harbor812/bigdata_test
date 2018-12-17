# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:56:58 2017

@author: Brianzhu
"""

import jieba,nltk
import codecs  
import jieba.posseg as ps
import json
import jieba.analyse as ja
#from jieba.analyse.analyzer import ChineseAnalyzer

#加载自定义分词
jieba.load_userdict("newdict.txt")  


def cut_sentence(sentence): 
    #加载自定义分词
#    jieba.load_userdict("newdict.txt")
#    analyzer = ChineseAnalyzer()
    stopwords = []  
    delstopwords = {}
    #,cut_all=True 去除标点符号
    strs=jieba.cut(sentence,cut_all=True)
#    strs=ps.cut(sentence)
#    for w,j in strs:
#        print w,j
#    strs=ja.extract_tags(sentence, topK=2000, withWeight=False, allowPOS=('eng'))
#    for j in range(len(strs)):
#        print strs[j]
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



if __name__ == '__main__':

    sentence="我的好朋友是888李明;我爱北京888天安门;IBM和Microsoft; I have a dream. this is intetesting and interested me a lot"
#    sentence=str(sentence).decode("unicode-escape")
#    print sentence
    dicts= cut_sentence(sentence)
    sort_dict=sorted(dicts.iteritems(),key=lambda d:d[1],reverse=True)
    key_dict=json.dumps(sort_dict,encoding="utf-8",ensure_ascii=False)
    key_dict=key_dict.replace("\",",":")
    dd=key_dict.replace("[","").replace("]","").replace("\"","")
    dd=dd.split(",")
    print "#############################################"
    for x in range(len(dd)):
        dt=dd[x].split(":")
        print dt[0]
