#Crear una calculadora usando bibliotecas
import math

def calculadora_biblioteca():
  """Calculadora que utiliza la biblioteca math para algunas operaciones."""
  while True:
    print("\nSeleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Potencia")
    print("7. Logaritmo natural")
    print("8. Salir")

    opcion = input("Ingrese el número de la operación deseada: ")

    if opcion in ('1', '2', '3', '4', '5', '6', '7'):
      try:
        if opcion in ('1', '2', '3', '4', '6'):
          num1 = float(input("Ingrese el primer número: "))
          num2 = float(input("Ingrese el segundo número: "))

        elif opcion in ('5', '7'):
          num = float(input("Ingrese el número: "))

        if opcion == '1':
          print("Resultado:", num1 + num2)
        elif opcion == '2':
          print("Resultado:", num1 - num2)
        elif opcion == '3':
          print("Resultado:", num1 * num2)
        elif opcion == '4':
          if num2 == 0:
            print("¡Error! No se puede dividir por cero.")
          else:
            print("Resultado:", num1 / num2)
        elif opcion == '5':
          if num < 0:
            print("¡Error! No se puede calcular la raíz cuadrada de un número negativo.")
          else:
            print("Resultado:", math.sqrt(num))
        elif opcion == '6':
          print("Resultado:", math.pow(num1, num2))
        elif opcion == '7':
          if num <= 0:
            print("¡Error! El logaritmo natural no está definido para números no positivos.")
          else:
            print("Resultado:", math.log(num))

      except ValueError:
        print("Entrada inválida. Por favor, ingrese números.")
    elif opcion == '8':
      print("¡Gracias por usar la calculadora!")
      break
    else:
      print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
  calculadora_biblioteca()