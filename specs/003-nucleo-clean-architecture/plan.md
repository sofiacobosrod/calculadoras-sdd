# Plan: Núcleo de la calculadora con Clean Architecture

## Tecnología
Python 3, sin librerías externas. Pruebas con unittest.

## Archivos

### Domain (reglas puras, no importa nada del proyecto)
- `src/calculadora/domain/errores.py` → clase `DivisionPorCeroError(Exception)`.
- `src/calculadora/domain/operaciones.py` →
  - clase abstracta `Operacion(ABC)` con atributo `simbolo` y método abstracto `calcular(a, b)`.
  - clases hijas: `Suma`, `Resta`, `Multiplicacion`, `Division`.
  - `Division.calcular` lanza `DivisionPorCeroError` si b es 0.

### Application (casos de uso, solo importa domain)
- `src/calculadora/application/calcular.py` → clase `CalcularUseCase`:
  - diccionario `self.operaciones = {"+": Suma(), "-": Resta(), "*": Multiplicacion(), "/": Division()}`
  - método `ejecutar(a, operador, b)` que busca la operación en el diccionario y la calcula.
- `src/calculadora/application/controlador.py` → clase `ControladorCalculadora`:
  - recibe un `CalcularUseCase` en el constructor (inyección de dependencias).
  - variables de instancia: `pantalla`, `expresion`, `acumulado`, `operador_pendiente`, `nuevo_numero`.
  - diccionario `SIMBOLOS = {"+": "+", "-": "−", "*": "×", "/": "÷"}` para mostrar los operadores.
  - diccionario de acciones `{"C": self._limpiar, "±": self._cambiar_signo, "%": self._porcentaje, "=": self._igual}`.
  - método público `presionar(tecla)` que devuelve `{"expresion": ..., "pantalla": ...}`.
  - teclas que recibe: dígitos "0"-"9", ".", "+", "-", "*", "/", "=", "C", "±", "%".

### Pruebas (espejo de src)
- `tests/calculadora/domain/test_operaciones.py`
- `tests/calculadora/application/test_calcular.py`
- `tests/calculadora/application/test_controlador.py` → prueba todos los criterios de aceptación con secuencias de teclas.

## Cómo probar
`python -m unittest discover -s tests -t . -v`