# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:56:06 2017

@author: Brianzhu
"""

def basic_project(name): 
#        print name
        if "泡面番前端" in name:
            return 1
        if "泡面番后端" in name or "泡面番后台" in name:
            return 2
        if "公会系统" in name:
            return 3  
        if "通行证系统" in name:
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
        else:
            return 99




    