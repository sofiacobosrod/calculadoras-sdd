import unittest

from src.calculadora.domain.errores import DivisionPorCeroError
from src.calculadora.domain.operaciones import (
    Division,
    Multiplicacion,
    Operacion,
    Resta,
    Suma,
)


class TestOperaciones(unittest.TestCase):
    def test_clases_realizan_operaciones(self):
        self.assertEqual(Suma().calcular(2, 3), 5)
        self.assertEqual(Resta().calcular(5, 3), 2)
        self.assertEqual(Multiplicacion().calcular(4, 2), 8)
        self.assertEqual(Division().calcular(8, 2), 4)

    def test_operacion_es_abstracta(self):
        self.assertTrue(hasattr(Operacion, "__abstractmethods__"))
        self.assertTrue(Operacion.__abstractmethods__)

    def test_division_por_cero_lanza_error_controlado(self):
        with self.assertRaises(DivisionPorCeroError):
            Division().calcular(8, 0)
