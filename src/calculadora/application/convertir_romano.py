class ConvertirARomanoUseCase:
    # Recibe el conversor del domain (inyección de dependencias).
    def __init__(self, conversor):
        self.conversor = conversor

    # Le pasa el trabajo al conversor y devuelve el resultado.
    def ejecutar(self, numero):
        return self.conversor.convertir(numero)
    