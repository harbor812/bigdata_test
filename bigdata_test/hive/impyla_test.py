from impala.dbapi import connect
from impala.util import as_pandas

conn=connect(host='192.168.120.160',port=10000, database="parquet", user='hdfs', password='hdfs', auth_mechanism="PLAIN")
cur=conn.cursor()
cur.execute('SELECT * FROM live_show_video limit 10')
#data=as_pandas(cur.fetchall())
#print(data)

for result in cur.fetchall():
	print (result)
print (cur.fetchall())
conn.close()
