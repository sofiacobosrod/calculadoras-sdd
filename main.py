from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.infrastructure.ventana import VentanaCalculadora


if __name__ == "__main__":
    calcular = CalcularUseCase()
    controlador = ControladorCalculadora(calcular)
    ventana = VentanaCalculadora(controlador)
    ventana.mainloop()