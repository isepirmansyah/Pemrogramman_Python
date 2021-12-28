print('\n--gunakan modul dengan memanggil sebagian fungsinya--')
from modulku import tambah, kurang
tambah(20,30)
kurang(30,20)

print('\n--gunakan modul dengan memanggil seluruh fungsi--')
from modulku import *
tambah(20,30)
kurang(2,3)
kali(5,3)
bagi(20,3)
pangkat(2,3)