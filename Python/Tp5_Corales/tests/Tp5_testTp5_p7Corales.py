# No es necesario testear la función loop_preguntar_palabra debido a que
# no devuleve nada y lo unico que hace es iterar otra función hasta que se dé
# una condición

# Tampoco es necesario testear la función inputs debido a que lo unico de
# lo que se encarga es realizar inputs cada vez que se la llama desde el
# mismo archivo y devuelve ese valor de input. En caso de ser ejecutada
# desde algun archivo externo, devuelve absolutamente lo mismo que se le
# ingresa

# Diccionario: nombres_telefonos = {"carlos": "+11 6532-9856",
#                                   "ruben": "+11 2365-4875"
#                                   "jorge": "+11 5623-62365"}
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.Tp5_p7Corales  # noqa


class TestTp5_p7Corales(unittest.TestCase):
    def test_proceso_nombre(self):
        """Testea cada una de las palabras ingresadas comprobando que devuelva
        las vocales con su siguiente"""
        self.assertEqual(src.Tp5_p7Corales.proceso_nombre("Carlos"),
                         ("+11 6532-9856"))
        self.assertEqual(src.Tp5_p7Corales.proceso_nombre("Ruben"),
                         ("+11 2365-4875"))
        self.assertEqual(src.Tp5_p7Corales.proceso_nombre
                         ("Jorge"), ("+11 5623-62365"))
        self.assertEqual(src.Tp5_p7Corales.proceso_nombre
                         ("Pepito"), ("Agregar telefono"))
        self.assertEqual(src.Tp5_p7Corales.proceso_nombre
                         ("*"), ("Salir"))

    def test_agregar_telefono(self):
        """Evalúa si se agrega el telefono del nombre que no lo poseía
        correctamente"""
        self.assertEqual(src.Tp5_p7Corales.agregar_telefono
                         ("Pepito"), (""))

    def test_preguntar_palabra(self):
        """Llama a la funcion preguntar_palabra con cada palabra y devuelve
        si pasa los filtros de la cadena ingresada"""
        self.assertEqual(src.Tp5_p7Corales.preguntar_palabra("Carlos"),
                         ("Carlos"))
        self.assertEqual(src.Tp5_p7Corales.preguntar_palabra("Este ban"),
                         ("Error"))
        self.assertEqual(src.Tp5_p7Corales.preguntar_palabra("RUBEN "),
                         ("RUBEN"))
        self.assertEqual(src.Tp5_p7Corales.preguntar_palabra
                         ("Aaa 123"), ("Error"))
        self.assertEqual(src.Tp5_p7Corales.preguntar_palabra("   "),
                         ("Error"))
        self.assertEqual(src.Tp5_p7Corales.preguntar_palabra
                         ("123"), ("Error"))
unittest.main()
