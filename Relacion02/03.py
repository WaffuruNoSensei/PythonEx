"""
Ejercicio 03
Escribir una función que dados cuatro números, devuelva el mayor producto de
dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8,
que es el producto más grande que se puede obtener entre ellos.
"""


def mayor_producto(n1, n2, n3, n4):
    ary = [n1, n2, n3, n4]
    mayor = n1 * n2
    for i in ary:
        for j in ary:
            mayor2 = ary[j] * ary[j+1]
            if mayor2 > mayor:
                mayor = mayor2
            j += 1
            if j == 3:
                break
        i += 1
    return mayor

funcionamos = True
while funcionamos:
    try:
        num1 = int(input("Introduce número 1 : "))
        num2 = int(input("Introduce número 2 : "))
        num3 = int(input("Introduce número 3 : "))
        num4 = int(input("Introduce número 4 : "))
        funcionamos = False
    except ValueError:
        print("Error en la introducción de datos\n")

print("El mayor producto entre ellos es: ",
      mayor_producto(num1, num2, num3, num4))
