tup1 = ('PKI 1', 'PKI 2', 1948, 1965)
tup2 = (1, 2, 3, 4, 5)
tup3 = ('Kucing', 'Ikan', 'Sapi', 'Burung')
print('G30S/PKI Tahun :', tup1[3])
print("Bilangan Index Antara 1 dan 5 adalah", tup2[1:5])
print("Binatang Kesayanganku adalah", tup3[0])

#Untuk mengambil panjang atau jumlah item di dalam Tuple, kita bisa menggunakan fungsi len()
buah = ['Mangga','Jambu','Semangka','Rambutan']
print('Jumlah buah ada',len(buah))  

#neste tuple
gorengan = ('Bakwan', 'Cireng', 'Gehu')
sop = ('sop iga','sop butut','sop ayam')
nasi = ('Nasi uduk','Nasi rames','nasi goreng')
#nested tuple
makanan = (gorengan,sop,nasi)
print('-----cetak gorengan------')
print(makanan[0])
print('-----cetak per item------')
print(makanan[1][1])
print(makanan[2][1])
print('-----cetak all makanan------')
print(makanan)

#Siswa dinyatakan lulus minimal 60 nilainya
nama = "Budi Santoso"
matpel = "Matematika"
nilai = 59.99

#tuple & list
keterangan = ('Gagal', 'Lulus')[nilai >= 60]

#cetak data 
print("Nama Siswa \t:",nama,
"\nMata Pelajaran \t:",matpel,
"\nNilai \t\t:",nilai,
"\nKeterangan \t:",keterangan)

