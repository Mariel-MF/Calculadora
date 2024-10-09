import random
opciones = ["piedra", "papel", "tijera"]
def jugar_ronda():
    usuario = input("Elige piedra, papel o tijera: ").lower()
    computadora = random.choice(opciones)
    print(f"Computadora eligió: {computadora}")
    if usuario == computadora:
        print("Es un empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("Ganaste!")
    elif usuario in opciones:
        print("Perdiste, la computadora ganó JEJEJEJ")
    else:
        print("Opción no válida. Inténtalo de nuevo")
jugando = True
while jugando:
    jugar_ronda()
    jugar_otra = input("¿Quieres jugar otra ronda? (s/n): ").lower()
    if jugar_otra != 's':
        jugando = False
print("Gracias por jugar")
