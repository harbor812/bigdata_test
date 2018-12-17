# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:51:39 2018

@author: Brianzhu
"""
#from gensim.models import word2vec
import synonyms
#
#fp=open("D:\\git\\bigdata_test\\bigdata_test\\wordresult.txt",'r')
#sentences=fp.readlines()
#st=sentences[0].split(',')
#
##    print "###################################"
##    #
###    print st
##    print "###################################"
#
#st_list=[]
#
#for i in range(len(st)):
#    if '\xef\xbb\xbf' in st[i]: 
#        st1=st[i].replace("\xef\xbb\xbf","")
#        st_list.append(st1.strip())
#    else:
#        st_list.append(st[i].strip())
#
##    print st_list
#stlen=len(st_list)
#sentences1=[[] for i in range(stlen)]
#
#for a in range(0,stlen):    
#    sentences1[a].append(st_list[a]) 


#model = word2vec.Word2Vec(sentences1, min_count=1,size=300)
##y2=model.most_similar('填写',topn=1)
###model['OutOfMemory']
###y1 = model.similarity("OutOfMemory","内存溢出")
##print "比对结果：#######################"
###print y2
##for i in range(len(y2)):
##    print y2[i][0],y2[i][1]
#
#y2=model.most_similar(positive=['钱包', 'wallet'], negative=['奔溃'])
#
#for i in range(len(y2)):
#    print y2[i][0],y2[i][1]


###########################synonyms
comment='getQuestionCount'
bug_name='小程序apiquestionReplyaddComment传参错误'
print synonyms.compare(comment, bug_name, seg=False)
print len(comment),len(bug_name)
#str1="接口 报错  /api/user /userUnBindPlat"
#print str1
#print str1.strip()
#print str1.replace(" ","")
##sy=synonyms.nearby('一步')
#print sy
#for i in range(len(sy)):
#    
#    print sy[0][i],sy[1][i]

