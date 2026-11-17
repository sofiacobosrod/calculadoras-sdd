import contextlib
import io
import unittest
from unittest.mock import patch

from calculadora import dividir, multiplicar, pedir_numero, restar, sumar
import calculadora


class PruebasCalculadora(unittest.TestCase):
    def test_operaciones_de_aceptacion(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(restar(5, 7), -2)
        self.assertEqual(multiplicar(4, 2.5), 10)
        self.assertEqual(dividir(8, 2), 4)

    def test_dividir_por_cero_lanza_error(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(3, 0)

    def test_pedir_numero_repite_ante_entrada_invalida(self):
        with patch("builtins.input", side_effect=["texto", "2.5"]):
            with contextlib.redirect_stdout(io.StringIO()) as salida:
                numero = pedir_numero("Número: ")

        self.assertEqual(numero, 2.5)
        self.assertIn("Entrada no válida", salida.getvalue())

    def test_menu_muestra_error_de_division_y_vuelve(self):
        entradas = ["4", "3", "0", "5"]
        with patch("builtins.input", side_effect=entradas):
            with contextlib.redirect_stdout(io.StringIO()) as salida:
                calculadora.main()

        self.assertIn("No se puede dividir por cero", salida.getvalue())

    def test_menu_rechaza_opcion_invalida(self):
        with patch("builtins.input", side_effect=["9", "5"]):
            with contextlib.redirect_stdout(io.StringIO()) as salida:
                calculadora.main()

        self.assertIn("Opción no válida", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
