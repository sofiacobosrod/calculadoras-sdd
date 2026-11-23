import unittest

from src.calculadora.domain.calculo import Calculo


class TestCalculo(unittest.TestCase):
    def test_ida_y_vuelta_diccionario(self):
        calculo = Calculo("2 + 3", "5", "23/11/2026 09:30")
        datos = calculo.a_diccionario()
        copia = Calculo.desde_diccionario(datos)

        self.assertEqual(copia.expresion, "2 + 3")
        self.assertEqual(copia.resultado, "5")
        self.assertEqual(copia.fecha, "23/11/2026 09:30")
