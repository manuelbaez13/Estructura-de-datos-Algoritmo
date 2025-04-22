#Crear una calculadora usando funciones
def sumar(num1, num2):
  """Devuelve la suma de dos números."""
  return num1 + num2

def restar(num1, num2):
  """Devuelve la resta de dos números."""
  return num1 - num2

def multiplicar(num1, num2):
  """Devuelve la multiplicación de dos números."""
  return num1 * num2

def dividir(num1, num2):
  """Devuelve la división de dos números. Maneja la división por cero."""
  if num2 == 0:
    return "¡Error! No se puede dividir por cero."
  else:
    return num1 / num2

def calculadora():
  """Función principal de la calculadora."""
  while True:
    print("\nSeleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación deseada: ")

    if opcion in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
          print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
          print("Resultado:", restar(num1, num2))
        elif opcion == '3':
          print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
          print("Resultado:", dividir(num1, num2))
      except ValueError:
        print("Entrada inválida. Por favor, ingrese números.")
    elif opcion == '5':
      print("¡Gracias por usar la calculadora!")
      break
    else:
      print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
  calculadora()