numero_usuario = int(input("Ingresa un número: "))
divisores = 0

for numero in range(1, numero_usuario + 1):
    if numero_usuario % numero == 0:
        divisores += 1

if divisores == 2:
    print("El número es primo")
else:
    print("El número no es primo")
