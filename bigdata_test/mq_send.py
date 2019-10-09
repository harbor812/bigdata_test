# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:04:43 2019

@author: Brianzhu
"""

#import pika
#import random
# 
# # 新建连接，rabbitmq安装在本地则hostname为'localhost'
#hostname = '192.168.120.173'
#credentials=pika.PlainCredentials('admin','admin01')
## # 四个参数分别是  BrokerIP  BrokerPort, Vhost, username_and_password, 心跳时间间隔
#parameters = pika.ConnectionParameters(hostname,5672,'/',credentials=credentials)
#
#connection = pika.BlockingConnection(parameters)
#
# # 创建通道
#channel = connection.channel()
## 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
#channel.queue_declare(queue='hello')
# 
#number = random.randint(1, 1000)
#body = 'hello world:%s' % number
# # 交换机; 队列名,写明将消息发往哪个队列; 消息内容
## routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列
#channel.basic_publish(exchange='', routing_key='hello', body=body)
#print " [x] Sent %s" % body
#connection.close()

#from rb_mq import RabbitMQ
#import random
## RabbitMQ类的初始化参数，包括broker_ip, port, username, password, vhost
#args = ("192.168.120.173", 5672, "admin", "admin01", "/")
#mq = RabbitMQ(*args)  # 传入初始化参数,*聚合成元组，**聚合成字典
#mq.connect()   # 调用connect方法，连接broker
#number = random.randint(1, 1000)
#body = 'hello world:%s' % number
## 调用put方法，向目标queue中发送数据， 第一个参数是data, 第二个参数是queue_name, 第三个参数是route_name
#mq.put(body, "test", "test") 
#
## 发完数据，主动关闭连接
#mq.close()


from rb_mq import RabbitMQ

# RabbitMQ类的初始化参数，包括broker_ip, port, username, password, vhost
args = ("192.168.120.173", 5672, "admin", "admin01", "/")
mq = RabbitMQ(*args)  # 传入初始化参数
mq.connect()   # 调用connect方法，连接broker

mq.getting_start('test')  # 调用getting_start方法从queue中获取data， 传入的参数是queue_name
