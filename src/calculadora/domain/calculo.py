class Calculo:
    def __init__(self, expresion, resultado, fecha):
        self.expresion = expresion
        self.resultado = resultado
        self.fecha = fecha

    def a_diccionario(self):
        return {
            "expresion": self.expresion,
            "resultado": self.resultado,
            "fecha": self.fecha,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["expresion"],
            datos["resultado"],
            datos["fecha"],
        )
