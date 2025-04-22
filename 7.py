#Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero.
def determinar_signo():
  """Pide un número al usuario y determina si es positivo, negativo o cero."""
  try:
    numero = float(input("Ingrese un número: "))
    if numero > 0:
      print("El número es positivo.")
    elif numero < 0:
      print("El número es negativo.")
    else:
      print("El número es cero.")
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
  determinar_signo()