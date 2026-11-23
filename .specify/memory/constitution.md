# Constitución del proyecto

Estas reglas son obligatorias para cualquier persona o agente de IA que trabaje en el proyecto.

1. **Primero la especificación.** No se escribe código sin una spec en la carpeta `specs/`.
2. **Operaciones mínimas.** Cada calculadora soporta suma, resta, multiplicación y división.
3. **Errores controlados.** La división por cero y las entradas inválidas muestran un mensaje claro; el programa nunca se cierra por un error.
4. **Pruebas.** Todo el código tiene pruebas básicas que demuestran los criterios de aceptación.
5. **Simplicidad.** Código corto y legible. Nombres y comentarios en español.
6. **Trabajo con ramas.** Cada cambio se hace en una rama y entra a `main` por Pull Request.
7. **Memoria.** Cada avance importante se registra en `MEMORY.md`.
8. **Clean Architecture.** El código Python vive en `src/calculadora/` dividido en `domain`, `application` e `infrastructure`. Las dependencias apuntan hacia adentro: domain no conoce a nadie.
9. **Programación Orientada a Objetos.** La lógica va en clases. Se usan diccionarios para mapear opciones en lugar de cadenas de if/elif.
10. **Una spec por funcionalidad.** Cada funcionalidad nueva tiene su propia carpeta en `specs/`.
11. **Pruebas espejo.** `tests/` replica la estructura de `src/`.