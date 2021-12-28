from subclass_mahasiswa import *
from subclass_dosen import *
#ciptakan object
m1 = Mahasiswa('Siti Aminah','Wanita',20,'SI',3)
m2 = Mahasiswa('Budi Santoso','Pria',23,'TI',5)
d1 = Dosen('Sirojul Munir','Pria',43,'S.Si, M.Kom','Waket 1')
d2 = Dosen('Henry Saptono','Pria',44,'S.Si, M.Kom','Ketua BTSI')
#gunakan fungsi2 yg ada di class 
d1.setGaji(12000000)
d2.setGaji(10000000)
m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()
