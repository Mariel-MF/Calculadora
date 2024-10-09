import random
def lanzar_moneda():
    resultado = random.choice(['Cara', 'Cruz'])
    return resultado
resultado = lanzar_moneda()
print(f"\nResultado del lanzamiento de la moneda: {resultado}")
