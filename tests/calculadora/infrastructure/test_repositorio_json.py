import os
import tempfile
import unittest

from src.calculadora.domain.calculo import Calculo
from src.calculadora.infrastructure.repositorio_json import RepositorioHistorialJson


class TestRepositorioHistorialJson(unittest.TestCase):
    def test_archivo_inexistente_devuelve_lista_vacia(self):
        carpeta = tempfile.mkdtemp()
        ruta = os.path.join(carpeta, "historial.json")
        repositorio = RepositorioHistorialJson(ruta)

        self.assertEqual(repositorio.obtener_todos(), [])

    def test_archivo_danado_devuelve_lista_vacia(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as archivo:
            archivo.write("{dato danado")
            ruta = archivo.name

        try:
            repositorio = RepositorioHistorialJson(ruta)
            self.assertEqual(repositorio.obtener_todos(), [])
        finally:
            os.unlink(ruta)

    def test_guarda_y_recupera_calculos(self):
        carpeta = tempfile.mkdtemp()
        ruta = os.path.join(carpeta, "historial.json")
        repositorio = RepositorioHistorialJson(ruta)
        calculo = Calculo("2 + 3", "5", "23/11/2026 09:30")

        repositorio.guardar(calculo)
        calculos = repositorio.obtener_todos()

        self.assertEqual(len(calculos), 1)
        self.assertEqual(calculos[0].expresion, "2 + 3")
        self.assertEqual(calculos[0].resultado, "5")
