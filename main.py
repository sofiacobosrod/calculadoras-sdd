from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.application.historial import HistorialUseCase
from src.calculadora.application.convertir_letras import ConvertirALetrasUseCase
from src.calculadora.domain.numero_a_letras import ConversorNumeroALetras
from src.calculadora.infrastructure.ventana import VentanaCalculadora
from src.calculadora.infrastructure.repositorio_json import RepositorioHistorialJson


if __name__ == "__main__":
    calcular = CalcularUseCase()
    repositorio = RepositorioHistorialJson()
    historial = HistorialUseCase(repositorio)
    convertir_letras = ConvertirALetrasUseCase(ConversorNumeroALetras())
    controlador = ControladorCalculadora(calcular, historial, convertir_letras)
    ventana = VentanaCalculadora(controlador, historial)
    ventana.mainloop()