suma = 0

for numero in range(10):
    numero_usuario = int(input("Ingresa un número (0 para terminar): "))
    if numero_usuario == 0:
        break
    suma += numero_usuario

if numero == 9:
    numero += 1
    
print(f"La suma de los numeros es: {suma}")

if numero == 0:
    print("No hay promedio porque no se puede dividir por cero")
else:
    print(f"El promedio es: {suma / numero}")