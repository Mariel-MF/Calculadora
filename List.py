def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
entrada = input("Introduce una lista de números separados por comas (por ejemplo, 3,1,4,1,5): ")
numeros = [int(x) for x in entrada.split(',')]
ordenar_burbuja(numeros)
print("\nLista ordenada:")
print(numeros)
