def tabla_de_multiplicar(numero):
  """
  Genera la tabla de multiplicar para un número dado.

  Args:
    numero: El número del cual se generará la tabla.
  """
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número para generar la tabla de multiplicar: "))

tabla_de_multiplicar(numero)