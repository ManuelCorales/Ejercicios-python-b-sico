# No es necesario testear la función loop_preguntar_nombre debido a que
# no devuleve nada y lo unico que hace es iterar otra función hasta que se dé
# una condición

# Tampoco es necesario testear la función inputs debido a que lo único de
# lo que se encarga es realizar inputs cada vez que se la llama desde el
# mismo archivo y devuelve ese valor de input. En caso de ser ejecutada
# desde algun archivo externo, devuelve absolutamente lo mismo que se le
# ingresa

# Diccionario: nombres_telefonos = {"carlos": "1165329856",
#                                   "ruben": "1123654875"
#                                   "jorge": "1156236235"}

# Los teléfonos tienen que ser de 10 números
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p7bCorales  # noqa


class TestTp5_p7bCorales(unittest.TestCase):
    def test_si_o_no_editar_telefono(self):
        """Testea si segun ingresa 'si' o 'no' si decide o no editar
        teléfono"""
        self.assertEqual(src.Tp5_p7bCorales.si_o_no_editar_telefono("Si"),
                         ("Editar teléfono"))
        self.assertEqual(src.Tp5_p7bCorales.si_o_no_editar_telefono("si"),
                         ("Editar teléfono"))
        self.assertEqual(src.Tp5_p7bCorales.si_o_no_editar_telefono("No"),
                         ("Volver a preguntar nombre"))
        self.assertEqual(src.Tp5_p7bCorales.si_o_no_editar_telefono("no"),
                         ("Volver a preguntar nombre"))

    def test_crear_o_no_telefono(self):
        """Testea si segun ingresa 'si' o 'no' si decide o no crear
        teléfono"""
        self.assertEqual(src.Tp5_p7bCorales.crear_o_no_telefono("Si"),
                         ("Crear teléfono"))
        self.assertEqual(src.Tp5_p7bCorales.crear_o_no_telefono("si"),
                         ("Crear teléfono"))
        self.assertEqual(src.Tp5_p7bCorales.crear_o_no_telefono("No"),
                         ("No crear"))
        self.assertEqual(src.Tp5_p7bCorales.crear_o_no_telefono("no"),
                         ("No crear"))

    def test_editar_telefono(self):
        """Testea en qué casos devuelve error si se mete cualquier
        otra cosa que no sea un número y tenga 10 cifras"""
        self.assertEqual(src.Tp5_p7bCorales.editar_telefono
                         ("Carlos", "1156982059"),
                         ("1156982059"))
        self.assertEqual(src.Tp5_p7bCorales.editar_telefono
                         ("Carlos", "asdasd"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.editar_telefono
                         ("Carlos", "asd1156982059"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.editar_telefono
                         ("Carlos", ""),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.editar_telefono
                         ("Carlos", "115698205965465135"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.editar_telefono
                         ("Maxi", "11059"),
                         ("Error"))

    def test_crear_telefono(self):
        """Testea en qué casos devuelve error si se mete cualquier
        otra cosa que no sea un número y tenga 10 cifras"""
        self.assertEqual(src.Tp5_p7bCorales.crear_telefono
                         ("Juan Jesús de la Rosa", "1156652059"),
                         ("1156652059"))
        self.assertEqual(src.Tp5_p7bCorales.crear_telefono
                         ("Elba nana", "asdasd"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.crear_telefono
                         ("", "asd1156982059"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.crear_telefono
                         ("Estebean Rogelio", ""),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.crear_telefono
                         ("Carlos", "115698205965465135"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.crear_telefono
                         ("Maxi", "11059"),
                         ("Error"))

    def test_proceso_nombre(self):
        """Testea cada una de los nombres ingresados comprobando que devuelva
        sus respectivos números de teléfono"""
        self.assertEqual(src.Tp5_p7bCorales.proceso_nombre
                         ("carlos", {"carlos": "1165329856"}),
                         ("1165329856"))
        self.assertEqual(src.Tp5_p7bCorales.proceso_nombre
                         ("jorge", {"jorge": "1156236235"}),
                         ("1156236235"))
        self.assertEqual(src.Tp5_p7bCorales.proceso_nombre
                         ("ruben", {"ruben": "1123654875"}),
                         ("1123654875"))

    def test_preguntar_nombre(self):
        """Llama a la funcion preguntar_nombre con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEqual(src.Tp5_p7bCorales.preguntar_nombre("Carlos"),
                         ("carlos"))
        self.assertEqual(src.Tp5_p7bCorales.preguntar_nombre("Elba Nana"),
                         ("elba nana"))
        self.assertEqual(src.Tp5_p7bCorales.preguntar_nombre("RUBEN "),
                         ("ruben"))
        self.assertEqual(src.Tp5_p7bCorales.preguntar_nombre
                         ("Aaa 123"), ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.preguntar_nombre("   "),
                         ("Error"))
        self.assertEqual(src.Tp5_p7bCorales.preguntar_nombre
                         ("123"), ("Error"))
unittest.main()
