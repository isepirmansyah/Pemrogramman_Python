import pymysql
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_pyhton"
)

cursor = db.cursor()
sql = "INSERT INTO barang (nama, harga) VALUES (%s, %s)"
brg = [('Bangku', 1000000), ('Meja', 750000)]

for val in brg:  
    cursor.execute(sql, val)
    db.commit()
    
print("data berhasil di tambahkan")