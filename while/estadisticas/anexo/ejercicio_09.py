contador = 0
suma = 0

while contador < 5:
    numero = int(input("Ingresa un número: "))

    suma += numero
    contador += 1

print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio es: {suma/contador}")