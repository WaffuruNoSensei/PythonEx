"""
Ejercicio 05
Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario
"""

leyendo = True

while leyendo:
    try:
        nIni = int(input("Introduzca el valor inicial: "))
        nFin = int(input("Introduca el valor final: "))
        leyendo = False
    except ValueError:
        print("Introduce solo valores numéricos enteros\n")

nIni += nIni % 2
for i in range(nIni, nFin+1, 2):
    print("\x1b[1;33m", i)