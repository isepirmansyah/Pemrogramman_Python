import pymysql
db = pymysql.connect(host = "localhost", user = "root", passwd = "", database = "db_pyhton")

# Insert data
def insert_data(db):
    nama = input("Nama Barang: ")
    harga = float(input("Harga Barang: ")) 
    val = (nama,harga)
    cursor = db.cursor()
    sql = "INSERT INTO barang(nama,harga) VALUES (%s,%s)"
    cursor.execute(sql,val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))
    
# Show data
def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
            
            
# Update data
def update_data(db):
    cursor = db.cursor()
    show_data(db)
    nama = input("Barang Baru: ")
    harga = float(input("Harga Baru: "))    
    id = int(input("ID Barang yang akan diubah: "))
    sql = "UPDATE barang SET nama=%s,harga=%s WHERE id=%s"
    val = (nama,harga,id)
    cursor.execute(sql,val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


# Delete data
def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id = int(input("ID Barang yg akan dihapus: "))
    sql = "DELETE FROM barang WHERE id=%s"
    cursor.execute(sql,id)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


# Cari data
def search_data(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM barang WHERE nama LIKE %s OR harga LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)

# Menu data
def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")
    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")
        
# Run app       
if __name__ == "__main__":
    while(True):
        show_menu(db)


