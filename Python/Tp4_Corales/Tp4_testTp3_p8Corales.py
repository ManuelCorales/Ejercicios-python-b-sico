import unittest
import Tp3_p8Corales


class TestTp3_p8Corales(unittest.TestCase):
    def test_transformador_dec_a_rom(self):
        """Testea si los valores introducidos son validos"""
        self.assertEqual(Tp3_p8Corales.transformador_dec_a_rom(77), "LXXVII")
        self.assertEqual(Tp3_p8Corales.transformador_dec_a_rom("A"), "Error")
        self.assertEqual(Tp3_p8Corales.transformador_dec_a_rom(555666),
                         "dlvDCLXVI")
unittest.main()
