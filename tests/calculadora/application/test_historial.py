import unittest

from src.calculadora.application.historial import HistorialUseCase
from src.calculadora.application.puertos import RepositorioHistorial
from src.calculadora.domain.calculo import Calculo


class RepositorioEnMemoria(RepositorioHistorial):
    def __init__(self):
        self.calculos = []

    def guardar(self, calculo):
        self.calculos.append(calculo)

    def obtener_todos(self):
        return list(self.calculos)


class TestHistorialUseCase(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioEnMemoria()
        self.historial = HistorialUseCase(self.repositorio)

    def test_registrar_guarda_calculo(self):
        self.historial.registrar("2 + 3", "5")
        calculos = self.repositorio.obtener_todos()
        self.assertEqual(len(calculos), 1)
        self.assertEqual(calculos[0].expresion, "2 + 3")
        self.assertEqual(calculos[0].resultado, "5")

    def test_ultimos_devuelve_mas_recientes_primero(self):
        for numero in range(12):
            self.repositorio.guardar(
                Calculo(str(numero), str(numero), "fecha")
            )

        ultimos = self.historial.ultimos()
        self.assertEqual(len(ultimos), 10)
        self.assertEqual(ultimos[0].expresion, "11")
        self.assertEqual(ultimos[-1].expresion, "2")
