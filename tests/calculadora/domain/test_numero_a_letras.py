import unittest

from src.calculadora.domain.numero_a_letras import ConversorNumeroALetras


class TestConversorNumeroALetras(unittest.TestCase):
    def setUp(self):
        self.conversor = ConversorNumeroALetras()

    def test_cero(self):
        self.assertEqual(self.conversor.convertir(0), "cero con 00/100")

    def test_quince(self):
        self.assertEqual(self.conversor.convertir(15), "quince con 00/100")

    def test_veintiuno(self):
        self.assertEqual(self.conversor.convertir(21), "veintiuno con 00/100")

    def test_cien(self):
        self.assertEqual(self.conversor.convertir(100), "cien con 00/100")

    def test_ciento_uno(self):
        self.assertEqual(self.conversor.convertir(101), "ciento uno con 00/100")

    def test_trescientos_ochenta_y_cinco(self):
        self.assertEqual(
            self.conversor.convertir(385),
            "trescientos ochenta y cinco con 00/100",
        )

    def test_mil(self):
        self.assertEqual(self.conversor.convertir(1000), "mil con 00/100")

    def test_dos_mil_veinticinco(self):
        self.assertEqual(
            self.conversor.convertir(2025),
            "dos mil veinticinco con 00/100",
        )

    def test_un_millon(self):
        self.assertEqual(
            self.conversor.convertir(1000000),
            "un millón con 00/100",
        )

    def test_dos_millones_quinientos_mil(self):
        self.assertEqual(
            self.conversor.convertir(2500000),
            "dos millones quinientos mil con 00/100",
        )

    def test_decimales(self):
        self.assertEqual(
            self.conversor.convertir(12.5),
            "doce con 50/100",
        )

    def test_negativo(self):
        self.assertEqual(
            self.conversor.convertir(-7),
            "menos siete con 00/100",
        )

    def test_fuera_de_rango_superior(self):
        self.assertEqual(
            self.conversor.convertir(1000000000),
            "Número fuera de rango",
        )

    def test_fuera_de_rango_inferior(self):
        self.assertEqual(
            self.conversor.convertir(-1000000000),
            "Número fuera de rango",
        )
