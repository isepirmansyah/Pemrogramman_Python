nama = 'Isep Irmansyah'
matpel = 'Matematika'
nilai = 78

if (nilai >= 85 and nilai <= 100):
    ket = "Grade A"
elif (nilai >= 75 and nilai < 85):
    ket = "Grade B"
elif (nilai >= 60 and nilai < 75):
    ket = "Grade C"
elif (nilai >= 30 and nilai < 60):
    ket = "Grade D"
else:
    ket = "Grade E"

print('Nama Siswa \t:', nama,
      '\nMata Pelajaran \t:', matpel,
      '\nNilai \t\t:', nilai,
      '\nKeterangan \t:', ket)
