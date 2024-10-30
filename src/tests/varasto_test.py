import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_luo_tyhjan_varaston_jos_yrittaa_negatiivista_tilavuutta(self):
        negatiivinen_varasto = Varasto(-10)
        self.assertAlmostEqual(negatiivinen_varasto.saldo, 0)
    
    def test_konstruktori_laittaa_saldoksi_0_jos_meinaa_menna_negatiiviseksi(self):
        negatiivinen_saldo = Varasto(10, -10)
        self.assertAlmostEqual(negatiivinen_saldo.saldo, 0)

    def test_konstruktori_jos_saldoa_enemman_kuin_tilaa(self):
        liikaa_saldoa = Varasto(10, 100)
        self.assertAlmostEqual(liikaa_saldoa.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
    
    def test_lisays_lisaa_negatiivinen_saldo(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_lisays_lisaa_liikaa_loput_hukkaan(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_negatiivisen_ottaminen(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_liikaa_ottaminen(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_tulostaminen(self):
        self.varasto.lisaa_varastoon(69)
        self.assertAlmostEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")