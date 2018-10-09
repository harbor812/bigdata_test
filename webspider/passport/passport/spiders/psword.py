# -*- coding: utf-8 -*-
import scrapy
from passport.items import PassportItem
from scrapy.http import FormRequest



class PswordSpider(scrapy.Spider):
    name = "psword"
    allowed_domains = ["passport.xiaohulu.com"]
    start_urls = ['https://passport.xiaohulu.com/me']
    
    headers={
            "Host": "passport.xiaohulu.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
#            Cookie: 6N3e_f2ec___XHLTXZ__www=516bTi9pxwbnr%2BTD60SAFn7H56ukRQGR5k8sFCjqQV5a6p0gv8BJanuxyjmVjpva9eOPngMxAH93jNj%2F5kvqJ9%2BqlKm36e%2FwfSVSYNmuAdJTZgVZ1uREQaPaCecP9EYt6PSgrSGHII7cbHj9DIU7gGc; 6N3e_f2ec_auth=f2d0OJBwMGXu%2BZHHiW1ankZvjId1%2BvZNinkdDwYD3lO8%2F%2B40NtbI7uQtqFzg9efeLs8YbE%2BJ43SbCkKNd44gHxnTPv2ZgTDSDZ0YC0zU; Hm_lvt_df9403e4b025ecf85b4310bda73ab65e=1531278211,1531278235,1531363105,1531363498; 6N3e_f2ec_saltkey=P4r4VpMR; 6N3e_f2ec_lastvisit=1535086387; Hm_lvt_2772005b8bc0b193d080228322981977=1534832621; Hm_lvt_1c358b33dfa30c89dd3a1927a5921793=1534832621; 6N3e_f2ec___XHLTXZ__www_my="cae706ANqO5yZtrgZ/VklIwYge8ZcIBrt9XzCW4/Q5l1Wd3JBpOu5kRQ0ZQxLvrXUzmJsiKb3EeX5JguF4SkQIbasLirReFdyPh/4w=="; XSRF-TOKEN=eyJpdiI6Im9FTHRkRjc3bkJiYTBEY0xmRW4zOUE9PSIsInZhbHVlIjoiblhYOTBYQllVZUlIcW92WWNvTjg3SHVyYm54WHFuVjVXeCszd3JBU1Jvb2hlTWRjdHVyQVhBQzA5dEVoaGlTQ1wvWW9CeUNjRVZiSFRsTFpQZmJINmhBPT0iLCJtYWMiOiJhZDMwNGY1OTA1YTU3ODM1MTdkZTBjYTUzZDZmMjQ1ZWM0ZmQ1OTMyNjI5YTNlOTAxZGEyNzY0ZGE4OTJlNzQzIn0%3D; laravel_session=eyJpdiI6IjR1RHZcL0VFbDlERWFieElxdlhoWmd3PT0iLCJ2YWx1ZSI6InVlQ3FXOFZqdXpndEJmdWpMcDd4TjI2MHF5K2VWOVwvc1lNeTc0N0xjVjdXaE5UWjA3T3dtSGg4dWxkVGlNSjBsQ0U4MFNnZ1NFQXBGU0w5WDl0YUhoUT09IiwibWFjIjoiM2UyZTg5YTY4MGE5NDljZTY4YmU5M2FhNDk1OGM0MGVlMTczMzIyNGZiMmY0N2QyYjU5NGI2MWVlODI3OTljZiJ9; Hm_lvt_afc61e0a3581591fec36a81263bcfe5d=1535089955,1535339670; Hm_lpvt_afc61e0a3581591fec36a81263bcfe5d=1536057965

            }    




def start_requests(self):

#    t = str(int(time.time() * 1000))
    captcha_url = 'https://passport.xiaohulu.com/'
    return [scrapy.Request(url=captcha_url, headers=self.header, callback=self.parser_captcha)]


    def parse(self, response):
        pass
