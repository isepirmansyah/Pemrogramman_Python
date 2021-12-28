import pymysql
db = pymysql.connect(
host = "localhost", user = "root",
passwd = "", database = "db_pyhton"
)
cursor = db.cursor()
sql = "DELETE FROM barang WHERE id=%s"
val = (3,)
cursor.execute(sql, val)
db.commit()
print("{} data dihapus".format(cursor.rowcount))
