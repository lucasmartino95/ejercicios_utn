numero_usuario = int(input("Ingresa un número: "))
limite = numero_usuario + 1
numeros_primos = 0

print("Números primos:")

for numero in range(2, limite):
    divisores = 0
    for numero_dos in range(1, numero + 1):
        if numero % numero_dos == 0:
            divisores += 1
    if divisores == 2:
        numeros_primos += 1
        print(numero)

print(f"Cantidad de números primos: {numeros_primos}")
