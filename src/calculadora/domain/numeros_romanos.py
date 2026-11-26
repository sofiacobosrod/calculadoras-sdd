class ConversorNumeroRomano:
    # Diccionario de mayor a menor incluyendo las 6 restas especiales.
    # El orden importa: el algoritmo lo recorre de arriba hacia abajo.
    VALORES = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def convertir(self, numero):
        # La pantalla llega como texto ("385", "12.5"), así que lo convertimos a número.
        try:
            decimal = float(numero)
        except ValueError:
            return "Sin romano"

        # Los romanos solo existen para enteros del 1 al 3999.
        if decimal != int(decimal) or decimal < 1 or decimal > 3999:
            return "Sin romano"

        restante = int(decimal)   # lo que falta por convertir
        resultado = ""            # el texto romano, empieza vacío
        for valor, simbolo in self.VALORES.items():
            # Mientras el valor quepa en lo que falta: agrego su símbolo y lo resto.
            while restante >= valor:
                resultado += simbolo
                restante -= valor
        return resultado