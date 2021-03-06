"""
Ejercicio 01
Escribir funciones que resuelvan los siguientes problemas:
Dado un número entero n, indicar si es o no par.
"""

from math import sqrt


def par(n):
    return n % 2 == 0


"""Dado un número entero n, indicar si es o no primo."""


def primo(n):
    primo = True
    if not (n % 2):
        for i in (3, sqrt(n) + 1, 2):
            if n % i == 0:
                primo = False
                break
        return primo
