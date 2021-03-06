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
import src.Tp5_p5aCorales  # noqa


class TestTp5_p5aCorales(unittest.TestCase):
    def test_proceso_palabra(self):
        """Testea cada una de las palabras ingresadas comprobando que devuelva
        la primera letra de cada palabra"""
        self.assertEqual(src.Tp5_p5aCorales.proceso_palabra("Heladera Fría"),
                         ("HF"))
        self.assertEqual(src.Tp5_p5aCorales.proceso_palabra("Fede aprobame"),
                         ("FA"))
        self.assertEqual(src.Tp5_p5aCorales.proceso_palabra
                         ("Ciudad Autonoma Buenos Aires"), ("CABA"))

    def test_preguntar_palabra(self):
        """Llama a la funcion preguntar_palabra con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEqual(src.Tp5_p5aCorales.preguntar_palabra("Ojo123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p5aCorales.preguntar_palabra("123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p5aCorales.preguntar_palabra("Aaa 123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p5aCorales.preguntar_palabra
                         ("Aeroplano volador"), ("Aeroplano volador"))


unittest.main()
