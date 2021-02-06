leyendo = True

while leyendo:
    numero_amigos = input("Cuántos amigos tienes")
    try:
        numero_amigos = int(numero_amigos)
        if numero_amigos == 0:
            print("¿0 amigos? ¿Qué pringao no?")
            leyendo = True
        else:
            leyendo = False
    except ValueError:
        print(numero_amigos, "no es un número, prueba de nuevo")

for n in range(numero_amigos):
    nombre = input("Introduce el nombre de tu amigo")
    print("Hola", nombre)