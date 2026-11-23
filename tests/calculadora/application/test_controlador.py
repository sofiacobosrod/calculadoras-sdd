import unittest

from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.application.puertos import RepositorioHistorial


class HistorialPrueba(RepositorioHistorial):
    def __init__(self):
        self.registros = []

    def guardar(self, calculo):
        self.registros.append(calculo)

    def obtener_todos(self):
        return list(self.registros)


class HistorialUseCasePrueba:
    def __init__(self):
        self.registros = []

    def registrar(self, expresion, resultado):
        self.registros.append((expresion, resultado))


class TestControladorCalculadora(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorCalculadora(CalcularUseCase())
        self.historial = HistorialUseCasePrueba()

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

    def test_igual_valido_registra_historial(self):
        historial = HistorialUseCasePrueba()
        controlador = ControladorCalculadora(CalcularUseCase(), historial)
        for tecla in ["2", "+", "3", "="]:
            controlador.presionar(tecla)

        self.assertEqual(historial.registros, [("2 + 3", "5")])

    def test_error_no_registra_historial(self):
        historial = HistorialUseCasePrueba()
        controlador = ControladorCalculadora(CalcularUseCase(), historial)
        for tecla in ["8", "/", "0", "="]:
            controlador.presionar(tecla)

        self.assertEqual(historial.registros, [])
