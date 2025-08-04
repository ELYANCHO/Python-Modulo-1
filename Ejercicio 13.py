def agregar_producto(inventario):
    """
    Agrega un nuevo producto al inventario.

    Args:
        inventario (list): Lista de productos representados como diccionarios.
    """
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad disponible: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado correctamente.\n")


def realizar_venta(inventario):
    """
    Realiza la venta de un producto y actualiza su cantidad.

    Args:
        inventario (list): Lista de productos representados como diccionarios.
    """
    nombre = input("Nombre del producto a vender: ").strip()
    cantidad_vendida = int(input("Cantidad a vender: "))

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                total = producto["precio"] * cantidad_vendida
                print(f"Venta realizada. Total: ${total:.2f}\n")
                return
            else:
                print("No hay suficiente stock para realizar la venta.\n")
                return
    print("Producto no encontrado en el inventario.\n")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos disponibles en el inventario.

    Args:
        inventario (list): Lista de productos representados como diccionarios.
    """
    if not inventario:
        print("Inventario vacío.\n")
        return

    print("Inventario de productos:")
    for producto in inventario:
        print(f"• {producto['nombre']} - ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
    print()


def sistema_inventario():
    """
    Sistema interactivo para gestionar el inventario de una tienda.

    Permite al usuario agregar productos, realizar ventas y visualizar el inventario.

    No recibe parámetros de entrada.
    """
    inventario = []

    while True:
        print("\nMENÚ DEL INVENTARIO")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción 1-4: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            realizar_venta(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("hasta luego")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

sistema_inventario()
