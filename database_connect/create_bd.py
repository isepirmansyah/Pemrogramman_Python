import pymysql
db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# membuat database
cursor = db.cursor()
cursor.execute("CREATE DATABASE db_pyhton")

print("DB Sukses di Buat")