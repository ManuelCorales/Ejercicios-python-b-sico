# No es necesario testear la función loop_preguntar_palabra debido a que
# no devuleve nada y lo unico que hace es iterar otra función hasta que se dé
# una condición

# Tampoco es necesario testear la función inputs debido a que lo unico de
# lo que se encarga es realizar inputs cada vez que se la llama desde el
# mismo archivo y devuelve ese valor de input. En caso de ser ejecutada
# desde algun archivo externo, devuelve absolutamente lo mismo que se le
# ingresa
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p1Corales  # noqa
# La contraseña correcta es "123"


class TestTp5_p1aCorales(unittest.TestCase):
    def test_preguntar_contasena(self):
        """Prueba cada una de las contraseñas que hay ahi"""
        self.assertEqual(src.Tp5_p1Corales.preguntar_contrasena("Pepe"),
                         False)
        self.assertEqual(src.Tp5_p1Corales.preguntar_contrasena("123123"),
                         False)
        self.assertEqual(src.Tp5_p1Corales.preguntar_contrasena("Pepe123421"),
                         False)
        self.assertEqual(src.Tp5_p1Corales.preguntar_contrasena(""),
                         False)
        self.assertEqual(src.Tp5_p1Corales.preguntar_contrasena("123"),
                         True)

unittest.main()
