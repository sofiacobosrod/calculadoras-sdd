COLORES = {
    "fondo": "#1E2128",
    "pantalla": "#181B21",
    "borde": "#353B45",
    "numero": "#3A3F47",
    "operador": "#FF8A1F",
    "limpiar": "#E5484D",
    "igual": "#1F6FEB",
    "historial": "#2EA44F",
    "texto": "#FFFFFF",
    "texto_secundario": "#9AA0A6",
}


FILAS_BOTONES = [
    [
        {"texto": "C", "tecla": "C", "tipo": "limpiar", "columnas": 3},
        {"texto": "±", "tecla": "±", "tipo": "numero", "columnas": 3},
        {"texto": "%", "tecla": "%", "tipo": "numero", "columnas": 3},
        {"texto": "÷", "tecla": "/", "tipo": "operador", "columnas": 3},
    ],
    [
        {"texto": "7", "tecla": "7", "tipo": "numero", "columnas": 3},
        {"texto": "8", "tecla": "8", "tipo": "numero", "columnas": 3},
        {"texto": "9", "tecla": "9", "tipo": "numero", "columnas": 3},
        {"texto": "×", "tecla": "*", "tipo": "operador", "columnas": 3},
    ],
    [
        {"texto": "4", "tecla": "4", "tipo": "numero", "columnas": 3},
        {"texto": "5", "tecla": "5", "tipo": "numero", "columnas": 3},
        {"texto": "6", "tecla": "6", "tipo": "numero", "columnas": 3},
        {"texto": "−", "tecla": "-", "tipo": "operador", "columnas": 3},
    ],
    [
        {"texto": "1", "tecla": "1", "tipo": "numero", "columnas": 3},
        {"texto": "2", "tecla": "2", "tipo": "numero", "columnas": 3},
        {"texto": "3", "tecla": "3", "tipo": "numero", "columnas": 3},
        {"texto": "+", "tecla": "+", "tipo": "operador", "columnas": 3},
    ],
    [
        {"texto": "Historial", "tecla": None, "tipo": "historial", "columnas": 4},
        {"texto": "0", "tecla": "0", "tipo": "numero", "columnas": 3},
        {"texto": ".", "tecla": ".", "tipo": "numero", "columnas": 2},
        {"texto": "=", "tecla": "=", "tipo": "igual", "columnas": 3},
    ],
]
