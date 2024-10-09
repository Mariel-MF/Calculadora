def buscar_elemento(lista, elemento):
    for indice, valor in enumerate(lista):
        if valor == elemento:
            return indice
    return -1
entrada = input("Introduce una lista de números separados por comas (por ejemplo, 3,1,4,1,5): ")
numeros = [int(x) for x in entrada.split(',')]
elemento = int(input("Introduce el número que deseas buscar: "))
posicion = buscar_elemento(numeros, elemento)
if posicion != -1:
    print(f"\nEl número {elemento} se encuentra en la posición {posicion}.")
else:
    print(f"\nEl número {elemento} no se encuentra en la lista.")

