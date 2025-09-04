numero_usuario = int(input("Ingresa un número: "))
limite = numero_usuario + 1
numeros_primos = 0
bandera = True

while bandera:
    if numero_usuario > 1:
        print("Números primos: ")
        for numero in range(1, limite):
            divisores = 0
            for numero_dos in range(1, numero + 1):
                if numero % numero_dos == 0:
                    divisores += 1
            if divisores == 2:
                numeros_primos += 1
                print(numero)
        bandera = False
    elif numero_usuario == 1:
        print("El 1 no es un número primo")
        bandera = False
    else:
        print("No ingresaste un número mayor a 1")
        bandera = False

print(f"Cantidad de números primos: {numeros_primos}")
