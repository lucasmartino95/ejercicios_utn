numero_usuario = int(input("Ingresa un número: "))
limite = numero_usuario + 1
cadena = ""

for numero in range(1, limite):
    cadena += str(numero)
    print(cadena)