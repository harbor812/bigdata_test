# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:16:23 2018

@author: Brianzhu
"""

#from gensim.models import word2vec
import db_mysql
import synonyms
import datetime


def wordresult(db):
    dd= db.levelwords_selname()
    bugname=str(dd).decode("unicode-escape")
    print bugname
    bugname=bugname.replace("(u'","").replace(",)","").replace("(","").replace("'","")
    bugname=bugname.replace(")","").encode('utf-8')
    
    with open("wordresult.txt","w") as f:
         f.write(bugname)


def similarity(db,keywords):
    fp=open("D:\\git\\bigdata_test\\bigdata_test\\wordresult.txt",'r')
    sentences=fp.readlines()
    st=sentences[0].split(',')
#    print "###################################"
#    #
##    print st
#    print "###################################"
    
    st_list=[] #  词库列表
    keywords1=0   #最接近的词
#    sim=0.01   #相似度
    sim1=0.01   #相似度
    sim2=0.01   #相似度
    sent1=0


    for i in range(len(st)):
        if '\xef\xbb\xbf' in st[i]: 
            st1=st[i].replace("\xef\xbb\xbf","")
            st_list.append(st1.strip())
        else:
            st_list.append(st[i].strip())
    
#    print st_list
    stlen=len(st_list)
    #sentences=np.array(st_list).reshape(1,12)
    #sentences2=np.array(st_list,dtype=str).reshape((1,stlen))
    sentences1=[[] for i in range(stlen)]
    
    for a in range(0,stlen):    
        sentences1[a].append(st_list[a])  
    
#    print "###################################"
#    print sentences1
    
    
#    model = word2vec.Word2Vec(sentences1, min_count=1,size=500)
#    kw1=keywords.encode('utf-8')
##    print " 获取词性最接近的词###################################" 
#    y1=model.most_similar(kw1)
#    keywords1=y1[0][0]
#    sim=y1[0][1]
#    if kw1==keywords1:
#       keywords1=y1[1][0]
#       sim=y1[1][1]
    keywords1=keywords.encode('utf-8')
    sentlen=len(sentences1)
    for i in range(sentlen):
        sent=sentences1[i][0]
        if keywords1 != sent:
            sim1=synonyms.compare(keywords1, sent, seg=True)
            if sim1 > sim2:
                sim2 =sim1
                sent1=sent
       
    return sent1,sim2
    
        


if __name__ == '__main__':
    db=db_mysql.dbmysql()
    starttime=datetime.datetime.now()
    wordresult(db)   
    try:
        levelname_list=db.levelwords_no_tagname()
    #        print levelname_list[1][0]
        for i in range(len(levelname_list)):
            ln=levelname_list[i][0]
            ky=similarity(db,ln)
            same_word=str(ky[0])
            Similarity=ky[1]

            if Similarity > 0.3:
               print ln,ky
               print Similarity
               levelwords_detail=db.levelwords_detail(same_word)
    #           print ln,ky[0],ky[1]
    #           print "############################"
               level_id=levelwords_detail[0][0]
               tag_name=levelwords_detail[0][1]
    #           print tag_name
               if tag_name !=None and Similarity > 0.5:
                   print "############################"
                   print ln,level_id,tag_name,same_word,Similarity
                   db.levelwords_update(ln,level_id,tag_name,same_word,Similarity,'0')
               else:
                   print " 为none############################"
                   print ln,level_id,tag_name,same_word,Similarity
                   db.levelwords_update(ln,level_id,tag_name,same_word,Similarity,'1')
 #KeyError   
    except (UnicodeDecodeError,KeyError),e:
            print e.message
    endtime=datetime.datetime.now()
    rtime=endtime - starttime
    
    print rtime
    
       
       


