from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.application.historial import HistorialUseCase
from src.calculadora.infrastructure.ventana import VentanaCalculadora
from src.calculadora.infrastructure.repositorio_json import RepositorioHistorialJson


if __name__ == "__main__":
    calcular = CalcularUseCase()
    repositorio = RepositorioHistorialJson()
    historial = HistorialUseCase(repositorio)
    controlador = ControladorCalculadora(calcular, historial)
    ventana = VentanaCalculadora(controlador, historial)
    ventana.mainloop()