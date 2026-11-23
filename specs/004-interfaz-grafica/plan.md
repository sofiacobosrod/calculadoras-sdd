# Plan: Interfaz gráfica de la calculadora

## Tecnología
Python 3 + CustomTkinter (ver requirements.txt).

## Archivos

### Infrastructure
- `src/calculadora/infrastructure/configuracion_botones.py` → SIN importar customtkinter, para poder probarlo:
  - diccionario `COLORES` con claves "fondo", "pantalla", "borde", "numero", "operador", "limpiar", "igual", "historial", "texto", "texto_secundario".
    Valores sugeridos: fondo "#1E2128", pantalla "#181B21", borde "#353B45", numero "#3A3F47", operador "#FF8A1F", limpiar "#E5484D", igual "#1F6FEB", historial "#2EA44F", texto "#FFFFFF", texto_secundario "#9AA0A6".
  - lista `FILAS_BOTONES`: cada botón es un diccionario {"texto": "×", "tecla": "*", "tipo": "operador", "columnas": 3}.
  - Cuadrícula de 12 columnas: en las filas 1 a 4 cada botón ocupa 3 columnas; en la fila 5: Historial 4, 0 3, "." 2, "=" 3.
- `src/calculadora/infrastructure/ventana.py` → clase `VentanaCalculadora(ctk.CTk)`:
  - recibe un `ControladorCalculadora` en el constructor (inyección de dependencias).
  - crea encabezado, pantalla, botones (recorriendo `FILAS_BOTONES`) y pie de página.
  - método `_al_presionar(tecla)` que llama a `controlador.presionar(tecla)` y actualiza las etiquetas con el diccionario.
  - método `_abrir_historial()` vacío por ahora.
  - tamaño aproximado 380 x 620, no redimensionable, esquinas de botones redondeadas (corner_radius 14).

### Punto de entrada
- `main.py` → crea `CalcularUseCase`, se lo pasa a `ControladorCalculadora`, se lo pasa a `VentanaCalculadora` y llama a `mainloop()`. Usa `if __name__ == "__main__":`.

### Pruebas
- `tests/calculadora/infrastructure/test_configuracion_botones.py` → verifica que haya 20 botones, que todos los tipos tengan color en `COLORES` y que cada fila sume 12 columnas.

## Cómo probar
- Pruebas: `python -m unittest discover -s tests -t . -v`
- App: `python main.py`