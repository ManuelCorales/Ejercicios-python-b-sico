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
import src.Tp5_p2Corales  # noqa


class TestTp5_p2Corales(unittest.TestCase):
    def test_proceso_palabra(self):
        """LLama a la funcion proceso_palabra con alguna palabra y devuelve
        si tiene más letra 'E' o 'A'"""
        self.assertEqual(src.Tp5_p2Corales.proceso_palabra("Aeroplano"),
                         ("Hay más letras A"))
        self.assertEqual(src.Tp5_p2Corales.proceso_palabra("Ojo"),
                         ("No contiene ninguna de las dos letras"))
        self.assertEqual(src.Tp5_p2Corales.proceso_palabra("Alado"),
                         ("Hay más letras A"))
        self.assertEqual(src.Tp5_p2Corales.proceso_palabra("Ejecución"),
                         ("Hay más letras E"))
        self.assertEqual(src.Tp5_p2Corales.proceso_palabra("Alfajor"),
                         ("Hay más letras A"))

    def test_preguntar_palabra(self):
        """Llama a la funcion preguntar_palabra con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEqual(src.Tp5_p2Corales.preguntar_palabra("Ojo123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p2Corales.preguntar_palabra("123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p2Corales.preguntar_palabra(""),
                         ("Error"))
        self.assertEqual(src.Tp5_p2Corales.preguntar_palabra("Aeroplano"),
                         ("Aeroplano"))
unittest.main()
