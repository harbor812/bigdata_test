# -*- coding: utf-8 -*-
import scrapy
from webspider.items import WebspiderItem


class TencentpostionSpider(scrapy.Spider):
    name = "tencentPostion"
    allowed_domains = ["tencent.com"]
    start_urls = ['http://hr.tencent.com/position.php?&start=']

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = WebspiderItem()
            # 职位名称
#            /html/body/div[3]/div[1]/table/tbody/tr[2]/td[1]/a
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 1680:
            self.offset += 10

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
