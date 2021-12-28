import math

def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print('Hasil Tambah Dari',bil1,'+',bil2,'=',hasil )
    
def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print('Hasil Kurang Dari',bil1,'-',bil2,'=',hasil )
    
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print('Hasil Kali Dari',bil1,'x',bil2,'=',hasil )
    
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print('Hasil Bagi Dari',bil1,':',bil2,'=',hasil )
    
def pangkat(bil1, bil2):
    hasil = math.pow(bil2, bil2)
    print('Hasil Pemangkatan Dari',bil1,'^',bil2,'=',hasil )