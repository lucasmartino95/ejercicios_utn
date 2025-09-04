numero_usuario = int(input("Ingresa un número: "))
divisores = 0

for numero in range(1, numero_usuario + 1):

    if numero_usuario % numero == 0:
        print(numero)
        divisores += 1
    

print(f"Cantidad de divisores encontrados: {divisores}")
