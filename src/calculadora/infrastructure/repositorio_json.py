import json

from src.calculadora.application.puertos import RepositorioHistorial
from src.calculadora.domain.calculo import Calculo


class RepositorioHistorialJson(RepositorioHistorial):
    def __init__(self, ruta="historial.json"):
        self.ruta = ruta

    def guardar(self, calculo):
        calculos = self.obtener_todos()
        calculos.append(calculo.a_diccionario())
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            json.dump(calculos, archivo, ensure_ascii=False)

    def obtener_todos(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return []

        if not isinstance(datos, list):
            return []

        calculos = []
        for dato in datos:
            try:
                calculos.append(Calculo.desde_diccionario(dato))
            except (KeyError, TypeError):
                continue
        return calculos
