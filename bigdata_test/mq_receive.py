# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:13:59 2019

@author: Brianzhu
"""

#import pika
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
#channel.queue_declare(queue='hello')
#
#def callback(ch, method, properties, body):
#     print " [x] Received %r" % (body)
# 
# # 告诉rabbitmq使用callback来接收信息
##channel.basic_consume(callback,queue='hello',no_ack=True)
#channel.basic_consume('test',callback,auto_ack=True)
# 
## 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理,按ctrl+c退出
#print ' [*] Waiting for messages. To exit press CTRL+C'
#channel.start_consuming()





from rb_mq import RabbitMQ

# RabbitMQ类的初始化参数，包括broker_ip, port, username, password, vhost
args = ("192.168.120.173", 5672, "admin", "admin01", "/")
mq = RabbitMQ(*args)  # 传入初始化参数
mq.connect()   # 调用connect方法，连接broker

mq.getting_start('test')  # 调用getting_start方法从queue中获取data， 传入的参数是queue_name