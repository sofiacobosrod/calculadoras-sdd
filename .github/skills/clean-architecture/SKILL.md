---
name: clean-architecture
description: Usar al crear o modificar código Python de la calculadora en src/ o tests/. Define las capas domain, application e infrastructure, la regla de dependencia y el estilo con clases y diccionarios.
---

# Skill: Clean Architecture para la calculadora

## Estructura obligatoria

    src/calculadora/
        domain/          -> reglas puras: entidades, operaciones, errores
        application/     -> casos de uso y controladores
        infrastructure/  -> interfaz gráfica (CustomTkinter) y archivos
    tests/calculadora/
        domain/          -> pruebas del domain
        application/     -> pruebas de application
        infrastructure/  -> pruebas de infrastructure
    main.py              -> único punto de entrada; conecta las capas

## Regla de dependencia
- domain NO importa nada de application ni de infrastructure.
- application solo importa de domain.
- infrastructure puede importar de application y domain.
- main.py crea los objetos y los conecta (inyección de dependencias).

## Estilo de código
- Toda la lógica va dentro de clases (Programación Orientada a Objetos).
- Usar clases abstractas (ABC) cuando haya varias versiones de lo mismo.
- Usar diccionarios para elegir comportamientos, en vez de cadenas largas de if/elif.
  Ejemplo: {"+": Suma(), "-": Resta()}.
- Nombres de clases, variables y comentarios en español.
- Imports absolutos desde la raíz: from src.calculadora.domain.operaciones import Suma

## Pruebas
- Por cada archivo en src/ hay un archivo test_*.py en la misma capa dentro de tests/.
- Usar unittest. Ejecutar con: python -m unittest discover -s tests -t . -v
- Toda prueba debe pasar antes de dar la tarea por terminada.