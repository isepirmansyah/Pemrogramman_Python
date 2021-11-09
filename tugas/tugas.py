# Program aplikasi sederhana Tugas 1 Isep Irmansyah
print('----------SELAMAT DATANGG DI APLIKASI PENGAJIAN PT.XYZ---------')
title = 'SLIP GAJI PT. XYJ\n---------------'
nama_pegawai = str(input('Masukan Nama Anda : '))
agama = str(input('Masukan Agama Anda : '))
jumlah_anak = int(input('Masukan Jumlah Anak Anda : '))
gaji_pokok = int(input('Masukan Gaji Pokok Anda : '))
tunjangan_jabatan1 = ( 20/100 * gaji_pokok)
tunjangan_keluarga1 = int 

if (jumlah_anak < 1):
    tunjangan_keluarga1 = 0
elif (jumlah_anak >= 1 and jumlah_anak <= 2):
    tunjangan_keluarga1 = (10/100 * gaji_pokok)
elif (jumlah_anak > 2):
    tunjangan_keluarga1 = (20/100 * gaji_pokok)

    
gaji_kotor = gaji_pokok + tunjangan_jabatan1 + tunjangan_keluarga1 

zakat_propesi = (0, 0.025)[agama == 'islam' and gaji_kotor >= 6000000] * gaji_pokok

gaji_bersih = gaji_kotor - zakat_propesi

print('')
print(title)
print('Nama Pegawai \t\t:' , nama_pegawai)
print('Agama \t\t\t:' , agama)
print('Jumlah Anak \t\t:' , jumlah_anak)
print('Gaji Pokok \t\t:' , gaji_pokok)
print('Tunjangan Jabatan \t:' , tunjangan_jabatan1)
print('Tunjangan Keluarga \t:' , tunjangan_keluarga1)
print('Gaji Kotor \t\t:' , gaji_kotor)
print('Jakat Profesi \t\t:' , zakat_propesi)
print('Take Home Pay \t\t:' , gaji_bersih)
