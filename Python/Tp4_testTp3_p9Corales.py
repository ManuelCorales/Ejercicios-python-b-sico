
import Tp3_p9Corales
import unittest

# ACLARACIÓN DISCLAMER WARNING
#
#
# Las funciones loop_proceso_notas, loop_ingreso_datos, inputs no son
# testeadas debido a que no es necesario, lo unico de lo que se
# encargan es iterar otras funciones y tampoco devuelven nada


class TestTp3_p9Corales(unittest.TestCase):
    def test_proceso_notas(self):
        """Prueba según el numero de ejercicios por examen, el
        porcentaje con el cual se aprueba, la cantidad de
        ejercicios que hizo bien el alumno y otra variable
        irrelevante para el test, si aprobó o no o si ingresó
        el caracter '*' """
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 30, 4, 1),
                         "Aprobó")
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 30, 3, 1),
                         "Aprobó")
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 50, 4, 1),
                         "Desaprobó")
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 50, 4.5, 1),
                         "Desaprobó")
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 30, "*", 1),
                         "*")
        # Test del valor centinela '*'
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 30, 11, 1),
                         "Error")
        # Acá señaló que hizo correctamente más ejercicios de los que
        # habia en el examen
        self.assertEqual(Tp3_p9Corales.proceso_notas(10, 30, -1, 1),
                         "Error")

    def test_ingreso_dato_cant_ejer(self):
        self.assertEqual(Tp3_p9Corales.ingreso_dato_cant_ejer("a"),
                         "Error cant_ejer")
        self.assertEqual(Tp3_p9Corales.ingreso_dato_cant_ejer(3), 3)

    def test_ingreso_dato_cant_nece(self):
        self.assertEqual(Tp3_p9Corales.ingreso_dato_cant_nece("a", "xd"),
                         "Error cant_nece")
        self.assertEqual(Tp3_p9Corales.ingreso_dato_cant_nece(10, 20), 20)
        self.assertNotEqual(Tp3_p9Corales.ingreso_dato_cant_nece(10, 20), 30)
unittest.main()
