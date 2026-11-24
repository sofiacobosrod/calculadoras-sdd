from abc import ABC, abstractmethod

from src.calculadora.domain.errores import DivisionPorCeroError


class Operacion(ABC):
    def __init__(self, simbolo):
        self.simbolo = simbolo

    @abstractmethod
    def calcular(self, a, b):
        pass


class Suma(Operacion):
    def __init__(self):
        super().__init__("+")

    def calcular(self, a, b):
        return a + b


class Resta(Operacion):
    def __init__(self):
        super().__init__("-")

    def calcular(self, a, b):
        return a - b


class Multiplicacion(Operacion):
    def __init__(self):
        super().__init__("*")

    def calcular(self, a, b):
        return a * b


class Division(Operacion):
    def __init__(self):
        super().__init__("÷")

    def calcular(self, a, b):
        if b == 0:
            raise DivisionPorCeroError("No se puede dividir por cero")
        return a / b
