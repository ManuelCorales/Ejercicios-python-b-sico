import unittest
import Tp5_p2Corales


class TestTp5_p2Corales(unittest.TestCase):
    def test_proceso_palabra(self):
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Aeroplano"), (2, 1))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Ojo"), (0, 0))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Alado"), (2, 0))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Ejecución"), (0, 2))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Alfajor"), (2, 0))

    def test_preguntar_palabra(self):
        self.assertEqual(Tp5_p2Corales.preguntar_palabra("Aeroplano"),
                         "Aeroplano")
        self.assertEqual(Tp5_p2Corales.preguntar_palabra("Ojo123"), ("Error"))
        self.assertEqual(Tp5_p2Corales.preguntar_palabra("123"), ("Error"))
        self.assertEqual(Tp5_p2Corales.preguntar_palabra(""), ("Error"))
