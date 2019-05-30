import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p2Corales  # noqa


class TestTp5_p2Corales(unittest.TestCase):
    def test_proceso_palabra(self):
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Aeroplano"),
                         ("Hay más letras A"))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Ojo"),
                         ("No contiene ninguna de las dos letras"))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Alado"),
                         ("Hay más letras A"))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Ejecución"),
                         ("Hay más letras E"))
        self.assertEqual(Tp5_p2Corales.proceso_palabra("Alfajor"),
                         ("Hay más letras A"))

    def test_preguntar_palabra(self):
        self.assertEqual(Tp5_p2Corales.preguntar_palabra("Aeroplano"),
                         ("Aeroplano"))
        self.assertEqual(Tp5_p2Corales.preguntar_palabra("Ojo123"),
                         ("Error"))
        self.assertEqual(Tp5_p2Corales.preguntar_palabra("123"),
                         ("Error"))
        self.assertEqual(Tp5_p2Corales.preguntar_palabra(""),
                         ("Error"))

unittest.main()
