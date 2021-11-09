nilai = {'Firda':89, 'Inaya':100, 'Deden':59, 'Fazwa':95}
print('Data Nilai : ',nilai)
print("\n------------cetak valuenya saja---------------------\n")
#cetak nilai saja
for skor in nilai.values():
    print('Data Nilai : ',skor)
print("\n------------cetak key aja---------------------\n")
#cetak nama saja
for nama in nilai.keys():
    print('data siswa : ',nama)
print("\n------------cetak key dan values------------------\n")
#cetak key dan value secara bersamaan / manual
for nama,nilai in nilai.items():
    print('Nama Siswa : %s \t Nilai : %i' % (nama,skor))
    
#mengubah value
#nama_dic['kunci'] = 'Nilai'

#menghapus nilai Ina
nilai.pop('Ina')

#menghapus nilai Zaki
del nilai['Deden']
