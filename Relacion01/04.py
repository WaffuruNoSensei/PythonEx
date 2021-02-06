"""
Ejercicio 04
Utilice el programa anterior para generar una tabla de conversión de
temperaturas, desde 0º F hasta 120º F, de 10 en 10.
"""

def fahrtocelsius (f):
    return (f-32) * 5/9

print("\x1b[1;33m" + "Grados Fahrenheit   Grados Celsius")
print("\x1b[1;33m" + "=================   ==============")
for f in range(0,121, 10):
    if f < 10:
        print("\x1b[1;33m" + "      ", f, "             ", round(fahrtocelsius(f), 2))
    elif f < 100:
        if round(fahrtocelsius(f), 2) < 0:
            print("\x1b[1;33m" + "      ", f, "            ", round(fahrtocelsius(f), 2))
        else:
            print("\x1b[1;33m" + "      ", f, "             ", round(fahrtocelsius(f), 2))
    else:
        print("\x1b[1;33m" + "      ", f, "            ", round(fahrtocelsius(f), 2))