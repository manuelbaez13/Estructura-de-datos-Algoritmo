#Escribe un programa que sume números ingresados por el usuario hasta que ingrese 0.
def sumar_hasta_cero():
  """Suma números ingresados por el usuario hasta que ingrese 0."""
  suma = 0
  while True:
    try:
      numero = float(input("Ingrese un número (ingrese 0 para terminar): "))
      suma += numero
      if numero == 0:
        break
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número.")
  print(f"La suma total es: {suma}")

if __name__ == "__main__":
  sumar_hasta_cero()
