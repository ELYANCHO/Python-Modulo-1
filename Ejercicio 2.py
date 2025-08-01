def Edad_usuario (Edad):
    """
   Esta función toma la edad del usuario.

   Args:
       Edad (int): El primer valor.

   Returns:
       int: Edad del usuario.
       """
    return  Edad

Edad = int(input("Ingrese su edad: "))

result = Edad_usuario(Edad)

if result < 18 :
    print(f"Su edad es: {result} Es menor de edad")
elif result >= 18 and result <= 25  :
    print(f"Su edad es: {result} Es un joven adulto")
else:
    print(f"Su edad es: {result} Es mayor de edad")

