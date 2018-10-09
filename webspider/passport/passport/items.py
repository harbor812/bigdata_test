# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PassportItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    nick_name = scrapy.Field()
    # 性别
    sex = scrapy.Field()
    # 生日
    birthday = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 绑定平台数
    bind_platform = scrapy.Field()
    # 手机号
    mobile_num = scrapy.Field()
    pass