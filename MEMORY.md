# Memoria del proyecto

Bitácora de decisiones y avances. La entrada más reciente va al final.

## 2026-11-16
- Se creó la estructura SDD: constitución, agentes, memoria, plantillas y specs.
- Decisión: dos calculadoras. Python con GitHub Copilot y Java con OpenCode.

## 2026-11-17
- Se implementó la calculadora de consola en Python con suma, resta, multiplicación, división, menú y validación de entradas.
- Se añadieron pruebas unitarias para los criterios de aceptación y errores; `python -m unittest discover calculadora-python` pasó correctamente.
- Decisión: `dividir` propaga `ZeroDivisionError` y el menú lo captura para mostrar el mensaje requerido y continuar.

## 2026-11-17
- Se implementó la calculadora de consola en Java (`Calculadora.java` y `CalculadoraTest.java`) con suma, resta, multiplicación, división, menú y validación de entradas.
- Las pruebas se ejecutaron con `javac Calculadora.java CalculadoraTest.java` y `java CalculadoraTest`; todos los criterios de aceptación pasaron.
- Decisión: `dividir` lanza `ArithmeticException` cuando el divisor es cero y el menú la captura para mostrar "No se puede dividir por cero" y volver al menú.

## 2026-11-22
- Se implementó el núcleo Python de la spec 003 con Clean Architecture y POO.
- Se añadieron `DivisionPorCeroError`, operaciones abstractas e implementación, `CalcularUseCase`, `ControladorCalculadora` y pruebas espejo en domain/application.
- Las pruebas ejecutadas con `python -m unittest discover -s tests -t . -v` pasaron: 15 pruebas correctas.

## 2026-11-23
- Se implementó la interfaz gráfica de la spec 004 con CustomTkinter sin modificar domain ni application.
- Se añadieron la configuración visual de colores y botones, la ventana `VentanaCalculadora`, la conexión en `main.py` y las pruebas de infraestructura.
- El diseño usa tema oscuro, cuadrícula de 12 columnas, botones redondeados y colores acordes a la imagen de referencia.
- Las pruebas ejecutadas con `python -m unittest discover -s tests -t . -v` pasaron: 19 pruebas correctas.

## 2026-11-23
- Se implementó el historial de cálculos de la spec 005 siguiendo Clean Architecture.
- Se añadió `Calculo` en domain, el puerto `RepositorioHistorial` y `HistorialUseCase` en application, y `RepositorioHistorialJson` en infrastructure.
- El controlador registra solo resultados válidos de "=" y la ventana muestra los últimos 10 cálculos o el estado vacío.
- Las pruebas ejecutadas con `python -m unittest discover -s tests -t . -v` pasaron: 27 pruebas correctas.

## 2026-11-23
- Se implementó la función de número a letras de la spec 006 con lógica pura en domain.
- Se añadieron `ConversorNumeroALetras`, `ConvertirALetrasUseCase`, la clave `letras` en el estado del controlador y la tercera línea en la pantalla.
- Los criterios de aceptación incluyen rangos, negativos, decimales redondeados y los formatos completos solicitados.
- Las pruebas ejecutadas con `python -m unittest discover -s tests -t . -v` pasaron: 44 pruebas correctas.