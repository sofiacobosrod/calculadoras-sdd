# Plan: Calculadora en Java

## Tecnología
Java 21 (JDK), sin librerías externas.

## Archivos
- `calculadora-java/Calculadora.java` → métodos de cálculo y menú.
- `calculadora-java/CalculadoraTest.java` → pruebas simples que verifican los resultados.

## Diseño
- Métodos estáticos: `sumar`, `restar`, `multiplicar`, `dividir` (reciben y devuelven `double`).
- `dividir` lanza `ArithmeticException` si el divisor es 0; el menú la captura y muestra el mensaje.
- Usar `Scanner` para leer la entrada y validar que sea un número.
- Menú dentro de un bucle `while` en el método `main`.

## Cómo probar
Desde la carpeta `calculadora-java`:
- Compilar: `javac Calculadora.java CalculadoraTest.java`
- Ejecutar: `java Calculadora`
- Pruebas: `java CalculadoraTest`