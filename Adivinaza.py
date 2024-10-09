import random
num_sec = random.randint(1, 100)
adivinado = False
print("Holi bienvenido al juego de adivinanzas")
print("Estoy pensando en un número entre 1 y 100, adivina cual es")
while not adivinado:
    intento = int(input("Introduce el numero que creeas que es: "))
    if intento < num_sec:
        print("Uyyy ese no ese, es mas alto")
    elif intento > num_sec:
        print("Uyyy ese tampoco, es mas bajo")
    else:
        print("Correctooo, ese si es el numero que estaba pensando", num_sec)
        adivinado = True
