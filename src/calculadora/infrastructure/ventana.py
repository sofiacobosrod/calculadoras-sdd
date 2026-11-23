import customtkinter as ctk

from src.calculadora.infrastructure.configuracion_botones import (
    COLORES,
    FILAS_BOTONES,
)


class VentanaCalculadora(ctk.CTk):
    def __init__(self, controlador, historial=None):
        super().__init__()
        self.controlador = controlador
        self.historial = historial if historial is not None else getattr(
            controlador, "historial", None
        )

        ctk.set_appearance_mode("dark")
        self.title("Mi Calculadora")
        self.geometry("380x620")
        self.resizable(False, False)
        self.configure(fg_color=COLORES["fondo"])

        for columna in range(12):
            self.grid_columnconfigure(columna, weight=1)

        self._crear_encabezado()
        self._crear_pantalla()
        self._crear_botones()
        self._crear_pie()
        self._actualizar_pantalla(
            {"expresion": "", "pantalla": "0"}
        )

    def _crear_encabezado(self):
        encabezado = ctk.CTkFrame(
            self,
            fg_color=COLORES["fondo"],
            corner_radius=0,
        )
        encabezado.grid(row=0, column=0, columnspan=12, sticky="nsew", padx=20, pady=(12, 8))

        icono = ctk.CTkLabel(
            encabezado,
            text="▦",
            text_color=COLORES["texto"],
            font=ctk.CTkFont(size=42),
            width=50,
        )
        icono.pack(side="left", padx=(0, 8))

        textos = ctk.CTkFrame(encabezado, fg_color="transparent")
        textos.pack(side="left", pady=2)

        titulo = ctk.CTkLabel(
            textos,
            text="Mi Calculadora",
            text_color=COLORES["texto"],
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        titulo.pack(anchor="w")

        subtitulo = ctk.CTkLabel(
            textos,
            text="Simple, rápida y diferente",
            text_color=COLORES["texto_secundario"],
            font=ctk.CTkFont(size=13),
        )
        subtitulo.pack(anchor="w")

    def _crear_pantalla(self):
        pantalla = ctk.CTkFrame(
            self,
            fg_color=COLORES["pantalla"],
            border_width=2,
            border_color=COLORES["borde"],
            corner_radius=18,
        )
        pantalla.grid(
            row=1,
            column=0,
            columnspan=12,
            sticky="nsew",
            padx=18,
            pady=(4, 12),
        )

        self.etiqueta_expresion = ctk.CTkLabel(
            pantalla,
            text="",
            text_color=COLORES["texto_secundario"],
            font=ctk.CTkFont(size=20),
            anchor="e",
        )
        self.etiqueta_expresion.pack(fill="x", padx=18, pady=(12, 0))

        self.etiqueta_resultado = ctk.CTkLabel(
            pantalla,
            text="0",
            text_color=COLORES["texto"],
            font=ctk.CTkFont(size=48, weight="bold"),
            anchor="e",
        )
        self.etiqueta_resultado.pack(fill="both", expand=True, padx=18, pady=(0, 8))

        self.etiqueta_letras = ctk.CTkLabel(
            pantalla,
            text="",
            text_color=COLORES["texto_secundario"],
            font=ctk.CTkFont(size=13),
            anchor="e",
            wraplength=300,
        )
        self.etiqueta_letras.pack(fill="x", padx=18, pady=(0, 10))

    def _crear_botones(self):
        for indice_fila, fila in enumerate(FILAS_BOTONES):
            columna_inicio = 0
            fila_numero = indice_fila + 2
            self.grid_rowconfigure(fila_numero, weight=1)

            for boton in fila:
                tipo = boton["tipo"]
                color = self._color_boton(tipo)
                texto = boton["texto"]

                if tipo == "historial":
                    comando = self._abrir_historial
                    texto_boton = "◷  " + texto
                elif tipo == "igual":
                    comando = lambda tecla=boton["tecla"]: self._al_presionar(tecla)
                    texto_boton = texto
                else:
                    comando = lambda tecla=boton["tecla"]: self._al_presionar(tecla)
                    texto_boton = texto

                widget = ctk.CTkButton(
                    self,
                    text=texto_boton,
                    command=comando,
                    fg_color=color,
                    hover_color=self._color_hover(tipo),
                    text_color=COLORES["texto"],
                    font=ctk.CTkFont(size=24, weight="bold"),
                    corner_radius=14,
                )
                widget.grid(
                    row=fila_numero,
                    column=columna_inicio,
                    columnspan=boton["columnas"],
                    sticky="nsew",
                    padx=5,
                    pady=5,
                )
                columna_inicio += boton["columnas"]

    def _crear_pie(self):
        pie = ctk.CTkLabel(
            self,
            text="Más que una calculadora",
            text_color=COLORES["texto_secundario"],
            font=ctk.CTkFont(size=14),
        )
        pie.grid(row=7, column=0, columnspan=12, sticky="nsew", pady=(8, 10))

    def _color_boton(self, tipo):
        colores = {
            "numero": COLORES["numero"],
            "operador": COLORES["operador"],
            "limpiar": COLORES["limpiar"],
            "igual": COLORES["igual"],
            "historial": COLORES["historial"],
        }
        return colores[tipo]

    def _color_hover(self, tipo):
        colores = {
            "numero": "#454B55",
            "operador": "#F59A45",
            "limpiar": "#F06065",
            "igual": "#2F78EA",
            "historial": "#43B75C",
        }
        return colores[tipo]

    def _al_presionar(self, tecla):
        estado = self.controlador.presionar(tecla)
        self._actualizar_pantalla(estado)

    def _actualizar_pantalla(self, estado):
        self.etiqueta_expresion.configure(text=estado["expresion"])
        self.etiqueta_resultado.configure(text=estado["pantalla"])
        self.etiqueta_letras.configure(text=estado.get("letras", ""))

    def _abrir_historial(self):
        ventana = ctk.CTkToplevel(self)
        ventana.title("Historial")
        ventana.geometry("360x260")
        ventana.resizable(False, False)
        ventana.configure(fg_color=COLORES["fondo"])

        if self.historial is None:
            textos = []
        else:
            textos = self.historial.ultimos(10)

        if not textos:
            etiquetas = ["Aún no hay cálculos"]
        else:
            etiquetas = []
            for calculo in textos:
                etiquetas.append(
                    f"{calculo.expresion} = {calculo.resultado} "
                    f"  ({calculo.fecha})"
                )

        for indice, texto in enumerate(etiquetas):
            etiqueta = ctk.CTkLabel(
                ventana,
                text=texto,
                text_color=COLORES["texto"],
                font=ctk.CTkFont(size=14),
                anchor="w",
            )
            etiqueta.pack(fill="x", padx=16, pady=(12 if indice == 0 else 4, 4))
