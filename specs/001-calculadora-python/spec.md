# Spec: Calculadora en Python

## Objetivo
Una calculadora de consola (terminal) que realiza operaciones matemáticas básicas.

## Usuario y escenario
Una persona abre la terminal, ejecuta el programa y hace cálculos rápidos.

## Requisitos funcionales
- El programa muestra un menú: 1) Sumar 2) Restar 3) Multiplicar 4) Dividir 5) Salir.
- El usuario elige una opción y escribe dos números (enteros o con decimales).
- El programa muestra el resultado.
- Después de cada operación vuelve al menú, hasta que el usuario elija Salir.

## Casos de error
- División por cero → muestra "No se puede dividir por cero" y vuelve al menú.
- Si el usuario escribe texto en vez de un número → muestra "Entrada no válida" y lo pide de nuevo.
- Si elige una opción que no existe → muestra "Opción no válida".

## Criterios de aceptación
- 2 + 3 = 5
- 5 - 7 = -2
- 4 * 2.5 = 10
- 8 / 2 = 4
- 3 / 0 muestra "No se puede dividir por cero"