# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:13:58 2017

@author: Brianzhu
"""

import jieba,nltk,json,time
import codecs   
import db_mysql  



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



if __name__ == '__main__':
     db=db_mysql.dbmysql()
     #获取所有commintcode 信息
     commintcode=db.bug_sel_commitcode()
     for i in range(len(commintcode)):
         cc=commintcode[i]
         cn=db.bug_sel_keyword_cc(cc[0],cc[2])
         #在词频表中 如果 commintcode 存在就不继续处理
         if cn[0] == 0:
    #         print type(cc[1])
             #获取commitcode 对应的bugname
             res=db.bug_sel_bugname(cc[2],str(cc[1]))
             #bugname 不为空 做词频统计和排序
             if res != ():
                 strs=str(res).decode("unicode-escape")
                 dicts=cut_sentence(strs)
                 sort_dict=sorted(dicts.iteritems(),key=lambda d:d[1],reverse=True)
                 key_dict=json.dumps(sort_dict,encoding="utf-8",ensure_ascii=False)
                 key_dict=key_dict.replace("\",",":")
                 dd=key_dict.replace("[","").replace("]","").replace("\"","")
                 dd=dd.split(",")
                 #合并有效数据，插入数据库
                 for i in range(len(dd)):
                    dt=dd[i].split(":")
                    date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    if dt[0]:
                        #转译词频词并且去除空格
                        kw=dt[0].encode('utf-8').strip() 
                        bugid=db.bug_sel_bugid(cc[2],str(cc[1]),kw)
                        bugid=str(bugid).replace("(","").replace(",)","").replace("u","").replace("'","").replace(")","")
                        db.keyword_save(cc[0],cc[2],kw,dt[1],date,bugid)
                        db.keyword_del()
