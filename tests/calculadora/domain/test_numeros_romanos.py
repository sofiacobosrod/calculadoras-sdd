import unittest

from src.calculadora.domain.numeros_romanos import ConversorNumeroRomano


class TestConversorNumeroRomano(unittest.TestCase):
    # setUp se ejecuta antes de cada prueba y crea un conversor nuevo.
    def setUp(self):
        self.conversor = ConversorNumeroRomano()

    def test_uno(self):
        self.assertEqual(self.conversor.convertir("1"), "I")

    def test_cuatro_resta_especial(self):
        self.assertEqual(self.conversor.convertir("4"), "IV")

    def test_nueve_resta_especial(self):
        self.assertEqual(self.conversor.convertir("9"), "IX")

    def test_catorce(self):
        self.assertEqual(self.conversor.convertir("14"), "XIV")

    def test_cuarenta(self):
        self.assertEqual(self.conversor.convertir("40"), "XL")

    def test_trescientos_ochenta_y_cinco(self):
        self.assertEqual(self.conversor.convertir("385"), "CCCLXXXV")

    def test_dos_mil_veinticinco(self):
        self.assertEqual(self.conversor.convertir("2025"), "MMXXV")

    def test_maximo_3999(self):
        self.assertEqual(self.conversor.convertir("3999"), "MMMCMXCIX")

    def test_cero_no_tiene_romano(self):
        self.assertEqual(self.conversor.convertir("0"), "Sin romano")

    def test_negativo_no_tiene_romano(self):
        self.assertEqual(self.conversor.convertir("-5"), "Sin romano")

    def test_decimal_no_tiene_romano(self):
        self.assertEqual(self.conversor.convertir("12.5"), "Sin romano")

    def test_mayor_a_3999_no_tiene_romano(self):
        self.assertEqual(self.conversor.convertir("4000"), "Sin romano")

    def test_texto_no_tiene_romano(self):
        self.assertEqual(self.conversor.convertir("Error"), "Sin romano")