from src.calculadora.application.calcular import CalcularUseCase
from src.calculadora.application.controlador import ControladorCalculadora
from src.calculadora.application.historial import HistorialUseCase
from src.calculadora.application.convertir_letras import ConvertirALetrasUseCase
from src.calculadora.application.convertir_romano import ConvertirARomanoUseCase
from src.calculadora.domain.numero_a_letras import ConversorNumeroALetras
from src.calculadora.domain.numeros_romanos import ConversorNumeroRomano
from src.calculadora.infrastructure.ventana import VentanaCalculadora
from src.calculadora.infrastructure.repositorio_json import RepositorioHistorialJson


if __name__ == "__main__":
    calcular = CalcularUseCase()
    repositorio = RepositorioHistorialJson()
    historial = HistorialUseCase(repositorio)
    convertir_letras = ConvertirALetrasUseCase(ConversorNumeroALetras())
    convertir_romano = ConvertirARomanoUseCase(ConversorNumeroRomano())
    controlador = ControladorCalculadora(
        calcular, historial, convertir_letras, convertir_romano
    )
    ventana = VentanaCalculadora(controlador, historial)
    ventana.mainloop()