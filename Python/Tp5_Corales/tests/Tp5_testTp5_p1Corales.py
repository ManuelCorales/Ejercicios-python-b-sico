import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p1Corales  # noqa
# La contraseña correcta es "123"


class TestTp5_p1aCorales(unittest.TestCase):
    def test_preguntar_contasena(self):
        """Prueba cada una de las contraseñas que hay ahi"""
        self.assertEqual(Tp5_p1Corales.preguntar_contrasena("Pepe"),
                         False)
        self.assertEqual(Tp5_p1Corales.preguntar_contrasena("123123"),
                         False)
        self.assertEqual(Tp5_p1Corales.preguntar_contrasena("Pepe123421"),
                         False)
        self.assertEqual(Tp5_p1Corales.preguntar_contrasena(""),
                         False)
        self.assertEqual(Tp5_p1Corales.preguntar_contrasena("123"),
                         True)

unittest.main()
