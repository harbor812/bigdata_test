from pyhive import hive

#SQL="SELECT platform_id,room_id FROM live_show_video WHERE platform_id=201 AND room_id = '56630472225' AND create_time >= 1534435200 AND create_time < 1535040000 AND date = '20180823'"
SQL="""SELECT platform_id,room_id,video_desc,create_time  FROM live_show_video WHERE platform_id=201 AND create_time >= 1534435200 AND create_time < 1535040000 """
#SQL="SHOW TABLES"


conn = hive.Connection(host='192.168.120.160', port=10000, username='hdfs', password='hdfs',database='parquet',auth='LDAP')#host主机ip,port：端口号，username:用户名，database:使用的数据库名称
cursor=conn.cursor()
cursor.execute(SQL)#执行查询
for result in cursor.fetchall():
	print(result)
