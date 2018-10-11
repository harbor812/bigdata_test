#!/usr/bin/env python

import sys
from pyhive import hive
import MySQLdb

class HiveClient:

    def __init__(self, db_host, hdatabase, husername,hport=10000):
        """
        create connection to hive server
        """
        self.conn = hive.Connection(host=db_host,   port=hport,  database=hdatabase,username=husername)

    def query(self, sql):
        """
        query
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        return res

    def close(self):
        """
        close connection
        """
        self.conn.close()


class MysqlClient:
    def __init__(self, mdb):
        self.conn = MySQLdb.connect (host = "113.107.166.5",   user = "root",  passwd = "rp1qaz@WSX",  port=11606,db = mdb)
    def insert(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close ()
        self.conn.commit()

    def close(self):
        self.conn.close ()

def dhive():
#    try:
        hcon = HiveClient('192.168.120.160', 'parquet', 'hdfs','10000' )
        mcon = MysqlClient('test')
        res = hcon.query("SELECT platform_id,room_id,video_desc,video_share_url,video_digg_count,video_share_count,video_id,video_tag,video_url,video_duration,comment_count,music_id,video_location_name,music_title,create_time,plat FROM live_show_video limit 1000000")
        hcon.close()
#        print (res)
        for item in res:
            sql = """ insert  into live_show_video (platform_id,room_id,video_desc,video_share_url,video_digg_count,video_share_count,video_id,video_tag,video_url,video_duration,comment_count,music_id,video_location_name,music_title,create_time,plat) value( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """%( item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15])
            mcon.insert(sql)
        mcon.close()

#    except Exception:
#        print ('excepion')

if __name__ == "__main__":
   dhive()
