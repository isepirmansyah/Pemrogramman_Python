print('=================Cetak Angka 1 - 20=======================')
angka = 20
for no in range(angka):
    no += 1 #no = no + 1
    print('angka = ',no)

print('=================Cetak bilangan Bulat diantara 1 - 20=======================')
angka = 20
for no in range(angka):
    no += 1 #no = no + 1
    if(no % 2 == 0): #kalo bilangan ganjil no % 2 == 1
        print('bilangan BULAT = ',no)