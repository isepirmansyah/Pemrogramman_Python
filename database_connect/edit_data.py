import pymysql as mdb

db = mdb.connect(
host = "localhost", user = "root",
passwd = "", database = "db_pyhton"
)

cursor = db.cursor()
sql = "UPDATE barang SET nama=%s, harga=%s WHERE id=%s"
val = ("Sofa", 2000000, 1)
cursor.execute(sql, val)
db.commit()
print("{} data diubah".format(cursor.rowcount))
