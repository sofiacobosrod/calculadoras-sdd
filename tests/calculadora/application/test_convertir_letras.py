import unittest

from src.calculadora.application.convertir_letras import ConvertirALetrasUseCase
from src.calculadora.domain.numero_a_letras import ConversorNumeroALetras


class TestConvertirALetrasUseCase(unittest.TestCase):
    def setUp(self):
        conversor = ConversorNumeroALetras()
        self.caso_uso = ConvertirALetrasUseCase(conversor)

    def test_ejecutar(self):
        self.assertEqual(
            self.caso_uso.ejecutar(385),
            "trescientos ochenta y cinco con 00/100",
        )
