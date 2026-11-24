class ConvertirALetrasUseCase:
    def __init__(self, conversor):
        self.conversor = conversor

    def ejecutar(self, numero):
        return self.conversor.convertir(numero)
