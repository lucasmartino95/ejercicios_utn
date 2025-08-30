pregunta = int(input("¿Cuántos números quieres ingresar? (5 a 10): "))
contador = 0
suma = 0

print(f"Vas a ingresar {pregunta} números")

while contador < pregunta:
    numero = int(input("Ingresa un número: "))
    suma += numero
    contador += 1

print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio es: {suma/contador}")