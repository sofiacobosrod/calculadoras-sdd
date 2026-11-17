# Plan: Calculadora en Python

## Tecnología
Python 3 (sin librerías externas).

## Archivos
- `calculadora-python/calculadora.py` → funciones de cálculo y menú.
- `calculadora-python/test_calculadora.py` → pruebas con `unittest`.

## Diseño
- Cuatro funciones: `sumar(a, b)`, `restar(a, b)`, `multiplicar(a, b)`, `dividir(a, b)`.
- `dividir` lanza `ZeroDivisionError` si `b` es 0; el menú la captura y muestra el mensaje.
- Función `pedir_numero(mensaje)` que repite la pregunta hasta recibir un número válido.
- Función `main()` con el menú dentro de un bucle `while`.

## Cómo probar
- Ejecutar: `python calculadora-python/calculadora.py`
- Pruebas: `python -m unittest discover calculadora-python`