import pymysql
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_pyhton"
)

cursor = db.cursor()
sql = "INSERT INTO barang (nama, harga) VALUES (%s, %s)"
val = ('Lemari', 1000000)
cursor.execute(sql, val)

db.commit()
print("{} data di tambahkan" .format(cursor.rowcount))