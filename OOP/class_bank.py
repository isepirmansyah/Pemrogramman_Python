class Bank:
    #member1 variabel
    norek = ''
    nama = ''
    saldo = ''
    jmlNasabah = 0 # variabel stati 
    BANK = 'Bank Syariah Nurul Fikri ' # variabel konstant 

    #member2 konstrukto 
    def __init__(self,no,nasabah,saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlNasabah += 1
        
    #member3 method
    def nabung(self,uang):
    #self.saldo = self.saldo + uang
        self.saldo += uang

    def tarik(self,uang):
    #self.saldo = self.saldo - uang
        self.saldo -= uang

    def cetak(self):
        print(Bank.BANK,
            '\n==========================',
            '\nNo. Rekening\t:',self.norek,
            '\nNama Nasabah\t:',self.nama,
            '\nSaldo\t\t: Rp. ',format(self.saldo, ','),
            '\n--------------------------'
            )

