# ⦁	Calcula el área de un rectángulo. Pide al usuario que ingrese el largo y el ancho, y luego muestra el área
def calcular_area_rectangulo():
    """
    Pide al usuario que ingrese el largo y el ancho de un rectángulo y luego muestra su área.
    """
    # Pedir al usuario que ingrese el largo
    while True:
        try:
            largo = float(input("Ingresa el largo del rectángulo: "))
            if largo <= 0:
                print("Por favor, ingresa un valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    # Pedir al usuario que ingrese el ancho
    while True:
        try:
            ancho = float(input("Ingresa el ancho del rectángulo: "))
            if ancho <= 0:
                print("Por favor, ingresa un valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

    # Calcular el área
    area = largo * ancho

    # Mostrar el área
    print(f"El área del rectángulo es: {area}")


if __name__ == "__main__":
    calcular_area_rectangulo()