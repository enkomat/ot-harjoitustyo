import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_luodussa_kassapaattessa_on_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodussa_kassapaatteessa_on_oikeat_lounasmaarat(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.kassapaate.syo_edullisesti_kateisella(480)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)
        self.kassapaate.syo_edullisesti_kateisella(24)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)
    
    def test_kateisosto_toimii_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.kassapaate.syo_maukkaasti_kateisella(800)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100800)
        self.kassapaate.syo_maukkaasti_kateisella(40)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100800)
    
    def test_korttiosto_toimii_edulliset(self):
        testikortti_albert = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(testikortti_albert), True)
        self.assertEqual(str(testikortti_albert), "saldo: 7.6")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        testikortti_berta = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(testikortti_berta), False)
        self.assertEqual(str(testikortti_berta), "saldo: 0.1")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttiosto_toimii_maukkaat(self):
        testikortti_albert = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(testikortti_albert), True);
        self.assertEqual(str(testikortti_albert), "saldo: 6.0")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        testikortti_berta = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(testikortti_berta), False);
        self.assertEqual(str(testikortti_berta), "saldo: 0.1")
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    
    def test_saldo_kasvaa_kortille_rahaa_lisattaessa(self):
        testikortti_albert = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(testikortti_albert, 450)
        self.assertEqual(str(testikortti_albert), "saldo: 14.5")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100450)
        self.kassapaate.lataa_rahaa_kortille(testikortti_albert, -450)
        self.assertEqual(str(testikortti_albert), "saldo: 14.5")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100450)