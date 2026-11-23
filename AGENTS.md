# Instrucciones para agentes de IA (GitHub Copilot / OpenCode)

## Antes de escribir código
1. Lee `.specify/memory/constitution.md`. Sus reglas son obligatorias.
2. Lee la carpeta de `specs/` que corresponda a tu tarea.
3. Implementa SOLO lo que dice la spec. No agregues funciones extra.

## Skills disponibles (en `.github/skills/`)
- `clean-architecture` → úsalo siempre que escribas código en `src/` o `tests/`.
- `crear-spec` → úsalo cuando se pida crear una spec nueva.

## Mientras trabajas
- Sigue las tareas de `tasks.md` en orden.
- Marca cada tarea terminada cambiando `- [ ]` por `- [x]`.
- Escribe código simple, con nombres y comentarios en español.

## Dónde va cada cosa
- Calculadora Python v2 (Clean Architecture) → `src/calculadora/`, `tests/calculadora/` y `main.py` (herramienta: GitHub Copilot).
- Calculadora Python v1 (versión original) → `calculadora-python/` (no se modifica).
- Calculadora Java → `calculadora-java/` (herramienta: OpenCode).
- Imagen de referencia del diseño → `docs/ImagenDelResultado.png`.

## Al terminar
- Ejecuta todas las pruebas: `python -m unittest discover -s tests -t . -v`
- Agrega una entrada en `MEMORY.md` con la fecha, qué hiciste y qué decisiones tomaste.