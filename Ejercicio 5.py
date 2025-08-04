def jugar_adivinanza():
    """
    Dentro de la función se captura el número que ingresa el usuario y lo compara con el número secreto
    
    Returns:
        str: Muestra un mensaje cuando el usuario adivina el número secreto.
    """

    numero_secreto = 42
    adivinanza = None
    mensaje_final = "Adivinaste el número secreto"

    print("Adivina el número secreto entre 1 y 100.")

    while adivinanza != numero_secreto:
        try:
            adivinanza = int(input("Ingresa tu número: "))
            #La función recibe adivinanza como argumento, 
            #pero como se desea que el usuario tenga varios intentos,
            #lo mejor es dejar la entrada dentro del ciclo.
            if adivinanza < numero_secreto:
                print("Muy bajo. Intenta nuevamente.")
            elif adivinanza > numero_secreto:
                print("Muy alto. Intenta nuevamente.")
            else:
                print(mensaje_final)
                
                return mensaje_final

        except ValueError:
            print("solo se pueden ingresar números enteros. Inténtalo de nuevo.")

resultado = jugar_adivinanza()
print(f"!FELICIDADES! {resultado}")
