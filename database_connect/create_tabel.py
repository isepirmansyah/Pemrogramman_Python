import pymysql
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_pyhton"
)

sursor = db.cursor()
sql = """CREATE TABLE barang (id INT AUTO_INCREMENT PRIMARY KEY, 
nama VARCHAR(45),
harga DOUBLE)"""

sursor.execute(sql)

print("Tabel Sukses di Buat")