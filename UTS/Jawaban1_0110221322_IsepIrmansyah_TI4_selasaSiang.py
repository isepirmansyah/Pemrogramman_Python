# ====================================================================================
# ====================================================================================
# ======================= UTS DDP ISEP IRMANSYAH TI-14 SOAL 1 ========================
# ================== APLIKASI SEDERHANA PERHITUNGAN GAJI KARYAWAN ====================
# ======================== Copyright 2021 @isep_irmansyah ============================
# ====================================================================================
# ====================================================================================

# Judul
title = '============================================\n-------- Slip Gaji PT. ISEP TRONIK ---------\n============================================'


# Data Pegawai
nama_pegawai = ['Ahmad' , 'Alex']
agama = ['Muslim' , 'Kristen Protestan']
gaji_pokok = [4000000 , 6000000]
jumlah_anak = [2 , 5]
tunjangan_jabatan1 = ( 0.2 * gaji_pokok[0])
tunjangan_jabatan2 = ( 0.2 * gaji_pokok[1])

# Tunjangan Keluarga Pegawai 1
if (jumlah_anak[0] < 1):
    tunjangan_keluarga1 = 0
elif (jumlah_anak[0] >= 1 and jumlah_anak[0] <= 2):
    tunjangan_keluarga1 = (0.1 * gaji_pokok[0])
elif (jumlah_anak[0] > 2):
    tunjangan_keluarga1 = (0.2 * gaji_pokok[0])

# Tunjangan Keluarga Pegawai 2
if (jumlah_anak[1] < 1):
    tunjangan_keluarga2 = 0
elif (jumlah_anak[1] >= 1 and jumlah_anak[1] <= 2):
    tunjangan_keluarga2 = (0.1 * gaji_pokok[1])
elif (jumlah_anak[1] > 2):
    tunjangan_keluarga2 = (0.2 * gaji_pokok[1])
 
# Gaji Kotor, Zakat, Gaji Bersih   
gaji_kotor = [gaji_pokok[0] + tunjangan_jabatan1 + tunjangan_keluarga1 , gaji_pokok[1] + tunjangan_jabatan2 + tunjangan_keluarga2]

zakat_propesi = [(0, 0.025)[agama[0] == 'Islam' and gaji_kotor[0] >= 6000000] * gaji_pokok[0] ,(0, 0.025)[agama[1] == 'Islam' and gaji_kotor[1] >= 6000000] * gaji_pokok[1]]

gaji_bersih = [gaji_kotor[0] - zakat_propesi[0] , gaji_kotor[1] - zakat_propesi[1]]


print('===================================================================================='
    '\n======================= UTS DDP ISEP IRMANSYAH TI-14 SOAL 1 ========================'
    '\n================== APLIKASI SEDERHANA PERHITUNGAN GAJI KARYAWAN ===================='
    '\n======================== Copyright 2021 @isep_irmansyah ============================'
    '\n====================================================================================')

print('')
print(title)
print('Nama Pegawai \t\t:' , nama_pegawai[0],
    '\nAgama \t\t\t:' , agama[0],
    '\nJumlah Anak \t\t:' , jumlah_anak[0],
    '\nGaji Pokok \t\t:' , gaji_pokok[0],
    '\nTunjangan Jabatan \t:' , tunjangan_jabatan1,
    '\nTunjangan Keluarga \t:' , tunjangan_keluarga1,
    '\nGaji Kotor \t\t:' , gaji_kotor[0],
    '\nJakat Profesi \t\t:' , zakat_propesi[0],
    '\nTake Home Pay \t\t:' , gaji_bersih[0])

print('')
print(title)
print('Nama Pegawai \t\t:' , nama_pegawai[1],
    '\nAgama \t\t\t:' , agama[1],
    '\nJumlah Anak \t\t:' , jumlah_anak[1],
    '\nGaji Pokok \t\t:' , gaji_pokok[1],
    '\nTunjangan Jabatan \t:' , tunjangan_jabatan2,
    '\nTunjangan Keluarga \t:' , tunjangan_keluarga2,
    '\nGaji Kotor \t\t:' , gaji_kotor[1],
    '\nJakat Profesi \t\t:' , zakat_propesi[1],
    '\nTake Home Pay \t\t:' , gaji_bersih[1])


