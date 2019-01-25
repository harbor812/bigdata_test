# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:38:58 2018

@author: Brianzhu
"""

from flask import Flask
from flask_cache import Cache
import configparser


config=configparser.ConfigParser()
config.read("redis_config.ini")


ip=config.get("test","IP")
port=config.get("test","port")

cache = Cache()

config = {
  'CACHE_TYPE':'redis',
  'CACHE_REDIS_HOST':ip,
  'CACHE_REDIS_PORT':port,
  'CACHE_REDIS_DB':'',
  'CACHE_REDIS_PASSWORD':''
}

app = Flask(__name__)
#app.config.from_object(config)
cache.init_app(app,config)

@app.route('/')
@cache.cached(timeout=60*2)
def index():
  name = 'mink'
  return name

if __name__ == '__main__':
    app.run(host = '0.0.0.0',
        port = 6002,  
        debug = True )