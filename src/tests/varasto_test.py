import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_epapositiivisella_tilavuudella(self):
        tmp = Varasto(-1)
        self.assertAlmostEqual(tmp.tilavuus, 0.0)

    def test_konstruktori_negatiivisella_alkusaldolla(self):
        tmp = Varasto(10, -1)
        self.assertAlmostEqual(tmp.saldo, 0.0)

    def test_konstruktori_asettulla_alkusaldolla(self):
        tmp = Varasto(10, 1)
        self.assertAlmostEqual(tmp.saldo, 1)

    def test_konstruktori_liian_suurella_alkusaldolla(self):
        tmp = Varasto(10, 12)
        self.assertAlmostEqual(tmp.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_negatiivinen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0);
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_liian_paljon_tayttaa(self):
        self.varasto.lisaa_varastoon(1000)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_negatiivinen_palauttaa_oikean(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_ottaminen_negatiivinen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_liikaa_palauttaa_loput(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.ota_varastosta(100), 8)

    def test_ottaminen_liikaa_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(100)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str(self):
        varasto_str = self.varasto.__str__()
        self.assertEqual(varasto_str, "saldo = 0, vielä tilaa 10")
