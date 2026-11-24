import json
import os
import tempfile
import unittest

from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.application.historial import HistorialUseCase
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

    def test_guarda_varios_calculos_sin_error(self):
        carpeta = tempfile.mkdtemp()
        ruta = os.path.join(carpeta, "historial.json")
        repositorio = RepositorioHistorialJson(ruta)

        repositorio.guardar(Calculo("2 + 3", "5", "23/11/2026 09:30"))
        repositorio.guardar(Calculo("4 × 2", "8", "23/11/2026 09:31"))

        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self.assertEqual(len(datos), 2)
        self.assertEqual(datos[0]["expresion"], "2 + 3")
        self.assertEqual(datos[1]["expresion"], "4 × 2")

    def test_integracion_controlador_historial_json(self):
        carpeta = tempfile.mkdtemp()
        ruta = os.path.join(carpeta, "historial.json")
        repositorio = RepositorioHistorialJson(ruta)
        historial = HistorialUseCase(repositorio)
        controlador = ControladorCalculadora(CalcularUseCase(), historial)

        for tecla in ["2", "+", "3", "="]:
            controlador.presionar(tecla)

        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self.assertEqual(len(datos), 1)
        self.assertEqual(datos[0]["expresion"], "2 + 3")
        self.assertEqual(datos[0]["resultado"], "5")

    def test_integracion_igual_una_vez_guarda_un_registro(self):
        carpeta = tempfile.mkdtemp()
        ruta = os.path.join(carpeta, "historial.json")
        repositorio = RepositorioHistorialJson(ruta)
        historial = HistorialUseCase(repositorio)
        controlador = ControladorCalculadora(CalcularUseCase(), historial)

        for tecla in ["5", "*", "5", "="]:
            controlador.presionar(tecla)

        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self.assertEqual(len(datos), 1)
