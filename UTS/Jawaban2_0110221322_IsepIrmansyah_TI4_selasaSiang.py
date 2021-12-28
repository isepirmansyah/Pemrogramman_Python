# ====================================================================================
# ====================================================================================
# ======================= UTS DDP ISEP IRMANSYAH TI-14 SOAL 2 ========================
# =================== APLIKASI SEDERHANA PENJUALAN BARANG ONLINE =====================
# ======================== Copyright 2021 @isep_irmansyah ============================
# ====================================================================================
# ====================================================================================

# Judul
title = '====================================================\n-------- SELAMAT DATANG DI TOKO ISEP TRONIK --------\n===================================================='
foot = '====================================================\n---- Terimakasih Telah Berbelanja di Toko Kami -----\n===================================================='

print(title)

# List Barang Yang Tersedia 
print('Barang - Barang Yang Tersedia di Toko Kami'
      ' \n1.Televisi\tRp2.000.000'
      ' \n2.AC\t\tRp4.000.000'
      ' \n3.Kulkas\tRp5.000.000'
      ' \n4.Mesin Cuci\tRp3.000.000'
      ' \n5.Kipas Angin\tRp1.000.000\n')

# Input Data Beli dan Pelanggan
print('Silahkan Masukan atau Input Barang Yang Hendak Anda Beli!!')
nama_pembeli = str(input('Masukan Nama Anda : '))
barang_beli = str(input('Masukan Barang Yang Hendak di Beli : '))
jumlah_barang = int(input('Masukan Jumlah Barang : '))
keterangan = str

if (barang_beli == '1' or barang_beli == 'Televisi' or barang_beli == 'televisi'):
    jenis = 'Televisi'
    harga = 2000000
    harga_kotor = jumlah_barang * harga
    diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 0.1)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang_beli == '2' or barang_beli == 'AC' or barang_beli == 'ac'):
    jenis = 'AC'
    harga = 4000000
    harga_kotor = jumlah_barang * harga
    if (jumlah_barang >= 3):
        diskon = 0.1 * harga_kotor
    else:
        diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 0.1)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang_beli == '3' or barang_beli == 'Kulkas' or barang_beli == 'kulkas'):
    jenis = 'Kulkas'
    harga = 5000000
    harga_kotor = jumlah_barang * harga
    if (jumlah_barang >= 5):
        diskon = 20/100 * harga_kotor
    else:
        diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 0.1)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang_beli == '4' or barang_beli == 'Mesin Cuci' or barang_beli == 'mesin cuci'):
    jenis = 'Mesin Cuci'
    harga = 3000000
    harga_kotor = jumlah_barang * harga
    diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 0.1)
    harga_bersih = harga_kotor - diskon + ppn
elif (barang_beli == '5' or barang_beli == 'Kipas Angin' or barang_beli == 'kipas angin'):
    jenis = 'Kipas Angin'
    harga = 1000000
    harga_kotor = jumlah_barang * harga
    diskon = 5/100 * harga_kotor
    ppn = ((harga_kotor - diskon) * 0.1)
    harga_bersih = harga_kotor - diskon + ppn
else:
    keterangan = 'Barang Yang Anda Masukan Tidak Terdaptar di Barang Kami'
    
print('')
print("Complete...........................................................")
print('')


# Cek Inputan barang 
if (keterangan == 'Barang Yang Anda Masukan Tidak Terdaptar di Barang Kami'):
    print(keterangan)
else:
    print(foot , '\n')
    print('Berikut Data Pembelian Yang Anda Pilih')
    print("Nama Pelanggan\t:" , nama_pembeli,
      "\nNama Produk\t:" , jenis,
      "\nHarga Produk\t:" , harga,
      "\nJumlah Beli\t:" , jumlah_barang,
      "\nHarga Kotor\t:" , harga_kotor,
      "\nDiskon\t\t:" , diskon,
      "\nPPN 10%\t\t:" , ppn,
      "\nHarga Bersih\t:" , harga_bersih )
    
    
    



 

