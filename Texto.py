def leer_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        return "Error: El archivo no existe. Por favor, verifica la ruta."
    except IOError:
        return "Error: Ocurrió un problema al intentar leer el archivo."
ruta = input("Introduce la ruta del archivo de texto que deseas leer: ")
resultado = leer_archivo(ruta)
print("\nContenido del archivo:")
print(resultado)
