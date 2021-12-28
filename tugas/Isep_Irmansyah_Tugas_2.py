#Program Aplikasi Sederhana Penjualan Barang Online Created By Isep Irmansyah TI 14
print('------------Selamat Datang di Toko IsepTronik-------------')
print('Barang Yang Tersedia'
      '\n1.Televisi'
      '\n2.AC'
      '\n3.Kulkas'
      '\n4.Mesin Cuci'
      '\n5.Kipas Angin')

print('Masukan Data Diri Anda!!')
nama = str(input('Masukan Nama Anda : '))
barang = int(input('Masukan Barang Yang Hendak di Beli Dalam bentuk angka : '))
jumlah_barang = int(input('Masukan Jumlah Barang : '))

if (barang == 1):
    jenis = 'Televisi'
    harga = 2000000
    harga_kotor = jumlah_barang * harga
    diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 10/100)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang == 2):
    jenis = 'AC'
    harga = 4000000
    harga_kotor = jumlah_barang * harga
    if (jumlah_barang >= 3):
        diskon = 10/100 * harga_kotor
    else:
        diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 10/100)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang == 3):
    jenis = 'Kulkas'
    harga = 5000000
    harga_kotor = jumlah_barang * harga
    if (jumlah_barang >= 5):
        diskon = 20/100 * harga_kotor
    else:
        diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 10/100)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang == 4):
    jenis = 'Mesin Cuci'
    harga = 3000000
    harga_kotor = jumlah_barang * harga
    diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 10/100)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang == 5):
    jenis = 'Kipas Angin'
    harga = 1000000
    harga_kotor = jumlah_barang * harga
    diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 10/100)
    harga_bersih = harga_kotor - diskon + ppn
else:
    print('barang Yang Anda Masukan Tidak Terdaptar di Barang Kami')

print('..................')
print('..................')
print('..................')
print('Terimakasih Telah Berbelanja di IsepTronik\nBerikut Data Pembelian Anda')
print("Nama Pelanggan\t:",nama,
      "\nNama Produk\t:",jenis,
      "\nHarga Produk\t:",harga,
      "\nJumlah Beli\t:",jumlah_barang,
      "\nHarga Kotor\t:",harga_kotor,
      "\nDiskon\t\t:",diskon,
      "\nPPN 10%\t\t:",ppn,
      "\nHarga Bersih\t:",harga_bersih )