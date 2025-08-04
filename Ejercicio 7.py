def gestionar_lista_compras():
    """
    Permite al usuario administrar una lista mediante un menú de opciones,
    dentro de las cuales está agregar,eliminar, visualizar la lista y salir del menú
    Returns:
        None: La función no retorna nada, pero interactúa con el usuario a través de la consola.
    """

    lista_compras = []

    while True:
        print("\nMENÚ DE OPCIONES")
        print("1. Agregar producto a la lista")
        print("2. Eliminar producto de la lista")
        print("3. Ver la lista completa")
        print("4. Salir")

        opcion = input("Elige una opción 1-4: ")

        if opcion == "1":
            item = input("Escriba el producto que desea agregar: ")
            lista_compras.append(item)
            print(f"'{item}' ha sido agregado a la lista.")

        elif opcion == "2":
            item = input("Escribe el producto que desea eliminar: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"'{item}' ha sido eliminado de la lista.")
            else:
                print(f"'{item}' no está en la lista.")

        elif opcion == "3":
            if lista_compras:
                print("\nLa lista de compras contiene:")
                for i, producto in enumerate(lista_compras, start=1):
                    print(f"{i}. {producto}")
            else:
                print("La lista está vacía.")

        elif opcion == "4":
            print("HASTA LUEGO!")
            break

        else:
            print("Opción no válida. Intenta con un número del 1 al 4.")

gestionar_lista_compras()
