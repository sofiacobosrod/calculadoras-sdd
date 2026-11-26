# Plan: Números romanos

## Tecnología
Python 3, sin librerías externas. Pruebas con unittest.

## Archivos

### Domain
- `src/calculadora/domain/numeros_romanos.py` → clase `ConversorNumeroRomano`:
  - diccionario `VALORES` de mayor a menor, con las 6 restas especiales (1000: "M", 900: "CM", ..., 1: "I").
  - método `convertir(numero)`: convierte el texto a número; si no es entero entre 1 y 3999 devuelve "Sin romano".
  - algoritmo: recorre el diccionario y, mientras el valor quepa en lo que falta, agrega el símbolo y resta el valor.

### Application
- `src/calculadora/application/convertir_romano.py` → clase `ConvertirARomanoUseCase` que recibe el conversor y tiene `ejecutar(numero)` (mismo patrón que `ConvertirALetrasUseCase`).
- Modificar `ControladorCalculadora`: recibir opcionalmente `convertir_romano` y agregar la clave "romano" al diccionario de estado ("" si la pantalla es "Error").

### Infrastructure
- Modificar `VentanaCalculadora`: agregar la etiqueta `etiqueta_romano` debajo de `etiqueta_letras` y actualizarla en `_actualizar_pantalla`. Aumentar la altura de la ventana a 400x650.

### Punto de entrada
- Modificar `main.py`: importar las clases nuevas, crear `ConvertirARomanoUseCase(ConversorNumeroRomano())` y pasárselo al controlador.

### Pruebas
- `tests/calculadora/domain/test_numeros_romanos.py` → todos los criterios de aceptación.
- Actualizar las pruebas del controlador si comparan el diccionario completo (ahora incluye "romano").

## Cómo probar
- Pruebas: `python -m unittest discover -s tests -t . -v`
- App: `python main.py`