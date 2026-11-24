# Plan: Número a letras

## Archivos

### Domain
- `src/calculadora/domain/numero_a_letras.py` → clase `ConversorNumeroALetras`:
  - diccionario `UNIDADES` del 0 al 29 (ejemplo {0: "cero", 1: "uno", ..., 21: "veintiuno", ..., 29: "veintinueve"}).
  - diccionario `DECENAS` {30: "treinta", 40: "cuarenta", ..., 90: "noventa"}.
  - diccionario `CENTENAS` {100: "ciento", 200: "doscientos", ..., 900: "novecientos"} (100 exacto = "cien").
  - método `convertir(numero)` que devuelve el texto completo con "con XX/100".
  - métodos privados para convertir grupos de 3 cifras, miles y millones ("un millón" / "X millones").

### Application
- `src/calculadora/application/convertir_letras.py` → clase `ConvertirALetrasUseCase` que recibe el conversor y tiene `ejecutar(numero)`.
- Modificar `ControladorCalculadora`: recibir opcionalmente el caso de uso y agregar la clave "letras" al diccionario de estado ("" si la pantalla es "Error").

### Infrastructure
- Modificar `VentanaCalculadora`: agregar una tercera etiqueta en la pantalla para "letras" (gris, pequeña, alineada a la derecha, con ajuste de línea).
- Modificar `main.py` para conectar el conversor y el caso de uso.

### Pruebas
- `tests/calculadora/domain/test_numero_a_letras.py` → todos los criterios de aceptación.
- `tests/calculadora/application/test_convertir_letras.py`.
- `tests/calculadora/application/test_controlador.py` → agregar la clave "letras".