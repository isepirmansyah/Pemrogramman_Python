# Program aplikasi sederhana Tugas 1 Isep Irmansyah
title = 'SLIP GAJI PT. XYJ\n---------------'
nama_pegawai = ['Ahmad', 'Alex']
agama = ['Islam', 'Kristen Protestan']
jumlah_anak = [2, 5]
gaji_pokok = [4000000, 6000000]
tunjangan_jabatan1 = ( 20/100 * gaji_pokok[0])
tunjangan_jabatan2 = ( 20/100 * gaji_pokok[1])



if (jumlah_anak[0] < 1):
    tunjangan_keluarga1 = 0
elif (jumlah_anak[0] >= 1 and jumlah_anak[0] <= 2):
    tunjangan_keluarga1 = (10/100 * gaji_pokok[0])
elif (jumlah_anak[0] > 2):
    tunjangan_keluarga1 = (20/100 * gaji_pokok[0])


if (jumlah_anak[1] < 1):
    tunjangan_keluarga2 = 0
elif (jumlah_anak[1] >= 1 and jumlah_anak[1] <= 2):
    tunjangan_keluarga2 = (10/100 * gaji_pokok[1])
elif (jumlah_anak[1] > 2):
    tunjangan_keluarga2 = (20/100 * gaji_pokok[1])
    

gaji_kotor = [gaji_pokok[0] + tunjangan_jabatan1 + tunjangan_keluarga1 , gaji_pokok[1] + tunjangan_jabatan2 + tunjangan_keluarga2]

zakat_propesi = [(0, 0.025)[agama[0] == 'islam' and gaji_kotor[0] >= 6000000] * gaji_pokok[0] ,(0, 0.025)[agama[1] == 'islam' and gaji_kotor[1] >= 6000000] * gaji_pokok[1]]

gaji_bersih = [gaji_kotor[0] - zakat_propesi[0] , gaji_kotor[1] - zakat_propesi[1] ]

print('')
print(title)
print('Nama Pegawai \t\t:' , nama_pegawai[0])
print('Agama \t\t\t:' , agama[0])
print('Jumlah Anak \t\t:' , jumlah_anak[0])
print('Gaji Pokok \t\t:' , gaji_pokok[0])
print('Tunjangan Jabatan \t:' , tunjangan_jabatan1)
print('Tunjangan Keluarga \t:' , tunjangan_keluarga1)
print('Gaji Kotor \t\t:' , gaji_kotor[0])
print('Jakat Profesi \t\t:' , zakat_propesi[0])
print('Take Home Pay \t\t:' , gaji_bersih[0])

print('')
print(title)
print('Nama Pegawai \t\t:' , nama_pegawai[1])
print('Agama \t\t\t:' , agama[1])
print('Jumlah Anak \t\t:' , jumlah_anak[1])
print('Gaji Pokok \t\t:' , gaji_pokok[1])
print('Tunjangan Jabatan \t:' , tunjangan_jabatan2)
print('Tunjangan Keluarga \t:' , tunjangan_keluarga2)
print('Gaji Kotor \t\t:' , gaji_kotor[1])
print('Jakat Profesi \t\t:' , zakat_propesi[1])
print('Take Home Pay \t\t:' , gaji_bersih[1])