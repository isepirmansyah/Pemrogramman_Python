judul = '------------- SLIP GAJI PT. AnggiNovita ---------------\n'
nama_pegawai1 = 'Ahmad'
agama1 = 'Islam'
jumlah_anak1 = 2
gaji_pokok1 = 4000000
tunjangan_jabatan1 = ( 20/100 * gaji_pokok1)
nama_pegawai2 = 'Alex'
agama2 = 'Kristen Protestan'
jumlah_anak2 = 5
gaji_pokok2 = 6000000
tunjangan_jabatan2 = ( 20/100 * gaji_pokok2)


if (jumlah_anak1 < 1):
    tunjangan_keluarga1 = 0
elif (jumlah_anak1 >= 1 and jumlah_anak1 <= 2):
    tunjangan_keluarga1 = (10/100 * gaji_pokok1)
elif (jumlah_anak1 > 2):
    tunjangan_keluarga1 = (20/100 * gaji_pokok1)


if (jumlah_anak2 < 1):
    tunjangan_keluarga2 = 0
elif (jumlah_anak2 >= 1 and jumlah_anak2 <= 2):
    tunjangan_keluarga2 = (10/100 * gaji_pokok2)
elif (jumlah_anak2 > 2):
    tunjangan_keluarga2 = (20/100 * gaji_pokok2)
    

gaji_kotor = [gaji_pokok1 + tunjangan_jabatan1 + tunjangan_keluarga1 , gaji_pokok2 + tunjangan_jabatan2 + tunjangan_keluarga2]

zakat_propesi = [(0, 0.025)[agama1 == 'Islam' and gaji_kotor[0] >= 6000000] * gaji_pokok1 ,(0, 0.025)[agama2 == 'Islam' and gaji_kotor[1] >= 6000000] * gaji_pokok2]

gaji_bersih = [gaji_kotor[0] - zakat_propesi[0] , gaji_kotor[1] - zakat_propesi[1] ]

print('\n')
print(judul)
print('Nama Pegawai \t\t:' , nama_pegawai1)
print('Agama \t\t\t:' , agama1)
print('Jumlah Anak \t\t:' , jumlah_anak1)
print('Gaji Pokok \t\t:' , gaji_pokok1)
print('Tunjangan Jabatan \t:' , tunjangan_jabatan1)
print('Tunjangan Keluarga \t:' , tunjangan_keluarga1)
print('Gaji Kotor \t\t:' , gaji_kotor[0])
print('Jakat Profesi \t\t:' , zakat_propesi[0])
print('Take Home Pay \t\t:' , gaji_bersih[0])

print('\n')
print(judul)
print('Nama Pegawai \t\t:' , nama_pegawai2)
print('Agama \t\t\t:' , agama2)
print('Jumlah Anak \t\t:' , jumlah_anak2)
print('Gaji Pokok \t\t:' , gaji_pokok2)
print('Tunjangan Jabatan \t:' , tunjangan_jabatan2)
print('Tunjangan Keluarga \t:' , tunjangan_keluarga2)
print('Gaji Kotor \t\t:' , gaji_kotor[1])
print('Jakat Profesi \t\t:' , zakat_propesi[1])
print('Take Home Pay \t\t:' , gaji_bersih[1])