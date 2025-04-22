#Convierte grados Celsius a Fahrenheit. Pide al usuario que ingrese la temperatura en Celsius y muestra el resultado en Fahrenheit.
def celsius_a_fahrenheit(celsius):
  """Convierte grados Celsius a Fahrenheit.

  Args:
    celsius: La temperatura en grados Celsius.

  Returns:
    La temperatura en grados Fahrenheit.
  """
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Solicita al usuario que ingrese la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en Celsius: "))

# Convierte a Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Muestra el resultado
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit")