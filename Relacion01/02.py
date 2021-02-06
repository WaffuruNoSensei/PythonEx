"""
Ejercicio 02
Escribir un programa que le pregunte al usuario una cantidad de euros, una
tasa de interés y un número de años y muestre como resultado el monto final a
obtener. La fórmula a utilizar es (interés compuesto):
Cf = Ci * (1 + i/100) ^ n
Donde Ci es el capital inicial, i es la tasa de interés y n es el número de
años a calcular.
"""

def calculoInteres(ci, i, n):
    return ci * (1+ i/100) ** n

leyendo = True

while leyendo:
    try:
       ci = float(input("Introduce el capital inicial: "))
       annos = float(input("Introduce los años: "))
       interes = float(input("Introduce el interés en tanto por ciento (%) "))
       leyendo = False
    except ValueError:
        print("Error en la introducción de datos\n")

print("\x1b[1;33m" + "Total a pagar:", round(calculoInteres(ci,annos,interes), 2), "euros")