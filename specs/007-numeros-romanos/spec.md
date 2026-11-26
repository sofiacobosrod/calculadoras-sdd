# Spec: Números romanos

## Objetivo
Mostrar debajo de la línea de letras el resultado escrito en números romanos, como cambio solicitado en la retroalimentación. Este cambio se implementa sin ayuda de IA.

## Usuario y escenario
La persona hace un cálculo en la ventana y, además del número y las letras, ve su equivalente en romano.

## Requisitos funcionales
- Debajo de la línea de letras aparece una cuarta línea, pequeña y en gris, con el número en romano.
- Se usan los símbolos I (1), V (5), X (10), L (50), C (100), D (500) y M (1000).
- Se aplican las 6 restas especiales: IV (4), IX (9), XL (40), XC (90), CD (400) y CM (900).
- Se actualiza con cada tecla, igual que la pantalla y las letras.

## Casos de error
- Los números romanos solo existen para enteros del 1 al 3999.
- Si el número es 0, negativo, decimal o mayor que 3999, la línea muestra "Sin romano".
- Si la pantalla muestra "Error", la línea queda vacía.

## Criterios de aceptación
- 1 → I
- 4 → IV
- 9 → IX
- 14 → XIV
- 40 → XL
- 385 → CCCLXXXV
- 2025 → MMXXV
- 3999 → MMMCMXCIX
- 0 → Sin romano
- -5 → Sin romano
- 12.5 → Sin romano
- 4000 → Sin romano