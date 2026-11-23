from src.calculadora.domain.errores import DivisionPorCeroError


class ControladorCalculadora:
    SIMBOLOS = {
        "+": "+",
        "-": "−",
        "*": "×",
        "/": "÷",
    }

    def __init__(self, calcular):
        self.calcular = calcular
        self.pantalla = "0"
        self.expresion = ""
        self.acumulado = None
        self.operador_pendiente = None
        self.nuevo_numero = True
        self.error = False
        self.acciones = {
            "C": self._limpiar,
            "±": self._cambiar_signo,
            "%": self._porcentaje,
            "=": self._igual,
        }

    def presionar(self, tecla):
        if tecla in self.acciones:
            self.acciones[tecla]()
        elif tecla in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            self._numero(tecla)
        elif tecla == ".":
            self._decimal()
        elif tecla in self.SIMBOLOS:
            self._operador(tecla)
        else:
            raise ValueError("Tecla no valida")

        return {"expresion": self.expresion, "pantalla": self.pantalla}

    def _limpiar(self):
        self.pantalla = "0"
        self.expresion = ""
        self.acumulado = None
        self.operador_pendiente = None
        self.nuevo_numero = True
        self.error = False

    def _numero(self, tecla):
        if self.error:
            self._limpiar()
        if self.nuevo_numero:
            self.pantalla = tecla
            self.nuevo_numero = False
        elif self.pantalla == "0":
            self.pantalla = tecla
        else:
            self.pantalla += tecla

    def _decimal(self):
        if self.error:
            self._limpiar()
        if self.nuevo_numero:
            self.pantalla = "0."
            self.nuevo_numero = False
        elif "." not in self.pantalla:
            self.pantalla += "."

    def _cambiar_signo(self):
        if self.error:
            return
        numero = float(self.pantalla)
        numero *= -1
        self.pantalla = self._formatear(numero)

    def _porcentaje(self):
        if self.error:
            return
        numero = float(self.pantalla) / 100
        self.pantalla = self._formatear(numero)

    def _operador(self, operador):
        if self.error:
            return

        if self.operador_pendiente is not None:
            if not self.nuevo_numero:
                numero_actual = self.pantalla
                resultado = self._calcular_pendiente()
                if resultado is None:
                    return
                self.expresion = (
                    f"{self.expresion} {numero_actual} "
                    f"{self.SIMBOLOS[operador]}"
                )
            else:
                simbolos = list(self.SIMBOLOS)
                ultimo = self.expresion[-1:]
                if ultimo in ("+", "−", "×", "÷"):
                    self.expresion = (
                        self.expresion[:-1].rstrip()
                        + " "
                        + self.SIMBOLOS[operador]
                    )
        else:
            self.acumulado = float(self.pantalla)
            self.expresion = (
                f"{self._formatear(self.acumulado)} {self.SIMBOLOS[operador]}"
            )

        self.operador_pendiente = operador
        self.nuevo_numero = True

    def _igual(self):
        if self.error:
            return
        if self.operador_pendiente is None:
            return
        if not self.expresion.endswith(self.SIMBOLOS[self.operador_pendiente]):
            pass
        else:
            self.expresion = f"{self.expresion} {self.pantalla}"
        resultado = self._calcular_pendiente()
        if resultado is not None:
            self.operador_pendiente = None
            self.nuevo_numero = True

    def _calcular_pendiente(self):
        try:
            resultado = self.calcular.ejecutar(
                self.acumulado,
                self.operador_pendiente,
                float(self.pantalla),
            )
        except DivisionPorCeroError:
            self.pantalla = "Error"
            self.expresion = "No se puede dividir por cero"
            self.acumulado = None
            self.operador_pendiente = None
            self.nuevo_numero = True
            self.error = True
            return None

        self.acumulado = float(resultado)
        self.pantalla = self._formatear(resultado)
        return resultado

    @staticmethod
    def _formatear(numero):
        numero = float(numero)
        if numero == 0:
            return "0"
        if numero.is_integer():
            return str(int(numero))
        return str(numero)
