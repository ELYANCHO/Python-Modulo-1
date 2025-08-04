def frecuencia_palabras(texto):
    """
    Calcula la frecuencia de cada palabra en un texto dado por el usuario.
    -Covierte el texto a minúsculas y lo divide en palabras,
    -Cuenta cuántas veces aparece cada una utilizando un diccionario.
   
    Args:
    texto (str): Texto que se desea analizar.

    Retorna:
        dict: Diccionario con las palabras como claves y su frecuencia como valores.
    """
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


texto = input("Por favor ingrese un texto: ")
resultado = frecuencia_palabras(texto)

print("\nFrecuencia de palabras:")
for palabra, cantidad in resultado.items():
    print(f"'{palabra}': {cantidad}")
