def palindromo(frase):
    """
    Prubea si la palabra es un palindromo
    Se ignoran espacios, mayusculas y minusulas.

    Args:
        frase (str): Palabra que inserta el usuario.

    Returns:
        str: Mensaje de confirmacion (Si/No, es un palindromo).
    """
    nuevo = frase.replace(" ", "").lower()
    respuesta = ""

    if nuevo == nuevo[::-1]:
        respuesta = "Si es un palíndromo"
    else:
        respuesta = "No es un palíndromo"

    return respuesta

frase = input("Por favor ingrese una palabra o frase: ")
#Isaac no ronca asi
resultado = palindromo(frase)
print(f"{frase} : {resultado}")
