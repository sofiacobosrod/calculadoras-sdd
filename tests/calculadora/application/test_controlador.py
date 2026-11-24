import unittest

from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.application.puertos import RepositorioHistorial
from src.calculadora.application.convertir_letras import ConvertirALetrasUseCase
from src.calculadora.domain.numero_a_letras import ConversorNumeroALetras


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

    def test_estado_incluye_letras(self):
        convertir = ConvertirALetrasUseCase(ConversorNumeroALetras())
        controlador = ControladorCalculadora(
            CalcularUseCase(),
            convertir_letras=convertir,
        )
        estado = None
        for tecla in ["1", "5"]:
            estado = controlador.presionar(tecla)

        self.assertIn("letras", estado)
        self.assertEqual(estado["letras"], "quince con 00/100")

    def test_error_deja_letras_vacias(self):
        convertir = ConvertirALetrasUseCase(ConversorNumeroALetras())
        controlador = ControladorCalculadora(
            CalcularUseCase(),
            convertir_letras=convertir,
        )
        estado = None
        for tecla in ["8", "/", "0", "="]:
            estado = controlador.presionar(tecla)

        self.assertEqual(estado["letras"], "")

    def test_igual_una_sola_vez_56_por_9(self):
        estado = self.probar_teclas(["5", "6", "*", "9", "="])
        self.assertEqual(estado["pantalla"], "504")

    def test_igual_una_sola_vez_5_por_5(self):
        estado = self.probar_teclas(["5", "*", "5", "="])
        self.assertEqual(estado["pantalla"], "25")

    def test_negativo_por_positivo(self):
        estado = self.probar_teclas(["5", "±", "*", "3", "="])
        self.assertEqual(estado["pantalla"], "-15")

    def test_positivo_por_negativo(self):
        estado = self.probar_teclas(["3", "*", "5", "±", "="])
        self.assertEqual(estado["pantalla"], "-15")

    def test_resta_con_resultado_negativo(self):
        estado = self.probar_teclas(["2", "-", "5", "="])
        self.assertEqual(estado["pantalla"], "-3")

    def test_cadena_con_resultado_negativo(self):
        estado = self.probar_teclas(["2", "-", "5", "=", "*", "2", "="])
        self.assertEqual(estado["pantalla"], "-6")
