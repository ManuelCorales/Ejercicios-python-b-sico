import unittest
import Tp5_p1aCorales


class TestTp5_p1aCorales(unittest.TestCase):
    def test_pregunta_contasena(self):
        self.assertEqual(Tp5_p1aCorales.preguntar_contrasena("Pepe"),
                         "Contraseña incorrecta")
        self.assertEqual(Tp5_p1aCorales.preguntar_contrasena("123123"),
                         "Contraseña incorrecta")
        self.assertEqual(Tp5_p1aCorales.preguntar_contrasena("Pepe123421"),
                         "Contraseña incorrecta")
        self.assertEqual(Tp5_p1aCorales.preguntar_contrasena("123"),
                         "Contraseña correcta")
