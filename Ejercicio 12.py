# Diccionario de factores de conversión relativos a 1 metro
conversiones = {
    'metro': 1.0,
    'centimetro': 100.0,
    'milimetro': 1000.0,
    'kilometro': 0.001,
}

def convertir(cantidad, unidad_origen, unidad_destino):
    """
    Convierte una cantidad entre dos unidades de longitud usando un diccionario.

    Args:
        cantidad (float): La cantidad a convertir.
        unidad_origen (str): La unidad en la que está la cantidad original.
        unidad_destino (str): La unidad a la que se quiere convertir.

    Returns:
        float: El resultado de la conversión, o None si alguna unidad no es válida.
    """
    if unidad_origen in conversiones and unidad_destino in conversiones:
        cantidad_en_metros = cantidad / conversiones[unidad_origen]
        resultado = cantidad_en_metros * conversiones[unidad_destino]
        return resultado
    else:
        print("Error: Una de las unidades no está en el diccionario.")
        return None

resultado = convertir(1000, 'metro', 'kilometro')
if resultado is not None:
    print(f"1000 metros equivalen a {resultado:.4f} kilometros")