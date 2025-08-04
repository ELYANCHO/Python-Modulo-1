def agenda_contactos():
    """
    Esta funcion simula una agenda de contactos
    que permite agregar, buscar y mostrar contactos.

    No recibe parámetros de entrada.
    Retorna:
        dict: El diccionario completo de contactos al finalizar.
    """
    agenda = {}

    def agregar_contacto(nombre, telefono):
        agenda[nombre] = telefono
        print(f"Contacto '{nombre}' agregado exitosamente.")

    def buscar_contacto(nombre):
        if nombre in agenda:
            print(f"Teléfono de '{nombre}': {agenda[nombre]}")
        else:
            print(f"'{nombre}' no está en la agenda.")

    def mostrar_contactos():
        if agenda:
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            print("Agenda vacía.")

    while True:
        print("\nAGENDA")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")

        opcion = input("Selecciona una opción 1-4: ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agregar_contacto(nombre, telefono)
        elif opcion == "2":
            nombre = input("Nombre del contacto a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            print("VUELVE PRONTO")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

    return agenda

agenda = agenda_contactos()
