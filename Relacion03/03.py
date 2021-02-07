"""
Ejercicio 03
Escribir un programa que reciba una a una las notas del usuario,
preguntando a cada paso si desea ingresar más notas, e imprimiendo el
promedio correspondiente.
"""

print("\x1b[1;33m", "Introduzca las notas del alumno")
print("\x1b[1;33m", "===============================")
i = 0
total = 0
masNotas = True
while masNotas:
    leyendo = True
    while leyendo:
        try:
            n = float(input("Introduzca nota: "))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico")

    total += n
    i += 1
    leyendo = True
    while leyendo:
        respuesta = input("¿Otra nota? (S/N)")
        if (respuesta in "SNsn") and not(respuesta == ""):
            leyendo = False
    if respuesta in "Nn":
        masNotas = False
print("\x1b[1;33m", "Su promedio es de", round(total / i, 2), "puntos")

