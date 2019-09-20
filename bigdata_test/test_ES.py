# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:26:12 2019

@author: Brianzhu
"""

from elasticsearch5 import Elasticsearch
import pandas as pd

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)



def db_es():
    es = Elasticsearch(
            ['113.107.166.14'],
    #        http_auth=('elastic', 'passwd'),
            port=19200
    )
    #platID=1&roomID=2384875205&startTime=1561482671&endTime=1561523909
    #query ={'query': {'match_all': {}}}
    
    #query = {
    #        "size": 10000,
    #    "query":{
    #        "match":{
    #            "platform_id":"2"
    ##            "timestamp":"1561735836"
    #        }
    #    }
    #}
    
    #query = {
    #        "size": 10000,
    #    "query":{
    #         "bool": {
    #        "must":[
    #        {"match":{
    #            "platform_id":"20"
    ##            "timestamp":"1561735836"
    #        }},
    #        {"match":{
    #            "room_id":"281147838"
    ##            "timestamp":"1561735836"
    #        }},
    #        {"match":{
    #            "gift_type":"0"
    ##            "timestamp":"1561735836"
    #        }},
    #        {"range":{
    #           "timestamp":{"lte":"1562638920",} #gte,lte
    #        }}
    ##        {"range":{
    ##           "timestamp":{"lte":"1562638920",} #gte,lte
    ##        }}
    ##        {"sort":{
    ##           "from_id":{"order by":"desc",} #gte,lte
    ##        }}
    #        ]
    #        }
    #    }
    #}
    #        
    query = {
            "size": 10,
        "query":{
             "bool": {
            "must":[
            {"match":{
                "platform_id":"1"
            }},
#            {"match":{
#                "from_id":"cc_1333_38802060_1477136798"
#            }}
            {"match":{
                "gift_name":""
            }},
            {"match":{
                "gift_type":"1"
            }}
#            {"range":{
#               "count":{"gte":2} #gte,lte
#            }}                
#            {"range":{
#               "timestamp":{"gte":"1563798600"} #gte,lte ,"lte":"1563728700"    "gte":'1562567226'
#            }}
            ]
            }
        }
    }
    #query = {
    #    "query":{
    #        "terms":{
    #            "room_id":[
    #                "432863","432863"
    #            ]
    #        }
    #    }
    #}
    #res = es.get(index="liveshow-2018-07-20",doc_type='gift',id='1')  # 获取所有数据
    #res = es.search(index='liveshow-online-page-2019-06-29', doc_type='page',body=query)
    res = es.search(index='xiaohulu-liveshow-2019-08-26', doc_type='gift',body=query)
    return res    
 

#统计礼物价格区间 数量
def price_type_1(res):
    count=[]
    count1=[]
    count2=[]
    from_id_list=[]
    from_id_list1=[]
    price_sum=[]
    for hit in res['hits']['hits']:
    #    print hit["_source"]['from_id']
    #    print hit["_source"]
        price=float(hit["_source"]['price'])*float(hit["_source"]['count'])
        count.append(price)
        count1.append(hit["_source"]['from_id'])
        count2.append(hit["_source"]['count'])
    
    cns_data=pd.DataFrame({'price':count,'from_id':count1,'zcount':count2})
    
    for i in range(len(cns_data)):
        from_id_list.append(cns_data.iloc[i,0])
    from_id_data=pd.DataFrame({'from_id':from_id_list})
    from_id_data_duplicates=from_id_data.drop_duplicates()
    
    
    for j in range(len(from_id_data_duplicates)):
        changename_data1=cns_data[(cns_data['from_id'] == from_id_data_duplicates.iloc[j,0])]
        price_sum.append(int(changename_data1['price'].sum()))
        from_id_list1.append(from_id_data_duplicates.iloc[j,0])
    
    cns_data1=pd.DataFrame({'price':price_sum,'from_id':from_id_list1})
    
    #print cns_data1
    #print cns_data
    ############################
    #cns_data=pd.DataFrame({'timestamp':count})
    #bugid_cn=cns_data.drop_duplicates() 
    
    #print bugid_cn
    #print cns_data
    ############################
    int1,int2,int3,int4,int5=0,0,0,0,0
    
    
    ###################################
    #cns_data1=pd.DataFrame({'from_id':count1})
    
    #cn_count_price=cns_data1[cns_data1['from_id'].str.contains('85893344')].count()
    
    #cn_count_price=cns_data[cns_data['from_id'].str.contains('701868355')]
    
    #print cn_count_price
    ###################################
    
    #
    for z in range(len(cns_data1)):
        cn_count_int=float(cns_data1.iloc[z,1])
    #    print fm_id  
    #    cn_count=cns_data[cns_data['fx_change_name'].str.contains(fm_id)]
    #    cn_count_int=float(cns_data['fx_change_name'])
        if cn_count_int == 0:
            int1=int1+1
        if cn_count_int >= 10 and cn_count_int <100 :
            int2=int2+1
        if cn_count_int >= 100 and cn_count_int < 1000:
            int3=int3+1
            from_id_list1.append(cns_data.iloc[i,0])
        if cn_count_int >= 1000 and cn_count_int < 5000:
            int4=int4+1
        if cn_count_int < 10 :
            int5=int5+1
    #        print cns_data1.iloc[z,0],cns_data1.iloc[z,1]
    #        from_id_list.append(cns_data.iloc[i,0])
    #cns_data=pd.DataFrame({'timestamp':from_id_list})
    ##cns_data1=pd.DataFrame({'timestamp':from_id_list1})
    #bugid_cn=cns_data.drop_duplicates() 
    ##bugid_cn1=cns_data1.drop_duplicates()
    #print "####################"
    #print len(bugid_cn)
    #print "####################"
    #print bugid_cn
    #"####################"
    print '等于0：%s,大于10小于99：%s,大于100小于999：%s,大于1000小于4999：%s,小于10：%s'%(int1,int2,int3,int4,int5)
    
#根据gift_id 统计礼物数量
def price_type_2(res):
    count=[]
    count1=[]
    count2=[]
    from_id_list=[]
    from_id_list1=[]
    price_sum=[]
    for hit in res['hits']['hits']:
    #    print hit["_source"]['from_id']
    #    print hit["_source"]
        price=float(hit["_source"]['price'])*float(hit["_source"]['count'])
        count.append(price)
        count1.append(hit["_source"]['gift_id'])
        count2.append(int(hit["_source"]['count']))
    
    cns_data=pd.DataFrame({'price':count,'from_id':count1,'zcount':count2})
    
    for i in range(len(cns_data)):
        from_id_list.append(cns_data.iloc[i,0])
    from_id_data=pd.DataFrame({'from_id':from_id_list})
    from_id_data_duplicates=from_id_data.drop_duplicates()
    
    
    for j in range(len(from_id_data_duplicates)):
        changename_data1=cns_data[(cns_data['from_id'] == from_id_data_duplicates.iloc[j,0])]
        price_sum.append(int(changename_data1['zcount'].sum()))
        from_id_list1.append(from_id_data_duplicates.iloc[j,0])
    
    cns_data1=pd.DataFrame({'price':price_sum,'from_id':from_id_list1})
    
    #print cns_data1
    #print cns_data
    ############################
    #cns_data=pd.DataFrame({'timestamp':count})
    #bugid_cn=cns_data.drop_duplicates() 
    
    #print bugid_cn
    #print cns_data
    ############################
    print cns_data1

def message(res):

    count1=[]
    
    int1,int2,int3,int4,int5=0,0,0,0,0
    for hit in res['hits']['hits']:
        count1.append(hit["_source"]['from_id'])

    
    cns_data=pd.DataFrame({'fx_change_name':count1})
    

    for i in range(len(cns_data)):
        fm_id=cns_data.iloc[i,0]
    #    print fm_id
        cn_count=cns_data[cns_data['fx_change_name'].str.contains(fm_id)].count()
#        print   fm_id, cn_count['fx_change_name']  
        cn_count_int=int(cn_count['fx_change_name'])
        if cn_count_int == 1:
            int1=int1+1
        if cn_count_int >= 2 and cn_count_int <= 5:
            int2=int2+1
        if cn_count_int >= 6 and cn_count_int <= 10:
            int3=int3+1
        if cn_count_int >= 11 and cn_count_int <= 20:
            int4=int4+1
        if cn_count_int >= 20:
            int5=int5+1
    print '等于1：%s,大于2小于5：%s,大于6小于10：%s,大于11小于20：%s,大于20：%s'%(int1,int2,int3,int4,int5)

def sample_data(res):
    price=0
    for hit in res['hits']['hits']:
#        print hit["_source"]['price'],hit["_source"]['count'],hit["_source"]['room_id']
        price1=float(hit["_source"]['price'])*float(hit["_source"]['count'])
        price=price+price1
#    print price
#        print price1,hit["_source"]['timestamp']
        print hit["_source"]['price'],hit["_source"]['count'],price1,hit["_source"]['timestamp'],hit["_source"]['from_id'],hit["_source"]['gift_name']

def sample_data_message(res):
#    price=0
    for hit in res['hits']['hits']:
#        print hit["_source"]['price'],hit["_source"]['count'],hit["_source"]['room_id']
#        price1=1
#        price=price+price1
        print hit["_source"]['timestamp'],hit["_source"]['from_id'],hit["_source"]['from_name']
if __name__ == '__main__':
    res=db_es()
#    price_type_1(res)
#    price_type_2(res)
    sample_data(res)
#    sample_data_message(res)
#    message(res)