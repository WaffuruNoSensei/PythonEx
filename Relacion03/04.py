"""
Ejercicio 04
Escribir una función que reciba un número entero k e imprima su
descomposición en factores primos.
>>> factPrimos(24)
1
2
2
2
3
>>> factPrimos(100)
1
2
2
5
5
>>> factPrimos(12)
1
2
2
3
>>> factPrimos(11)
1
11
>>> factPrimos(1)
1
>>> factPrimos(0)
1
"""


def factPrimos(n):
    if n < 2:
        print(1)
    else:
        i = 2
        print(1)
        while (n / 2 + 1) > i:
            if n % i == 0:
                print(i)
                n //= i
            else:
                i += 1
        print(n)
