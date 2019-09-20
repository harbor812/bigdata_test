# -*- coding: utf-8 -*-
#qa:192.168.120.92:8080
#113.107.166.14:28080

import prestodb
import datetime
import numpy as np
import math


i=0
values='秦侯王爵'
values=values.decode('UTF-8')
conn=prestodb.dbapi.connect(
    host='113.107.166.14',
    port=28080,
    user='root',
#    catalog='the-catalog',
#    schema='the-schema',
)
cur = conn.cursor()
starttime=datetime.datetime.now()
#cur.execute("select * FROM hive.parquet.live_show_comment where  platform_id=201 and room_id='89867512720'  and context like '%%"+values+"%%'")
#cur.execute("select * FROM hive.parquet.live_show_entry where  platform_id=1 and from_id='768901368' and timestamp >=1555171200 and timestamp < 1555257600 limit 100")
#cur.execute("select video_tag,room_id,count(*) FROM hive.parquet.live_show_video where  platform_id=209 and timestamp >=1556294400 and timestamp < 1556467200 group by video_tag,room_id")
#cur.execute("SELECT recommend_uid ,count(distinct room_id ) as v ,array_agg(distinct room_id)  as master  FROM hive.parquet.live_show_recommend where date>='20190526'  and date<='20190627' group by recommend_uid")
#cur.execute("SELECT date, sum(video_digg_count) FROM hive.parquet.live_show_video WHERE date>='20190426'  and  date <='20190428'and plat =209 and room_id ='302280680'group by date")
#cur.execute("select platform_id, room_id ,sum(cast (video_duration as double )) as video_duration , sum(video_collection_count)  as  video_collection_count, sum(comment_count) as  comment_count ,sum(video_view_count) as video_view_count,sum(video_share_count) as  video_share_count ,sum(video_danmaku_count) as video_danmaku_count , sum(video_coin_count) as video_coin_count,sum(video_digg_count) as video_digg_count from ( SELECT platform_id,room_id,video_id,min(video_duration) as  video_duration,min(video_collection_count) as video_collection_count,min(comment_count) as  comment_count ,min(video_view_count)  as  video_view_count ,min(video_share_count) as   video_share_count , min(video_danmaku_count) as video_danmaku_count  ,min(video_coin_count) as video_coin_count,min(video_digg_count) as video_digg_count FROM mongodb237.live_show.live_show_video_minute_20190617  group by platform_id,room_id,video_id) v group by  platform_id , room_id")

#cur.execute("select platform_id, room_id ,sum(cast (video_duration as double )) as video_duration , sum(video_collection_count)  as  video_collection_count, sum(comment_count) as  comment_count ,sum(video_view_count) as video_view_count ,sum(video_share_count) as  video_share_count ,sum(video_danmaku_count) as video_danmaku_count , sum(video_coin_count) as video_coin_count,sum(video_digg_count) as video_digg_count from ( SELECT  platform_id,room_id,video_id, max(video_duration) as  video_duration, max(video_collection_count) as video_collection_count, max(comment_count) as  comment_count , max(video_view_count)  as  video_view_count , max(video_share_count) as   video_share_count ,  max(video_danmaku_count) as video_danmaku_count  , max(video_coin_count) as video_coin_count,  max(video_digg_count) as video_digg_count  FROM mongodb237.live_show.live_show_video_minute_20190619  where timestamp >=1560927478 and  timestamp <=1560932278  and room_id='54915857242' group by platform_id,room_id,video_id ) v group by  platform_id , room_id")
#cur.execute("SELECT platform_id ,from_id, from_name, yesterday_msg_num, yesterday_gift_value, seven_msg_num, seven_gift_value, thirty_msg_num ,thirty_gift_value ,all_time_msg_num, all_time_gift_value FROM hive.parquet.audience_statistics_info  order by all_time_gift_value desc limit 10000")

