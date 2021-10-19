print('Selamat Datang di Aplikasi Kalkulator Sederhana')
print('Pilih Sistem Operasi \n1.Penjumlahan \n2.Pengurangan')

so = int(input('Masukan Sistem Pemjumlahan : '))
if (so == 1):
    angka1 = int(input('Masukan angka pertama :'))
    angka2 = int(input('Masukan angka kedua :'))
    hasil = angka1 + angka2
    print('Hasil Penjumlahan dari', angka1, '+', angka2, 'adalah :', hasil)
elif (so == 2):
    angka1 = int(input('Masukan angka pertama :'))
    angka2 = int(input('Masukan angka kedua :'))
    hasil = angka1 - angka2
    print('Hasil Penjumlahan dari', angka1, '-', angka2, 'adalah :', hasil)
