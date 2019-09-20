# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:26:25 2019

@author: Brianzhu
"""
from thrift.transport import TSocket,TTransport
from thrift.protocol import TCompactProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor, Mutation, BatchMutation, TRegionInfo
from hbase.ttypes import IOError, AlreadyExists

# thrift默认端口是9090
socket = TSocket.TSocket('113.107.166.14',13100)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TCompactProtocol.TCompactProtocol(transport)

client = Hbase.Client(protocol)
socket.open()

client.getTableNames()
#print client.getTableNames()
#print client.get('test','row1','cf:a')





