def analizar_calificaciones(calificaciones):
    """
    Calcula el promedio, la nota mas alta y la nota mas baja dentro de una lista.

    Args:
        calificaciones (list of float or int): Lista de némeros que representan calificaciones.

    Returns:
        tuple: Devuelve el promedio, la nota mas alta y la nota mas baja.
    """
    promedio = sum(calificaciones) / len(calificaciones)
    nota_maxima = max(calificaciones)
    nota_minima = min(calificaciones)
    return (promedio, nota_maxima, nota_minima)

lista = [1.2, 4.5, 2.8, 3.7, 5.0]

resultado = analizar_calificaciones(lista)
print(f"Promedio: {resultado[0]:.2f}")
print(f"Máxima calificación: {resultado[1]}")
print(f"Mínima calificación: {resultado[2]}")
