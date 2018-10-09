# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:11:38 2018

@author: Brianzhu
"""

import pymongo
 
myclient = pymongo.MongoClient('mongodb://mongoadmin:HwA5RW9kkc@58.253.65.93/xhl.audience_ident?authSource=admin&authMechanism=SCRAM-SHA-1')

mydb = myclient["live_plugin"]
mycol = mydb["live_plugin"]


##查询 
#x = mycol.find_one()
#print(x) 

#for x in mycol.find({"gid" : "e10adc3949ba59abbe56e057f20f883e",'time': 1538041811}):
#  print "##################################################################"
#  print(x)
  
  
#for x in mycol.find():
#  print "##################################################################"
#  print(x)



###插入数据
#mydict = {
#    "unionid" : "ab536a330d62c10a2e14bea982b6c22d",
#    "gid" : "e10adc3949ba59abbe56e057f20f883e",
#    "md5" : "7000f946991b72e489cf1a8b704a55ad",
#    "resid" : "6523e8ba-49bd-41ae-9921-5bfa06b0da15",
#    "guid" : "cjmke8zyc000d4ju35chv9grs",
#    "tag" : "1234567",
#    "data" : "{\"Fans\":{\"Id\":\"1\",\"Name\":\"嘻哈大傻瓜\",\"Icon\":null,\"UserRole\":0},\"TotalScore\":{\"Value\":7.0,\"UpdateStamp\":1532238561},\"TodayTotalScore\":{\"Value\":7.0,\"UpdateStamp\":1532238561},\"SignInScore\":{\"SeriesSignIn\":{\"SeriesDays\":1,\"SignIned\":false},\"SignIned\":false,\"isExtra\":false,\"Value\":7.0,\"UpdateStamp\":1532238561},\"TodaySignInScore\":{\"SeriesSignIn\":{\"SeriesDays\":0,\"SignIned\":false},\"SignIned\":false,\"isExtra\":false,\"Value\":0.0,\"UpdateStamp\":1537970400},\"SignInFreeGiftScore\":{\"SeriesSignIn\":{\"SeriesDays\":0,\"SignIned\":false},\"SignIned\":false,\"isExtra\":false,\"Value\":0.0,\"UpdateStamp\":1532238530},\"SignInPayGiftScore\":{\"SeriesSignIn\":{\"SeriesDays\":0,\"SignIned\":false},\"SignIned\":false,\"isExtra\":false,\"Value\":0.0,\"UpdateStamp\":1532238530},\"SignInGiftScore\":{\"SeriesSignIn\":{\"SeriesDays\":0,\"SignIned\":false},\"SignIned\":false,\"isExtra\":false,\"Value\":0.0,\"UpdateStamp\":1532238530},\"MusicScore\":{},\"TodayMusicScore\":{},\"QuerySecondStamp\":0,\"Consume\":1.0,\"IsDelete\":false}",
#    "block" : 1,
#    "totalBlock" : 3,
#    "time" : 1538041587
#}
#x = mycol.insert_one(mydict) 
#print(x)


###修改
#myquery = { "alexa": "10000" }
#newvalues = { "$set": { "alexa": "12345" } }
# 
#mycol.update_one(myquery, newvalues)


#myquery = { "name": { "$regex": "^F" } }
#newvalues = { "$set": { "alexa": "123" } }
#
#mycol.update_one(myquery, newvalues) 
#x = mycol.update_many(myquery, newvalues)
# 
#print(x.modified_count, "文档已修改")

###删除数据
#myquery = { "gid" : "e10adc3949ba59abbe56e057f20f883e" }
# 
#mycol.delete_one(myquery)
# 
## 删除后输出
#for x in mycol.find():
#  print(x)