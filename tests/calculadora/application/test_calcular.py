import unittest

from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.domain.errores import DivisionPorCeroError


class TestCalcularUseCase(unittest.TestCase):
    def setUp(self):
        self.calcular = CalcularUseCase()

    def test_operaciones_minimas(self):
        self.assertEqual(self.calcular.ejecutar(2, "+", 3), 5)
        self.assertEqual(self.calcular.ejecutar(5, "-", 3), 2)
        self.assertEqual(self.calcular.ejecutar(4, "*", 2), 8)
        self.assertEqual(self.calcular.ejecutar(8, "/", 2), 4)

    def test_division_por_cero(self):
        with self.assertRaises(DivisionPorCeroError):
            self.calcular.ejecutar(8, "/", 0)

    def test_operador_desconocido(self):
        with self.assertRaises(ValueError):
            self.calcular.ejecutar(2, "^", 3)
