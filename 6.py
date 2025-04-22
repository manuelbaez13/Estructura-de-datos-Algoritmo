def calculadora_basica():
  """Pide dos números al usuario y muestra las operaciones básicas."""
  try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 == 0:
      division = "No se puede dividir por cero."
    else:
      division = num1 / num2

    print(f"\nLa suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    print(f"La división de {num1} entre {num2} es: {division}")

  except ValueError:
    print("Entrada inválida. Por favor, ingrese números.")

if __name__ == "__main__":
  calculadora_basica()