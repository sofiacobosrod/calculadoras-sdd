# Memoria del proyecto

Bitácora de decisiones y avances. La entrada más reciente va al final.

## 2026-11-16
- Se creó la estructura SDD: constitución, agentes, memoria, plantillas y specs.
- Decisión: dos calculadoras. Python con GitHub Copilot y Java con OpenCode.

## 2026-11-17
- Se implementó la calculadora de consola en Python con suma, resta, multiplicación, división, menú y validación de entradas.
- Se añadieron pruebas unitarias para los criterios de aceptación y errores; `python -m unittest discover calculadora-python` pasó correctamente.
- Decisión: `dividir` propaga `ZeroDivisionError` y el menú lo captura para mostrar el mensaje requerido y continuar.