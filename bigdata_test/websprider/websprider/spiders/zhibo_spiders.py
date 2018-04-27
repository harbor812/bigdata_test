# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:02:58 2018

@author: Brianzhu
"""

#import scrapy
#
#class zhibo(scrapy.Spider):
#    name ='longzhu'
#    allowed_domains=["longzhu.com"]    
#    start_url=['http://star.longzhu.com/z165000',]
#    
#    
#    def parse(self, response):
#        filename = response.url
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#            print response.body

import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)