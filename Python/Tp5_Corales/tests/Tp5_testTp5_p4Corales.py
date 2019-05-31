# Las unicas cadenas que se admiten son las que no tienen numeros.

# La primera palabra ingresada siempre debe estar en minusculas en su
# totalidad, así como la segunda debe estar completamente en mayusculas.

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
import src.Tp5_p4Corales  # noqa


class TestTp5_p4Corales(unittest.TestCase):
    def test_proceso_palabra(self):
        """LLama a la función proceso_palabra con alguna palabra y devuelve
        cuantas vocales tiene la cadena"""
        self.assertEquals(src.Tp5_p4Corales.proceso_palabra(["asd", "ASD"]),
                          "Las palabras son iguales")
        self.assertEquals(src.Tp5_p4Corales.proceso_palabra(["xd", "XD"]),
                          "Las palabras son iguales")
        self.assertEquals(src.Tp5_p4Corales.proceso_palabra(["hola", "PEPE"]),
                          "Las palabras son diferentes")
        self.assertEquals(src.Tp5_p4Corales.proceso_palabra(["lol", "DOU"]),
                          "Las palabras son diferentes")

    def test_preguntar_palabra(self):
        """Llama a la funcion preguntar_palabra con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada. En la version 1 se prueba
        ingresando solo la primera palabra sin nada atras"""
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["", ""]),
                          (["Error", ""]))
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["123", ""]),
                          (["Error", ""]))
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd123", ""]),
                          (["Error", ""]))
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["ASD123", ""]),
                          (["Error", ""]))
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["AsD123", ""]),
                          (["Error", ""]))
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", ""]),
                          (["Error", ""]))

    def test_preguntar_palabra_v2(self):
        """En esta versión se pruea ingresando las dos cadenas que pide
        el programa en la gran mayoría de sus posibilidades"""
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", "123"]),
                          ["Error", ""])
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", "asd123"]),
                          ["Error", ""])
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", "ASD123"]),
                          ["Error", ""])
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", "AsD123"]),
                          ["Error", ""])
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", "OSO"]),
                          ["asd", "LIBRO"])
        self.assertEquals(src.Tp5_p4Corales.preguntar_palabra(["asd", "ASD"]),
                          ["asd", "ASD"])

unittest.main()
