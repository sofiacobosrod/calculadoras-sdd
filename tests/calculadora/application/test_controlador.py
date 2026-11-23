import unittest

from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora


class TestControladorCalculadora(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorCalculadora(CalcularUseCase())

    def probar_teclas(self, teclas):
        estado = None
        for tecla in teclas:
            estado = self.controlador.presionar(tecla)
        return estado

    def test_suma_basica(self):
        estado = self.probar_teclas(["2", "+", "3", "="])
        self.assertEqual(estado["pantalla"], "5")

    def test_operaciones_encadenadas(self):
        estado = self.probar_teclas(
            ["1", "2", "5", "*", "3", "+", "1", "0", "="]
        )
        self.assertEqual(estado["expresion"], "125 × 3 + 10")
        self.assertEqual(estado["pantalla"], "385")

    def test_division_por_cero(self):
        estado = self.probar_teclas(["8", "/", "0", "="])
        self.assertEqual(estado["pantalla"], "Error")
        self.assertEqual(
            estado["expresion"], "No se puede dividir por cero"
        )

    def test_siguiente_numero_despues_del_error(self):
        self.probar_teclas(["8", "/", "0", "="])
        estado = self.controlador.presionar("5")
        self.assertEqual(estado["pantalla"], "5")
        self.assertEqual(estado["expresion"], "")

    def test_cambiar_signo(self):
        estado = self.probar_teclas(["5", "±"])
        self.assertEqual(estado["pantalla"], "-5")

    def test_porcentaje(self):
        estado = self.probar_teclas(["5", "0", "%"])
        self.assertEqual(estado["pantalla"], "0.5")

    def test_decimal_y_numero_entero(self):
        estado = self.probar_teclas(["4", "*", "2", ".", "5", "="])
        self.assertEqual(estado["pantalla"], "10")

    def test_limpieza(self):
        estado = self.probar_teclas(["1", "2", "C"])
        self.assertEqual(estado["pantalla"], "0")
        self.assertEqual(estado["expresion"], "")

    def test_no_permite_dos_decimales(self):
        estado = self.probar_teclas(["4", ".", ".", "5"])
        self.assertEqual(estado["pantalla"], "4.5")
