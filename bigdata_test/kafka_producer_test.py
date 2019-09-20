# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:26:12 2019

@author: Brianzhu
"""
from kafka.producer import SimpleProducer
from kafka import KafkaConsumer
from kafka import KafkaClient
from kafka import TopicPartition

from kafka import KafkaProducer
import ast,pandas as pd 
print 'start '

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


#node-online-room
#short-video-crawler-video-201
#consumer = KafkaConsumer('node-online-data-player',bootstrap_servers='Kafka-game-01:9092',auto_offset_reset="earliest")


#consumer = KafkaConsumer('node-bullet-crawler-57',bootstrap_servers='Kafka-game-01:9092',auto_offset_reset="earliest")
#latest
consumer = KafkaConsumer('node-bullet-crawler-2',bootstrap_servers='Kafka-01:9092',auto_offset_reset="latest",group_id='kafka_crawler-video3')
# consumer.set_topic_partitions('kafka_input')
status=0
#,index = [0]
#values=pd.DataFrame({'create_time':'','video_id':'','video_share_count':'','comment_count':'','magic_effect_name':'','cha_list':[]})

#for i in consumer:
#    value=ast.literal_eval(i.value)
#    print value
#    print len(value)
#    value1=dict(value[0])
#    value2=value[1]
#    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#    print value1
#    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#    print value2
#    if i >1:
#        break
    


#for i in consumer:
##    if '6692971731864358158' in i.value:
#    value=ast.literal_eval(i.value)
#
#    for j in range(len(value)):
#        value1=dict(value[j])
#        v1=value1['item']
#        v2=dict(v1[0])
#        print v2['time']
##        print v2['time']
##        if v2['time']< and v2['roomid'] == :
##        if value1['create_time'] > 1559210423 and (value1['magic_effect_name'] !=''):
###        if value1['video_id']=='6696495263114185992' and (value1['magic_effect_name'] !='' or value1['cha_list'] !=[]):
##            print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
###            l_values='%s-%s-%s-%s'%(value1['create_time'],value1['video_id'],value1['video_share_count'],value1['comment_count'])
##            values1=pd.DataFrame({'create_time':value1['create_time'],'video_id':value1['video_id'],'video_share_count':value1['video_share_count'],'comment_count':value1['comment_count'],'magic_effect_name':value1['magic_effect_name'],'cha_list':value1['cha_list']})
##            print value1
###            status=1
###            values.append(l_values)
##            if values.iloc[0,0] == '':
##                values=values1
##            else:
##                ##合并dataframe
##                frames=[values1,values]
##                values=pd.concat(frames)
##            status=1
###            if j >= 100:
###                status=1            
##
#        if j == 2:
#            print "status == 1"
#            break
##        print "######################################"
##        print (value1['create_time'],value1['video_id'],value1['video_share_count'],value1['comment_count'])
#    break
#
#consumer.close()
##with open("kafka_values.txt","w") as f:
##     f.truncate() #清空数据
##     f.write(str(values))





time=[]
roomid=[]
message=[]
price1=[]
z=1
for i in consumer:
#    if '6692971731864358158' in i.value:
    value=ast.literal_eval(i.value)
#    print type(value)
    for j in range(len(value)):
        value1=dict(value[j])        
        v1=value1['item']
        v2=dict(v1[0])
#        print v2['time']
        if value1['sid'] =='2' :
            z=z+1
#        if value1['create_time'] > 1559210423 and (value1['magic_effect_name'] !=''):
#        if value1['video_id']=='6696495263114185992' and (value1['magic_effect_name'] !='' or value1['cha_list'] !=[]):
#            print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#            l_values='%s-%s-%s-%s'%(value1['create_time'],value1['video_id'],value1['video_share_count'],value1['comment_count'])
            if v2['type'] == 'gift' and v2['gift_type'] == '1':
                price=float(v2['count']) * float(v2['price'])
                price1.append(price)
            else:
                price1.append(0)

            roomid.append(value1['roomid'])
#            message.append(value1['chatCount'])
            if z == 10:
                break

#            status=1
#            values.append(l_values)
#        break
    break 
consumer.close()

#values1=pd.DataFrame.from_dict({'roomid':roomid,'price':price1}, orient='index')
values1=pd.DataFrame({'roomid':roomid,'price':price1})


print values1
#with open("kafka_values.txt","w") as f:
#     f.truncate() #清空数据
#     f.write(str(values))
     

     