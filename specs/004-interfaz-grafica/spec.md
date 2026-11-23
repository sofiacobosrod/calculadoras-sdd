# Spec: Interfaz gráfica de la calculadora

## Objetivo
Una ventana de escritorio con botones, muy parecida a la imagen `docs/ImagenDelResultado.png`, que usa el núcleo de la spec 003.

## Usuario y escenario
La persona ejecuta `python main.py`, se abre la ventana y calcula haciendo clic en los botones.

## Requisitos funcionales
- Tema oscuro.
- Encabezado: ícono de calculadora, título "Mi Calculadora" y subtítulo "Simple, rápida y diferente".
- Pantalla con borde redondeado, con dos líneas alineadas a la derecha:
  - arriba, en gris y más pequeña: la expresión (ejemplo "125 × 3 + 10")
  - abajo, en blanco, grande y en negrita: el resultado (ejemplo "385")
- Botones redondeados en este orden:
  - Fila 1: C, ±, %, ÷
  - Fila 2: 7, 8, 9, ×
  - Fila 3: 4, 5, 6, −
  - Fila 4: 1, 2, 3, +
  - Fila 5: Historial (más ancho), 0, ., =
- Colores de los botones:
  - C → rojo
  - números, ±, % y . → gris oscuro
  - ÷ × − + → naranja
  - = → azul
  - Historial → verde, con ícono de reloj
- Pie de página en gris: "Más que una calculadora".
- Cada clic envía la tecla al `ControladorCalculadora` y la pantalla muestra el diccionario de estado que devuelve.
- El botón Historial por ahora no hace nada (se implementa en la spec 005).

## Casos de error
- Si el núcleo responde "Error", la pantalla lo muestra sin que la ventana se cierre.

## Criterios de aceptación
- `python main.py` abre la ventana.
- Al hacer clic en 1 2 5 × 3 + 1 0 = se ve "125 × 3 + 10" arriba y "385" abajo.
- La ventana se parece a la imagen de referencia (colores, orden y forma de los botones).