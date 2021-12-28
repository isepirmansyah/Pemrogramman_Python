print('------------ Selamat Datang di Toko Kami -------------')
print('Barang Yang Tersedia'
      '\n1.Televisi'
      '\n2.AC'
      '\n3.Kulkas'
      '\n4.Mesin Cuci'
      '\n5.Kipas Angin')

barang = int(input('Masukan Barang Yang Hendak di Beli : '))
jumlah_barang = int(input('Masukan Jumlah Barang : '))
nama_pelanggan = str(input('Masukan Nama Anda : '))

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


print('\n')
print('Terimakasih Telah Berbelanja di Toko Kami\nBerikut Data Pembelian Anda')
print("Nama Pelanggan\t:",nama_pelanggan,
      "\nNama Produk\t:",jenis,
      "\nHarga Produk\t:",harga,
      "\nJumlah Beli\t:",jumlah_barang,
      "\nHarga Kotor\t:",harga_kotor,
      "\nDiskon\t\t:",diskon,
      "\nPPN 10%\t\t:",ppn,
      "\nHarga Bersih\t:",harga_bersih )