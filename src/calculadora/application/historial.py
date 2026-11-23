from datetime import datetime

from src.calculadora.domain.calculo import Calculo


class HistorialUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar(self, expresion, resultado):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        calculo = Calculo(expresion, resultado, fecha)
        self.repositorio.guardar(calculo)

    def ultimos(self, cantidad=10):
        calculos = self.repositorio.obtener_todos()
        return list(reversed(calculos))[:cantidad]
