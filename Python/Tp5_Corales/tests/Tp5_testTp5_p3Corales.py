import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p3Corales  # noqa


class TestTp5_p2Corales(unittest.TestCase):
    def test_proceso_palabra(self):
        """LLama a la función proceso_palabra con alguna palabra y devuelve
        cuantas vocales tiene la cadena"""
        self.assertEquals(src.Tp5_p3Corales.proceso_palabra("Aeroplano"), "5")
        self.assertEquals(src.Tp5_p3Corales.proceso_palabra("AEIOU"), "5")
        self.assertEquals(src.Tp5_p3Corales.proceso_palabra("aeiou"), "5")
        self.assertEquals(src.Tp5_p3Corales.proceso_palabra("XDXD"), "0")

    def test_preguntar_palabra(self):
        """Llama a la funcion preguntar_palabra con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEquals(src.Tp5_p3Corales.preguntar_palabra(""), "Error")
        self.assertEquals(src.Tp5_p3Corales.preguntar_palabra("123"), "Error")

unittest.main()
