print("-----------perkalian-----------------")
angka = float(input("Masukkan angka : "))
hasil = 10 * angka
print("Perkalian 10 x ",angka," = ",hasil)
print("Perkalian 10 x %.2f = %.2f" % (angka,hasil))

print("-----------banyak inputan-----------------")

nama = input("Input Nama :")
gender = str(input('Input Gender :'))
umur = int(input("Input Umur :"))
beratBadan = float(input("Berat Badan :"))

print('Nama\t\t: %s'
      '\nJenis Kelamin\t: %s'
      '\nUmur\t\t: %i Tahun'
      '\nBerat Badan\t: %.2f Kg'
      % (nama,gender,umur,beratBadan)
      )