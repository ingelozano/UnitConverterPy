def convertir_temperatura():
    try:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))

        # Conversiones
        fahrenheit = (celsius * 9/5) + 32  # Conversión a grados Fahrenheit
        kelvin = celsius + 273.15  # Conversión a Kelvin
        rankine = (celsius * 9/5) + 491.67  # Conversión a grados Rankine

        print(f"{celsius:.2f} grados Celsius equivalen a:")
        print(f"{fahrenheit:.2f} grados Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
        print(f"{rankine:.2f} grados Rankine")
    except ValueError:
        print("Por favor, ingresa una temperatura válida.")

def convertir_longitud():
    try:
        metros = float(input("Ingresa la longitud en metros: "))

        # Conversiones
        pulgadas = metros * 39.37  # Conversión a pulgadas
        pies = metros * 3.281  # Conversión a pies
        yardas = metros * 1.094  # Conversión a yardas
        millas = metros / 1609.34  # Conversión a millas

        print(f"{metros:.2f} metros equivalen a:")
        print(f"{pulgadas:.2f} pulgadas")
        print(f"{pies:.2f} pies")
        print(f"{yardas:.2f} yardas")
        print(f"{millas:.5f} millas")
    except ValueError:
        print("Por favor, ingresa una longitud válida.")

def convertir_peso():
    try:
        kilogramos = float(input("Ingresa el peso en kilogramos: "))

        # Conversiones
        gramos = kilogramos * 1000  # Conversión a gramos
        libras = kilogramos * 2.205  # Conversión a libras
        onzas = kilogramos * 35.274  # Conversión a onzas
        toneladas = kilogramos / 1000  # Conversión a toneladas

        print(f"{kilogramos:.2f} kilogramos equivalen a:")
        print(f"{gramos:.2f} gramos")
        print(f"{libras:.2f} libras")
        print(f"{onzas:.2f} onzas")
        print(f"{toneladas:.3f} toneladas")
    except ValueError:
        print("Por favor, ingresa un peso válido.")

if __name__ == "__main__":
    print("¡Bienvenido al Conversor de Unidades!")

    while True:
        print("\nSelecciona la opción de conversión:")
        print("1. Temperatura")
        print("2. Longitud")
        print("3. Peso")
        print("4. Salir")

        try:
            opcion = int(input("Ingresa el número de opción: "))
        except ValueError:
            print("Por favor, ingresa una opción válida.")
            continue

        if opcion == 1:
            convertir_temperatura()
        elif opcion == 2:
            convertir_longitud()
        elif opcion == 3:
            convertir_peso()
        elif opcion == 4:
            print("¡Gracias por usar el Conversor de Unidades! ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
