def comparar_listas(lista_a, lista_b):
    """
    Compara las dos lista y devuelve los elemnetos unicos y que se repiten
    en ambas listas.

    Args:
        lista_a (list): Primera lista.
        lista_b (list): Segunda lista.

    Returns:
        tuple: Una tupla de tres conjuntos:
            - comunes (set): Elementos comunes en las dos listas.
            - unicos_primera (set): Elementos únicos de la primera lista.
            - unicos_segunda (set): Elementos únicos de la segunda lista.
    """
    comunes = set(lista_a) & set(lista_b)
    unicos_primera = set(lista_a) - set(lista_b)
    unicos_segunda = set(lista_b) - set(lista_a)
    return (comunes, unicos_primera, unicos_segunda)

lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]

resultado = comparar_listas(lista_a, lista_b)
print("Comunes:", resultado[0])
print("Unicos en la primera lista:", resultado[1])
print("Unicos en la segunda lista:", resultado[2])