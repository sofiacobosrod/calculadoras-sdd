// Pruebas simples sin librerías externas para los criterios de aceptación.
public class CalculadoraTest {

    private static int fallos = 0;

    private static void verificar(String descripcion, double esperado, double obtenido) {
        if (esperado == obtenido) {
            System.out.println("OK: " + descripcion);
        } else {
            System.out.println("FALLO: " + descripcion + " (esperado " + esperado + ", obtenido " + obtenido + ")");
            fallos++;
        }
    }

    public static void main(String[] args) {
        verificar("2 + 3 = 5", 5, Calculadora.sumar(2, 3));
        verificar("5 - 7 = -2", -2, Calculadora.restar(5, 7));
        verificar("4 * 2.5 = 10", 10, Calculadora.multiplicar(4, 2.5));
        verificar("8 / 2 = 4", 4, Calculadora.dividir(8, 2));

        // La división por cero debe lanzar el error que el menú captura.
        try {
            Calculadora.dividir(3, 0);
            System.out.println("FALLO: 3 / 0 debía lanzar ArithmeticException");
            fallos++;
        } catch (ArithmeticException e) {
            System.out.println("OK: 3 / 0 lanza ArithmeticException");
        }

        if (fallos == 0) {
            System.out.println("Todas las pruebas pasaron");
        } else {
            System.out.println("Pruebas fallidas: " + fallos);
            System.exit(1);
        }
    }
}
