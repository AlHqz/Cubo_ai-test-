import os
import sys

if __name__ == "__main__":
    print("Ingrese la cantidad a invertir: ")
    cantidad = float(input("$"))
    print("Ingrese el porcentaje de interés anual: ")
    interes = float(input("% "))
    print("Ingrese el número de años: ")
    años = int(input())

    total = cantidad
    interes_total = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Cantidad inicial: ${cantidad:.2f}")
    print(f"Interés anual: {interes:.2f}%")
    print(f"Plazo: {años} años")
    print("---------------------------------------------------")

    for i in range(años):
        interes_anual = total * (interes / 100)
        interes_total += interes_anual
        total += interes_anual
        print(f"Año {i + 1}: ${total:.2f} - Interés: ${interes_anual:.2f}")

    print(f"Interés total acumulado: ${interes_total:.2f}")
    print("---------------------------------------------------")