#cur.execute("SELECT platform_id,room_id,from_id,gift_id,price,datetime,timestamp,gift_type FROM hive.parquet.live_show_gift  where date='20190626' and gift_type='-1' limit 10")
#cur.execute("SELECT price FROM hive.parquet.live_show_gift  where date='20190626' and gift_type='1' and room_id='2384875205'")
#cur.execute("SELECT gift_type,sum(cast (price as double )*count),count(distinct from_id),sum(count) FROM hive.parquet.live_show_gift  where date='20190626' and room_id='520021' and platform_id=64 group by gift_type")
#cur.execute("SELECT gift_type,sum(cast (price as double )*count),count(distinct from_id),sum(count) FROM hive.parquet.live_show_gift  where date ='20190626' and room_id='520021' and platform_id=64 group by gift_type") #10104
#cur.execute("SELECT gift_id,sum(cast (price as double )*count) as sum_price,sum(count) as cn FROM hive.parquet.live_show_gift  where date>='20190625' and date <='20190626' and room_id='57587492' and platform_id=25 group by gift_id order by sum_price,cn") #10105
#cur.execute("SELECT from_id,sum(cast (price as double )*count) as sum_price,sum(count) as cn FROM hive.parquet.live_show_gift  where date ='20190626' and room_id='520021' and platform_id=64 and gift_type='1' group by from_id order by sum_price") #10107
#cur.execute("SELECT from_id,count(from_id) as cn FROM hive.parquet.live_show_message  where date>='20190625' and date <='20190626' and room_id='57587492' and platform_id=25 group by from_id order by cn") #10110
#cur.execute("SELECT count(from_id) as cn FROM hive.parquet.live_show_message  where date>='20190625' and date <='20190626' and room_id='57587492' and platform_id=25") #10110
cur.execute("SELECT from_id FROM hive.parquet.live_show_message  where platform_id=1 and date='20190821' limit 10") 

#cur.execute("SELECT max(view_num),min(datetime),max(datetime) FROM hive.parquet.live_show_online  where date='20190625'  and room_id='57587492' and platform_id=25") #10111

#cur.execute("SELECT * FROM hive.parquet.live_show_online  where date='20190625'  and room_id='57587492' and platform_id=25 order by datetime") #10111

#cur.execute("SELECT * FROM hive.parquet.live_show_online  where date='20190628' and room_id='432863' and platform_id=9 order by datetime ") #10112

#cur.execute("SELECT music_id,room_id,datetime FROM hive.parquet.sv_video_info_thirty  where platform_id=201 and room_id in ('100000004069','100000004548','100000004548','24726754','51475584017','61203152684','61203152684','65028246886','84990209480','98934314891','99162789887') order by datetime") #10112

#cur.execute("SELECT music_id,room_id,datetime FROM hive.parquet.sv_video_info_thirty  where platform_id=201 and room_id = '84990209480' order by datetime") #10112


#sum(cast(price as double))
#having count(from_id)>=2 and count(from_id)<=5
rows = cur.fetchall()
endtime=datetime.datetime.now()
rtime=(endtime - starttime).seconds

#print len(rows)
print "用时："+ str(rtime)
for i in zip(rows):
##  print rows[i][0],rows[i][4],rows[i][10],rows[i][8],rows[i][13],rows[i][11]   #live_show_comment
##   print rows[i][0],rows[i][1],rows[i][2]   #live_show_entry
#    print "####################################################################"
#    print rows[i][0],rows[i][1],rows[i][2]   #live_show_recommend
#    print rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5],rows[i][6],rows[i][7],rows[i][8],rows[i][9]
#    print rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5],rows[i][6],rows[i][7],rows[i][8],rows[i][9],rows[i][10],rows[i][11],rows[i][12]
    print i
#    print rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5],rows[i][6],rows[i][7]
#    print rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5],rows[i][6],rows[i][7],rows[i][8]


#print rows




###取对数
#print np.log(8844)
###开根
#print math.sqrt(math.sqrt(math.sqrt(45.57142857142857)))
