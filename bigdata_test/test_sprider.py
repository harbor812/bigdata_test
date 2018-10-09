# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 13:44:32 2018

@author: Brianzhu
"""

#import requests,json,re
#
#url='http://star.longzhu.com/z165000'
##url='http://rpc.paomianfan.com:27020/'
##files='roomUrl=http://star.longzhu.com/z196955'
##resp=requests.post(url,data=files,timeout=1,allow_redirects=True)
#resp=requests.get(url,timeout=1,allow_redirects=True)
#html=resp.text
#getdata=re.findall('<script>(.*)</ script>',html)
#
#print html
#print "============================================="
#print getdata
##j=resp.json()
##
##print j['data']['liveStatus']
## 转json  resp.json() or data=json.loads(resp.text)


#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#
#browser = webdriver.Firefox()
#
#browser.get('http://www.baidu.com')
#assert 'Yahoo' in browser.title
#
#elem = browser.find_element_by_name('p')  # Find the search box
#elem.send_keys('seleniumhq' + Keys.RETURN)
#
#browser.quit()






import datetime,time

from business_calendar import Calendar



#def workDay():
# #判断是否为工作日,工作日返回1，非工作日返回0
# workTime=['09:00:00','20:00:00']
# dayOfWeek = datetime.datetime.now().weekday()
# #dayOfWeek = datetime.today().weekday()
# beginWork=datetime.datetime.now().strftime("%Y-%m-%d")+' '+workTime[0]
# endWork=datetime.datetime.now().strftime("%Y-%m-%d")+' '+workTime[1]
# beginWorkSeconds=time.time()-time.mktime(time.strptime(beginWork, '%Y-%m-%d %H:%M:%S'))
# endWorkSeconds=time.time()-time.mktime(time.strptime(endWork, '%Y-%m-%d %H:%M:%S'))
# if (int(dayOfWeek) in range(5)) and int(beginWorkSeconds)>0 and int(endWorkSeconds)<0:
#    return 1
# else:
#    return 0
#
# 
#print workDay()
#print (datetime.datetime.now()+datetime.timedelta(days=3)).weekday()


date=datetime.datetime.now().strftime("%Y-%m-%d")
date1=datetime.datetime.now()+datetime.timedelta(days=-1)
date1=date1.strftime("%Y-%m-%d")
date2=datetime.datetime.now()+datetime.timedelta(days=-2)
date2=date2.strftime("%Y-%m-%d")
#判断是否为工作日,工作日返回true，非工作日返回false
cal = Calendar()
if cal.isbusday(date)==True:
    if cal.isbusday(date2)==False:
        d1=0
        d2=0
        while cal.isbusday(date1)==False:
            d1=d1+1
            days1=-1-d1
            date1=datetime.datetime.now()+datetime.timedelta(days=days1)
            date1=date1.strftime("%Y-%m-%d")
        while cal.isbusday(date2)==False :
            d2=d2+1
            days2=-2-d2
            date2=datetime.datetime.now()+datetime.timedelta(days=days2)
            date2=date2.strftime("%Y-%m-%d")
            if date1 == date2:
                d2=d2+1
                days2=-2-d2
                date2=datetime.datetime.now()+datetime.timedelta(days=days2)
                date2=date2.strftime("%Y-%m-%d")

print date,date1,date2
