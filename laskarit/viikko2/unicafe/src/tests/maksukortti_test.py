import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kortille_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")

    def test_rahan_ottaminen_kortilta_toimii(self):
        self.maksukortti.lataa_rahaa(1000)
        self.maksukortti.ota_rahaa(44)
        self.assertEqual(str(self.maksukortti), "saldo: 9.66")
        self.maksukortti.ota_rahaa(7500)
        self.assertEqual(str(self.maksukortti), "saldo: 9.66")