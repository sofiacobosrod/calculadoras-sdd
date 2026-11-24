from abc import ABC, abstractmethod


class RepositorioHistorial(ABC):
    @abstractmethod
    def guardar(self, calculo):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass
