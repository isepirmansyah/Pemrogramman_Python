nama = input("Masukan Nama Anda :")
matpel = 'Matematika'
nilai = int(input("Masukan Nilai Anda :"))

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

print('Hasil Pembelajaran Siswa')
print('Nama Siswa \t:', nama,
      '\nMata Pelajaran \t:', matpel,
      '\nNilai \t\t:', nilai,
      '\nKeterangan \t:', ket)
