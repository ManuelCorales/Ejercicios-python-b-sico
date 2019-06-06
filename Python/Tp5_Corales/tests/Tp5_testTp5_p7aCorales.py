# No es necesario testear la función loop_preguntar_nombre debido a que
# no devuleve nada y lo unico que hace es iterar otra función hasta que se dé
# una condición

# Tampoco es necesario testear la función inputs debido a que lo unico de
# lo que se encarga es realizar inputs cada vez que se la llama desde el
# mismo archivo y devuelve ese valor de input. En caso de ser ejecutada
# desde algun archivo externo, devuelve absolutamente lo mismo que se le
# ingresa

# Diccionario: nombres_telefonos = {"carlos": "1165329856",
#                                   "ruben": "1123654875"
#                                   "jorge": "1156236235"}

# Los teléfonos deben ser de 10 cifras
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p7aCorales  # noqa


class TestTp5_p7aCorales(unittest.TestCase):
    def test_si_o_no_editar_telefono(self):
        self.assertEqual(src.Tp5_p7aCorales.si_o_no_editar_telefono("Si"),
                         ("Editar teléfono"))
        self.assertEqual(src.Tp5_p7aCorales.si_o_no_editar_telefono("si"),
                         ("Editar teléfono"))
        self.assertEqual(src.Tp5_p7aCorales.si_o_no_editar_telefono("No"),
                         ("Volver a preguntar nombre"))
        self.assertEqual(src.Tp5_p7aCorales.si_o_no_editar_telefono("no"),
                         ("Volver a preguntar nombre"))

    def test_editar_telefono(self):
        """Testea en qué casos devuelve error si se mete cualquier
        otra cosa que no sea un número y tenga 10 cifras"""
        self.assertEqual(src.Tp5_p7aCorales.editar_telefono
                         ("Carlos", "1156982059"),
                         ("1156982059"))
        self.assertEqual(src.Tp5_p7aCorales.editar_telefono
                         ("Carlos", "asdasd"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7aCorales.editar_telefono
                         ("Carlos", "asd1156982059"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7aCorales.editar_telefono
                         ("Carlos", ""),
                         ("Error"))
        self.assertEqual(src.Tp5_p7aCorales.editar_telefono
                         ("Carlos", "115698205965465135"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7aCorales.editar_telefono
                         ("Maxi", "11059"),
                         ("Error"))

    def test_proceso_nombre(self):
        """Testea cada una de los nombres ingresados comprobando que devuelva
        sus respectivos números de teléfono"""
        self.assertEqual(src.Tp5_p7aCorales.proceso_nombre
                         ("carlos", {"carlos": "1165329856"}),
                         ("1165329856"))
        self.assertEqual(src.Tp5_p7aCorales.proceso_nombre
                         ("jorge", {"jorge": "1156236235"}),
                         ("1156236235"))
        self.assertEqual(src.Tp5_p7aCorales.proceso_nombre
                         ("ruben", {"ruben": "1123654875"}),
                         ("1123654875"))

    def test_preguntar_nombre(self):
        """Llama a la funcion preguntar_nombre con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEqual(src.Tp5_p7aCorales.preguntar_nombre("Carlos"),
                         ("carlos"))
        self.assertEqual(src.Tp5_p7aCorales.preguntar_nombre("Elba Nana"),
                         ("elba nana"))
        self.assertEqual(src.Tp5_p7aCorales.preguntar_nombre("RUBEN "),
                         ("ruben"))
        self.assertEqual(src.Tp5_p7aCorales.preguntar_nombre
                         ("Aaa 123"), ("Error"))
        self.assertEqual(src.Tp5_p7aCorales.preguntar_nombre("   "),
                         ("Error"))
        self.assertEqual(src.Tp5_p7aCorales.preguntar_nombre
                         ("123"), ("Error"))
unittest.main()
