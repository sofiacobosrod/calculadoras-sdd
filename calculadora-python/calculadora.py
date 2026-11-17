def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida")


def main():
    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir,
    }

    while True:
        print("\nCalculadora")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "5":
            break
        if opcion not in operaciones:
            print("Opción no válida")
            continue

        a = pedir_numero("Escribe el primer número: ")
        b = pedir_numero("Escribe el segundo número: ")

        try:
            resultado = operaciones[opcion](a, b)
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        else:
            print(f"Resultado: {resultado:g}")


if __name__ == "__main__":
    main()
