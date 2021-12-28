class Gempa:
    #member1 variabel
    lokasi = ""
    skala = 0
    #member2 konstruktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    #member3 method
    def dampak(self):
        if( self.skala < 2 ):
            ket ='Tidak terasa'
        elif(self.skala >= 2 and self.skala < 4):
            ket = 'Bangunan retak-retak'
        elif(self.skala >= 4 and self.skala < 6):
            ket = 'Bangunan pada roboh'
        else:
            ket = 'Berpotensi tsunami'
        print('Telah terjadi gempa di',self.lokasi,
            ' dengan skala',self.skala,' richter'
            ' berdampak',ket)

