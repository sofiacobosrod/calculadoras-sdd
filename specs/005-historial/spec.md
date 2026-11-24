# Spec: Historial de cálculos

## Objetivo
Guardar cada cálculo terminado y poder consultarlo con el botón "Historial", aunque se cierre la calculadora.

## Requisitos funcionales
- Cada vez que se presiona "=" y el resultado es válido, se guarda: expresión, resultado y fecha/hora.
- Los cálculos con error (división por cero) NO se guardan.
- El historial se guarda en el archivo `historial.json` y se conserva al cerrar y abrir la app.
- El botón "Historial" abre una ventana pequeña con los últimos 10 cálculos, del más reciente al más antiguo, con el formato:
  "125 × 3 + 10 = 385   (23/11/2026 09:30)"
- Si no hay cálculos, muestra "Aún no hay cálculos".

## Casos de error
- Si `historial.json` no existe o está dañado, la app arranca con el historial vacío y no se cierra.

## Criterios de aceptación
- Después de calcular 2 + 3 = y abrir Historial, aparece "2 + 3 = 5".
- Después de 8 ÷ 0 =, el historial no cambia.
- Al cerrar y abrir la app, el historial sigue ahí.
- Al presionar "=" en la ventana, la app NO se cae y el cálculo se guarda en historial.json como diccionario.
- Al presionar "=" una vez, se guarda UN solo registro en el historial.