def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero."
    else:
        return x / y
def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
while True:
    mostrar_menu()
    opcion = input("Introduce el número de la operación (1/2/3/4) o 'q' para salir: ")
    if opcion == 'q':
        print("Gracias por usar la calculadora")
        break
    if opcion not in ['1', '2', '3', '4']:
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
        continue
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Por favor, introduce números válidos.")
        continue
    if opcion == '1':
        print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
    elif opcion == '4':
        resultado = division(num1, num2)
        print(f"Resultado: {num1} / {num2} = {resultado}")
    repetir = input("¿Quieres hacer otra operación? (s/n): ")
    if repetir.lower() != 's':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
