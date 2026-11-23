from src.calculadora.domain.operaciones import (
    Division,
    Multiplicacion,
    Resta,
    Suma,
)


class CalcularUseCase:
    def __init__(self):
        self.operaciones = {
            "+": Suma(),
            "-": Resta(),
            "*": Multiplicacion(),
            "/": Division(),
        }

    def ejecutar(self, a, operador, b):
        operacion = self.operaciones.get(operador)
        if operacion is None:
            raise ValueError("Operador no valido")
        return operacion.calcular(a, b)
