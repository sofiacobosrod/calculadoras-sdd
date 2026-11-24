# Spec: Número a letras (función única)

## Objetivo
Mostrar debajo del resultado el número escrito en palabras en español, con los centavos en formato de factura (XX/100). Ninguna calculadora común lo tiene y es útil para llenar facturas, recibos y cheques.

## Requisitos funcionales
- Debajo del resultado aparece una tercera línea, pequeña y en gris, con el número en letras.
- Formato: parte entera en palabras + " con " + dos decimales + "/100".
- Soporta números desde -999.999.999,99 hasta 999.999.999,99.
- Los negativos empiezan con "menos".
- Los decimales se redondean a 2 cifras.
- Se actualiza con cada tecla, igual que la pantalla.

## Casos de error
- Si la pantalla muestra "Error", la línea de letras queda vacía.
- Si el número está fuera de rango, muestra "Número fuera de rango".

## Criterios de aceptación
- 0 → "cero con 00/100"
- 15 → "quince con 00/100"
- 21 → "veintiuno con 00/100"
- 100 → "cien con 00/100"
- 101 → "ciento uno con 00/100"
- 385 → "trescientos ochenta y cinco con 00/100"
- 1000 → "mil con 00/100"
- 2025 → "dos mil veinticinco con 00/100"
- 1000000 → "un millón con 00/100"
- 2500000 → "dos millones quinientos mil con 00/100"
- 12.5 → "doce con 50/100"
- -7 → "menos siete con 00/100"