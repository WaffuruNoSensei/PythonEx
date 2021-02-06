"""
Ejercicio 03
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: F = 9/5 * C + 32.
"""

def fahrtocelsius (f):
    return (f-32) * 5/9

leyendo = True

while leyendo:
    try:
        f = float(input("Introduce la temperatura en grados Fahrenheit: "))
        leyendo = False
    except ValueError:
        print("Introduce un valor numérico porfavor\n")

print("\x1b[1;33m" + "La temperatura en grados Celsius es: ", round(fahrtocelsius(f), 2))
