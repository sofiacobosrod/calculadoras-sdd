from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


class ConversorNumeroALetras:
    UNIDADES = {
        0: "cero",
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis",
        7: "siete",
        8: "ocho",
        9: "nueve",
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince",
        16: "dieciséis",
        17: "diecisiete",
        18: "dieciocho",
        19: "diecinueve",
        20: "veinte",
        21: "veintiuno",
        22: "veintidós",
        23: "veintitrés",
        24: "veinticuatro",
        25: "veinticinco",
        26: "veintiséis",
        27: "veintisiete",
        28: "veintiocho",
        29: "veintinueve",
    }
    DECENAS = {
        30: "treinta",
        40: "cuarenta",
        50: "cincuenta",
        60: "sesenta",
        70: "setenta",
        80: "ochenta",
        90: "noventa",
    }
    CENTENAS = {
        100: "ciento",
        200: "doscientos",
        300: "trescientos",
        400: "cuatrocientos",
        500: "quinientos",
        600: "seiscientos",
        700: "setecientos",
        800: "ochocientos",
        900: "novecientos",
    }

    def convertir(self, numero):
        try:
            valor = Decimal(str(numero))
        except (InvalidOperation, ValueError):
            return "Número fuera de rango"

        if not valor.is_finite():
            return "Número fuera de rango"

        valor = valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if valor < Decimal("-999999999.99") or valor > Decimal("999999999.99"):
            return "Número fuera de rango"

        negativo = valor < 0
        absoluto = abs(valor)
        entero = int(absoluto)
        centavos = int((absoluto - Decimal(entero)) * 100)

        texto_entero = self._convertir_entero(entero)
        if negativo:
            texto_entero = "menos " + texto_entero

        return f"{texto_entero} con {centavos:02d}/100"

    def _convertir_entero(self, numero):
        if numero == 0:
            return "cero"
        if numero < 1000:
            return self._convertir_grupo(numero)
        if numero < 1000000:
            miles = numero // 1000
            resto = numero % 1000
            if miles == 1:
                texto = "mil"
            else:
                texto = f"{self._convertir_grupo(miles)} mil"
            if resto:
                texto += " " + self._convertir_grupo(resto)
            return texto

        millones = numero // 1000000
        resto = numero % 1000000
        if millones == 1:
            texto = "un millón"
        else:
            texto = f"{self._convertir_grupo(millones)} millones"
        if resto:
            texto_menor = self._convertir_entero(resto)
            texto += " " + texto_menor
        return texto

    def _convertir_grupo(self, numero):
        if numero < 30:
            return self.UNIDADES[numero]
        if numero < 100:
            decena = (numero // 10) * 10
            resto = numero % 10
            texto = self.DECENAS[decena]
            if resto:
                texto += " y " + self.UNIDADES[resto]
            return texto
        if numero == 100:
            return "cien"

        centena = (numero // 100) * 100
        texto = self.CENTENAS[centena]
        resto = numero % 100
        if resto:
            texto += " " + self._convertir_grupo(resto)
        return texto
