ar_buah = ['jeruk','mangga','pisang','jambu','apel']
ar_buah[2] = 'manggis'
del ar_buah[4]

print('Buah Index ke 2 :',ar_buah)

#tambah list
ar_buah.insert(0,'Kedongdong')
ar_buah.append('kukun')

#cetak list dengan looping
for buah in ar_buah:
    print('Buah',buah)

#memotong list di tengah
print('Memotong List buah index 1 - 4 :',ar_buah[1:4])



