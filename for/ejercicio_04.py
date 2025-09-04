numero_usuario = int(input("Ingresa un número: "))

for numero in range(numero_usuario + 1):
    resultado = numero_usuario * numero
    print(f"{numero_usuario} x {numero} = {resultado}")