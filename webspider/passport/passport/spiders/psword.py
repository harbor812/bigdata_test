# -*- coding: utf-8 -*-
import scrapy
from passport.items import PassportItem
#from scrapy.http import FormRequest
from scrapy.http import Request,FormRequest




class PswordSpider(scrapy.Spider):
    name = "psword"
    allowed_domains = ["passport.xiaohulu.com"]
    start_urls = ['https://passport.xiaohulu.com/me']
    
    header={
#            "Host": "passport.xiaohulu.com",
#            "Connection": "keep-alive",
#            "Cache-Control": "max-age=0",
#            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
#            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#            "Accept-Encoding": "gzip, deflate, sdch, br",
#            "Accept-Language": "zh-CN,zh;q=0.8",
#            Cookie: 6N3e_f2ec___XHLTXZ__www=516bTi9pxwbnr%2BTD60SAFn7H56ukRQGR5k8sFCjqQV5a6p0gv8BJanuxyjmVjpva9eOPngMxAH93jNj%2F5kvqJ9%2BqlKm36e%2FwfSVSYNmuAdJTZgVZ1uREQaPaCecP9EYt6PSgrSGHII7cbHj9DIU7gGc; 6N3e_f2ec_auth=f2d0OJBwMGXu%2BZHHiW1ankZvjId1%2BvZNinkdDwYD3lO8%2F%2B40NtbI7uQtqFzg9efeLs8YbE%2BJ43SbCkKNd44gHxnTPv2ZgTDSDZ0YC0zU; Hm_lvt_df9403e4b025ecf85b4310bda73ab65e=1531278211,1531278235,1531363105,1531363498; 6N3e_f2ec_saltkey=P4r4VpMR; 6N3e_f2ec_lastvisit=1535086387; Hm_lvt_2772005b8bc0b193d080228322981977=1534832621; Hm_lvt_1c358b33dfa30c89dd3a1927a5921793=1534832621; 6N3e_f2ec___XHLTXZ__www_my="cae706ANqO5yZtrgZ/VklIwYge8ZcIBrt9XzCW4/Q5l1Wd3JBpOu5kRQ0ZQxLvrXUzmJsiKb3EeX5JguF4SkQIbasLirReFdyPh/4w=="; XSRF-TOKEN=eyJpdiI6Im9FTHRkRjc3bkJiYTBEY0xmRW4zOUE9PSIsInZhbHVlIjoiblhYOTBYQllVZUlIcW92WWNvTjg3SHVyYm54WHFuVjVXeCszd3JBU1Jvb2hlTWRjdHVyQVhBQzA5dEVoaGlTQ1wvWW9CeUNjRVZiSFRsTFpQZmJINmhBPT0iLCJtYWMiOiJhZDMwNGY1OTA1YTU3ODM1MTdkZTBjYTUzZDZmMjQ1ZWM0ZmQ1OTMyNjI5YTNlOTAxZGEyNzY0ZGE4OTJlNzQzIn0%3D; laravel_session=eyJpdiI6IjR1RHZcL0VFbDlERWFieElxdlhoWmd3PT0iLCJ2YWx1ZSI6InVlQ3FXOFZqdXpndEJmdWpMcDd4TjI2MHF5K2VWOVwvc1lNeTc0N0xjVjdXaE5UWjA3T3dtSGg4dWxkVGlNSjBsQ0U4MFNnZ1NFQXBGU0w5WDl0YUhoUT09IiwibWFjIjoiM2UyZTg5YTY4MGE5NDljZTY4YmU5M2FhNDk1OGM0MGVlMTczMzIyNGZiMmY0N2QyYjU5NGI2MWVlODI3OTljZiJ9; Hm_lvt_afc61e0a3581591fec36a81263bcfe5d=1535089955,1535339670; Hm_lpvt_afc61e0a3581591fec36a81263bcfe5d=1536057965

            }    




    def start_requests(self):

        #    t = str(int(time.time() * 1000))
        captcha_url = 'https://passport.xiaohulu.com'
        return [Request(url=captcha_url, headers=self.header, meta={'cookiejar':1},callback=self.parser)]


    def parser(self, response):
        data={
              'username':'13818121262',
              'countryCode':'86',
              'lang':'',
              'type':'1',
              'password':'7c4a8d09ca3762af61e59520943dc26494f8941b',
              'homepage_params':'[]'
              }

        Cookie1 = response.headers.getlist('Set-Cookie')   #查看一下响应Cookie，也就是第一次访问注册页面时后台写入浏览器的Cookie
        print "########Cookie1########################"
        print Cookie1
        return [FormRequest.from_response(response,
                                          url='https://passport.xiaohulu.com/login',   #真实post地址
                                          meta={'cookiejar':response.meta['cookiejar']},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,
                                          )]
    def next(self,response):
        a = response.body  #登录后可以查看一下登录响应信息
        print "########登录后可以查看一下登录响应信息########################"
        print a
#        """登录后请求需要登录才能查看的页面，如个人中心，携带授权后的Cookie请求"""
        item = PassportItem()
        item["leir"] = response.xpath('/html/body/div[1]/nav/div[2]/div[1]/img/@src').extract()[0]  #得到个人中心页面
#        print '头像url',leir
        item["leir2"] = response.xpath('/html/body/div[1]/nav/div[2]/div[1]/p/text()').extract()[0]  # 得到个人中心页面
#        print '用户名',leir2
        yield item
#        """登录后请求需要登录才能查看的页面，如个人中心，携带授权后的Cookie请求"""
        yield Request('https://passport.xiaohulu.com/editpw',meta={'cookiejar':True},callback=self.next2)

    def next2(self,response):
        # 请求Cookie
#        Cookie3 = response.request.headers.getlist('Cookie')
#        print '查看需要登录才可以访问的页面携带Cookies：',Cookie3
        a = response.body
        print "########登录后可以查看一下登录响应信息next2########################"
        print a
        item = PassportItem()
        item["passwd"] = response.xpath('/html/body/div[1]/div/form/div/div[1]/label/text()').extract()[0]  #得到个人中心页面
        item["newpasswd"] = response.xpath('/html/body/div[1]/div/form/div/div[2]/label/text()').extract()[0]  #得到个人中心页面
        yield item
#        passwd= response.xpath('/html/body/div[1]/div/form/div/div[1]/label/text()').extract()[0]  #得到个人中心页面
#        newpasswd = response.xpath('/html/body/div[1]/div/form/div/div[2]/label/text()').extract()[0]  #得到个人中心页面
#        print "################################################"
#        print passwd
#        print newpasswd
