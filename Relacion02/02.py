"""
Ejercicio 02
Usando las funciones del ejercicio anterior, escribir un programa que lea de
teclado dos tiempos expresados en horas, minutos y segundos; las sume y
muestre el resultado en horas, minutos y segundos por pantalla.
"""

def horaSeg(h, m, s):
    return ((h * 60) + m)*60 + s


def segHora(s):
    horas = s // 3600
    s = s % 3600
    minutos = s // 60
    segundos = s % 60
    return horas, minutos, segundos

funcionamos = True
while funcionamos:
    try:
        h1 = int(input("Introduce horas    1: "))
        m1 = int(input("Introduce minutos  1: "))
        s1 = int(input("Introduce segundos 1: "))
        h2 = int(input("Introduce horas    2: "))
        m2 = int(input("Introduce minutos  2: "))
        s2 = int(input("Introduce segundos 2: "))
        funcionamos = False

    except ValueError:
        print("Error en la introducción de datos\n")

(h, m, s) = segHora(horaSeg(h1, m1, s1) + horaSeg(h2, m2, s2))

print("La suma es:", h, "horas", m, "minutos y", s, "segundos")