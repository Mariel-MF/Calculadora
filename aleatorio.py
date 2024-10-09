import random
def crear_lista_aleatoria(tamano, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(tamano)]
tamano = int(input("Introduce la cantidad de números en la lista: "))
rango_min = int(input("Introduce el valor mínimo del rango: "))
rango_max = int(input("Introduce el valor máximo del rango: "))
lista_aleatoria = crear_lista_aleatoria(tamano, rango_min, rango_max)
print("\nLista de números aleatorios:")
print(lista_aleatoria)
