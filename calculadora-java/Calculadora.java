import java.util.Scanner;

// Calculadora de consola con las cuatro operaciones básicas.
public class Calculadora {

    public static double sumar(double a, double b) {
        return a + b;
    }

    public static double restar(double a, double b) {
        return a - b;
    }

    public static double multiplicar(double a, double b) {
        return a * b;
    }

    public static double dividir(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("No se puede dividir por cero");
        }
        return a / b;
    }

    // Pide un número y lo vuelve a pedir si la entrada no es válida.
    public static double pedirNumero(Scanner scanner, String mensaje) {
        while (true) {
            System.out.print(mensaje);
            String texto = scanner.nextLine().trim();
            try {
                return Double.parseDouble(texto);
            } catch (NumberFormatException e) {
                System.out.println("Entrada no válida");
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nCalculadora");
            System.out.println("1) Sumar");
            System.out.println("2) Restar");
            System.out.println("3) Multiplicar");
            System.out.println("4) Dividir");
            System.out.println("5) Salir");
            System.out.print("Elige una opción: ");
            String opcion = scanner.nextLine().trim();

            if (opcion.equals("5")) {
                break;
            }
            if (!opcion.equals("1") && !opcion.equals("2") && !opcion.equals("3") && !opcion.equals("4")) {
                System.out.println("Opción no válida");
                continue;
            }

            double a = pedirNumero(scanner, "Escribe el primer número: ");
            double b = pedirNumero(scanner, "Escribe el segundo número: ");

            try {
                double resultado;
                switch (opcion) {
                    case "1" -> resultado = sumar(a, b);
                    case "2" -> resultado = restar(a, b);
                    case "3" -> resultado = multiplicar(a, b);
                    default -> resultado = dividir(a, b);
                }
                System.out.println("Resultado: " + resultado);
            } catch (ArithmeticException e) {
                System.out.println("No se puede dividir por cero");
            }
        }

        scanner.close();
    }
}
