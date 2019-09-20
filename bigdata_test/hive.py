# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 18:44:30 2018

@author: Brianzhu
"""


#from impala.dbapi import connect
##需要注意的是这里的auth_mechanism必须有，默认是NOSASL，但database不必须，user也不必须
##conn = connect(host='服务器ip', port=10000, database='default',auth_mechanism='NOSASL',user='在hdfs-site中设定的用户名（如果不懂，请看https://blog.csdn.net/a6822342/article/details/80697919）')
#conn = connect(host='192.168.120.160', port=10000,auth_mechanism='NOSASL',user='hdfs',password='hdfs')
#
#
#cur = conn.cursor()
# 
#cur.execute('SHOW DATABASES')
#print(cur.fetchall())
# 
#cur.execute('SHOW Tables')



#from pyhive import hive
#conn = hive.Connection(host='192.168.120.160', port=10000, username='hdfs', database='default')
#cursor=conn.cursor()
#cursor.execute("""SELECT * FROM live_show_music where date='20180903' order by timestamp desc limit 10""")
#for result in cursor.fetchall():
#    print result




#import pyhs2
#with pyhs2.connect(host='192.168.120.160',
#                   port=10000,
#                   # authMechanism='NONE',
#                   authMechanism='NOSASL',
#                   user='hdfs',
#                   password='hdfs',
#                   database='default')as conn:
#    with conn.cursor() as cur: 
#        print cur.getDatabases()
#        cur.execute("show databases")
#        for i in cur.fetch():
#                print i





import prestodb
conn=prestodb.dbapi.connect(
    host='113.107.166.14',
    port=28080,
    user='root',
#    catalog='the-catalog',
#    schema='the-schema',
)
cur = conn.cursor()
cur.execute('select count(m.platform_id) as n  from  (select  distinct platform_id, from_id  FROM hive.parquet.audience_statistics_info WHERE all_time_gift_value > 5000.0 ) m')
rows = cur.fetchall()

print rows
#import pyhs2
#
#
#
#class HiveClient:
#
#    def __init__(self, db_host, user, password, database, port=10000, authMechanism="PLAIN"):
#
#        """
#
#        create connection to hive server2
#
#        """
#
#        self.conn = pyhs2.connect(host=db_host,
#
#                                  port=port,
#
#                                  authMechanism=authMechanism,
#
#                                  user=user,
#
#                                  password=password,
#
#                                  database=database,
#
#                                  )
#
#
#
#    def query(self, sql):
#
#        """
#
#        query
#
#        """
#
#        with self.conn.cursor() as cursor:
#
#            cursor.execute(sql)
#
#            return cursor.fetch()
#
#
#
#    def close(self):
#
#        """
#
#        close connection
#
#        """
#
#        self.conn.close()
#
#
#
#
#
#def main():
#
#    """
#
#    main process
#
#    @rtype:
#
#    @return:
#
#    @note:
#
#
#
#    """
#
#    hive_client = HiveClient(db_host='192.168.120.160', port=10000, user='hdfs', password='hdfs',
#
#                             database='default', authMechanism='PLAIN')
#
#    result = hive_client.query("""SELECT * FROM live_show_music where date='20180903' order by timestamp desc limit 10""")
#
#    print result
#
#    hive_client.close()
#
#
#
#
#
#if __name__ == '__main__':
#
#    main()