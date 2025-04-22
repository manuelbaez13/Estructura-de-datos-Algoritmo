#Escribe un programa que pida al usuario un número y determine si es par o impar.
def determinar_par_impar():
  """Pide un número al usuario y determina si es par o impar."""
  try:
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
      print(f"El número {numero} es par.")
    else:
      print(f"El número {numero} es impar.")
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
  determinar_par_impar()