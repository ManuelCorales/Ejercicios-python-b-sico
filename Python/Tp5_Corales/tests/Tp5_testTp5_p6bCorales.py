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
import src.Tp5_p6bCorales  # noqa


class TestTp5_p6bCorales(unittest.TestCase):
    def test_proceso_palabra(self):
        """Testea cada una de las palabras ingresadas comprobando que devuelva
        las palabras sin las consonantes"""
        self.assertEqual(src.Tp5_p6bCorales.proceso_palabra("Antes de ayer"),
                         ("Ae e ae"))
        self.assertEqual(src.Tp5_p6bCorales.proceso_palabra("fede aprobame"),
                         ("ee aoae"))
        self.assertEqual(src.Tp5_p6bCorales.proceso_palabra
                         ("Ciudad Autonoma de Buenos Aires"),
                         ("iua Auooa e ueo Aie"))

    def test_preguntar_palabra(self):
        """Llama a la funcion preguntar_palabra con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEqual(src.Tp5_p6bCorales.preguntar_palabra("Ojo123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p6bCorales.preguntar_palabra("123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p6bCorales.preguntar_palabra("Aaa 123"),
                         ("Error"))
        self.assertEqual(src.Tp5_p6bCorales.preguntar_palabra
                         ("aeroplano volador"), ("aeroplano volador"))
        self.assertEqual(src.Tp5_p6bCorales.preguntar_palabra("   "),
                         ("Error"))
        self.assertEqual(src.Tp5_p6bCorales.preguntar_palabra
                         ("aeroplano volador"), ("aeroplano volador"))
unittest.main()
