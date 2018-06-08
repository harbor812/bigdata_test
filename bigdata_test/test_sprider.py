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


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.baidu.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()