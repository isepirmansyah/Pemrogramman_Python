print("----------luas bidang------------")
print("Pilih Bidang:"
      "\n1.Lingkaran"
      "\n2.Segitiga"
      "\n3.Persegi Panjang")

pilihan = int(input("Pilih No. Bidang:"))
if (pilihan == 1):
    bidang = 'Lingkaran'
    jari2 = float(input('Masukan jari2 :'))
    luas = 3.14 * jari2 * jari2
    print('Bidang %s dengan jari2 %.2f luasanya adalah = %.2f' % (bidang,jari2,luas))
elif (pilihan == 2):
    bidang = 'Segitiga'
    alas = float(input('Masukan Alas :'))
    tinggi = float(input('Masukan Tinggi :'))
    luas = 1/2 * alas * tinggi
    print("Bidang %s dengan alas %.2f dan tinggi %.2f luasnya = %.2f" % (bidang,alas,tinggi,luas))
elif (pilihan == 3):
    bidang = 'Persegi Panjang'
    p = float(input('Masukan Panjang :'))
    l = float(input('Masukan Lebar :'))
    luas = p * l
    print("Bidang %s dengan panjang %.2f dan lebar %.2f luasnya = %.2f" % (bidang,p,l,luas))
else:
    print("No. Bidang yang Anda pilih tidak ada")