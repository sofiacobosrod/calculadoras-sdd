import unittest

from src.calculadora.infrastructure.configuracion_botones import (
    COLORES,
    FILAS_BOTONES,
)


class TestConfiguracionBotones(unittest.TestCase):
    def test_colores_obligatorios(self):
        claves = (
            "fondo",
            "pantalla",
            "borde",
            "numero",
            "operador",
            "limpiar",
            "igual",
            "historial",
            "texto",
            "texto_secundario",
        )
        for clave in claves:
            self.assertIn(clave, COLORES)

    def test_hay_20_botones(self):
        botones = [
            boton
            for fila in FILAS_BOTONES
            for boton in fila
        ]
        self.assertEqual(len(botones), 20)

    def test_todas_las_filas_suman_12_columnas(self):
        for fila in FILAS_BOTONES:
            columnas = sum(boton["columnas"] for boton in fila)
            self.assertEqual(columnas, 12)

    def test_todos_los_tipos_tienen_color(self):
        tipos = {
            boton["tipo"]
            for fila in FILAS_BOTONES
            for boton in fila
        }
        self.assertTrue({"numero", "operador", "limpiar", "igual", "historial"} <= tipos)
