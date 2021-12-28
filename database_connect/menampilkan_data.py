import pymysql as mdb

db = mdb.connect(host = "localhost", user = "root", passwd = "", database = "db_pyhton")

cursor =  db.cursor()
sql = "SELECT * FROM barang"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)
