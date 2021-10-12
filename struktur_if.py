# deklarasi dan inisialaisasi variabel
# deklarasi = pelanggan
# inisialisasi = "Budi Santoso"
pelanggan = "Budi Santoso"
totalBelanja = 150000
batasHadiah = 100000

# struktur kendali if
if totalBelanja > batasHadiah:
    keterangan = "Selamat anda mendapatkan diskon"
else:
    keterangan = "terimakasih sudah belanja"

# ternery di php
# keterangan = (totalBelanja > batasHadiah) ? "selamat anda mendapatkan diskon": "terimakasih sudah belanja"

# cetak data
print('Pelanggan', pelanggan, '\nTotal belanja anda Rp.',
      totalBelanja, '\n', keterangan)

# Siswa dinyatakan lulus minimal 60 nilainya
nama = 'Gunawan Hadi'
matpel = 'Matematika'
nilai = 70.99

# ternary
keterangan = "Lulus" if nilai >= 60 else "Gagal"

# cetak data
print('Nama Siswa \t:', nama,
      '\nMata Pelajaran \t:', matpel,
      '\nNilai \t\t:', nilai,
      '\nKeterangan \t:', keterangan)
