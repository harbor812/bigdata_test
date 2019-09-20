# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:56:06 2017

@author: Brianzhu
"""

def basic_project(name):
#        print name
        if "泡面番前端" in name or "泡面番前台" in name:
            return 1
        if "泡面番后端" in name or "泡面番后台" in name:
            return 2
        if "公会系统" in name:
            return 3
        if "通行证系统" in name or "通行证" in name:
            return 4
        if "聚宝盆系统" in name:
            return 5
        if "大数据统计" in name:
            return 6
        if "视频处理" in name:
            return 7
        if "搜索引擎" in name:
            return 8
        if "实时抓取视频切割数据" in name or "实时抓取"in name:
            return 9
        if "弹幕游戏" in name:
            return 10
        if "系统监控" in name:
            return 11
        if "录制工具" in name:
            return 12
        if "抓娃娃" in name:
            return 13
        if "站内信" in name:
            return 14
        if "泡面番app安卓" in name or "泡面番APP安卓" in name:
            return 15
        if "泡面番appIOS" in name or "泡面番APPIOS" in name or "app-IOS" in name:
            return 16
        if "平台分享" in name:
            return 17
        if "范特西appIOS" in name or "范特西appiOS" in name:
            return 19
        if "范特西app安卓" in name:
            return 20
        if "范特西" in name:
            return 18
        if "阿凡达appIOS" in name or "阿凡达appios" in name or "阿凡达appiOS" in name or "avatarappIOS" in name or "avatarappios" in name or "avatarappiOS" in name:
            return 28
        if "阿凡达app安卓" in name:
            return 29
        if "阿凡达" in name or "avatar" in name:
            return 21
        if "IOS" in name or "ios" in name or "appiOS" in name:
            return 22
        if "安卓" in name:
            return 23
        if "小葫芦星球" in name or "兑换红包" in name or "h5直播数据" in name  or "足球" in name or "pick" in name or "小葫芦小程序" in name or "小程序主播端" in name or "小程序粉丝端" in name or "小程序星球" in name or "冲榜" in name or "时间胶囊" in name:
            return 21
        if "星球game" in name or "星球游戏" in name:
            return 24
        if "短视频" in name or "短视屏" in name:
            return 31
        else:
            return 99



def basic_project1(name): 
#        print name
       if "1" in name:
           return "泡面番前端"
       if "2" in name :
           return "泡面番后端"
       if "3" in name:
           return "公会系统" 
       if "4" in name:
           return "通行证系统"
       if "5" in name:
           return "聚宝盆系统"
       if "6" in name:
           return "大数据统计"
       if "7" in name:
           return "视频处理"
       if "8" in name:
           return "搜索引擎"
       if "9"in name:
           return "实时抓取"
       if "10" in name:
           return "弹幕游戏"
       if "11" in name:
           return "系统监控" 
       if "12" in name:
           return "录制工具" 
       if "13" in name:
           return "抓娃娃" 
       if "14" in name:
           return "站内信"
       if "15" in name:
           return "泡面番app安卓" 
       if "17" in name:
           return "平台分享"
       if "18" in name:
           return "范特西"
       if "19" in name:
           return "范特西appIOS"
       if "20" in name:
           return "范特西app安卓"
       if "21" in name:
           return "小葫芦星球"
       if "22" in name:
           return "小葫芦星球appIOS"
       if "23" in name:
           return "小葫芦星球app安"
       else:
           return "其他"


if __name__ == '__main__':
    name='（小葫芦星球2.8.9安卓）首页点击榜单切换月份闪退，C位战切换也闪退'
    print basic_project(name)
    