import Tp3_p7Corales
import unittest


class Test_Tp3_p7Corales (unittest.TestCase):
    def test_que_dia_es(self):
        self.assertEqual(Tp3_p7Corales.que_dia_es("a"), False)
        self.assertEqual(Tp3_p7Corales.que_dia_es(3.5), False)
        self.assertEqual(Tp3_p7Corales.que_dia_es(""), False)

    def test_que_dia_es_2(self):
        self.assertEqual(Tp3_p7Corales.que_dia_es(1), "Lunes")
        self.assertEqual(Tp3_p7Corales.que_dia_es(2), "Martes")
        self.assertEqual(Tp3_p7Corales.que_dia_es(3), "Miércoles")
        self.assertEqual(Tp3_p7Corales.que_dia_es(4), "Jueves")
        self.assertEqual(Tp3_p7Corales.que_dia_es(5), "Viernes")
        self.assertEqual(Tp3_p7Corales.que_dia_es(6), "Sábado")
        self.assertEqual(Tp3_p7Corales.que_dia_es(7), "Domingo")

if __name__ == "__main__":
    unittest.main()
