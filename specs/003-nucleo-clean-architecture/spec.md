# Spec: Núcleo de la calculadora con Clean Architecture

## Objetivo
Reconstruir la lógica de la calculadora Python usando Clean Architecture y Programación Orientada a Objetos, para que luego cualquier interfaz (ventana, web, terminal) pueda usarla.

## Usuario y escenario
La interfaz gráfica (spec 004) enviará cada tecla que presione el usuario y mostrará lo que el núcleo le responda.

## Requisitos funcionales
- Operaciones: suma, resta, multiplicación y división.
- Teclas especiales: C (limpiar todo), ± (cambiar signo), % (dividir el número actual entre 100), = (calcular), "." (decimal).
- Las operaciones se encadenan de izquierda a derecha: 125 × 3 + 10 = 385.
- Por cada tecla, el núcleo devuelve un diccionario con el estado:
  - "expresion": la operación escrita, por ejemplo "125 × 3 + 10"
  - "pantalla": el número que se muestra en grande, por ejemplo "385"
- Los números enteros se muestran sin ".0" (385 y no 385.0).

## Casos de error
- División por cero → "pantalla" muestra "Error" y "expresion" muestra "No se puede dividir por cero". La siguiente tecla numérica empieza de nuevo.
- No se permite escribir dos puntos decimales en el mismo número.

## Evidencias que debe tener el código
- Clases, incluyendo una clase abstracta y herencia.
- Variables de instancia dentro de las clases.
- Diccionarios para elegir la operación y para elegir la acción de cada tecla.

## Criterios de aceptación
- Teclas 2 + 3 = → pantalla "5"
- Teclas 1 2 5 × 3 + 1 0 = → expresion "125 × 3 + 10", pantalla "385"
- Teclas 8 ÷ 0 = → pantalla "Error"
- Teclas 5 ± → pantalla "-5"
- Teclas 5 0 % → pantalla "0.5"
- Teclas 4 × 2 . 5 = → pantalla "10"
- Tecla C → pantalla "0" y expresion vacía