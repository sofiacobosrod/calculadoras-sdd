# Plan: Historial de cálculos

## Archivos

### Domain
- `src/calculadora/domain/calculo.py` → clase `Calculo` con atributos `expresion`, `resultado`, `fecha`.
  - método `a_diccionario()` que devuelve {"expresion": ..., "resultado": ..., "fecha": ...}
  - método de clase `desde_diccionario(datos)` que crea un `Calculo` a partir de un diccionario.

### Application
- `src/calculadora/application/puertos.py` → clase abstracta `RepositorioHistorial(ABC)` con métodos abstractos `guardar(calculo)` y `obtener_todos()`.
- `src/calculadora/application/historial.py` → clase `HistorialUseCase`:
  - recibe un `RepositorioHistorial` en el constructor.
  - `registrar(expresion, resultado)` crea un `Calculo` con la fecha actual y lo guarda.
  - `ultimos(cantidad=10)` devuelve los más recientes primero.
- Modificar `ControladorCalculadora`: recibir opcionalmente un `HistorialUseCase` y llamar a `registrar` cuando "=" da un resultado válido.

### Infrastructure
- `src/calculadora/infrastructure/repositorio_json.py` → clase `RepositorioHistorialJson(RepositorioHistorial)`:
  - guarda una lista de diccionarios en `historial.json` con el módulo `json` (UTF-8, `ensure_ascii=False`).
  - si el archivo no existe o está dañado, devuelve una lista vacía.
- Modificar `VentanaCalculadora._abrir_historial()` para abrir un `CTkToplevel` con los últimos 10 cálculos.
- Modificar `main.py` para crear `RepositorioHistorialJson` y `HistorialUseCase` y conectarlos.

### Pruebas
- `tests/calculadora/domain/test_calculo.py` → ida y vuelta entre `Calculo` y diccionario.
- `tests/calculadora/application/test_historial.py` → usa una clase `RepositorioEnMemoria` definida en la prueba (sin archivos).
- `tests/calculadora/application/test_controlador.py` → agregar: "=" válido registra, error no registra.
- `tests/calculadora/infrastructure/test_repositorio_json.py` → usa un archivo temporal (`tempfile`) y prueba archivo inexistente y dañado.