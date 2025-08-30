bandera = True
suma = 0
contador = 0

while bandera:
    numero = int(input("Ingresa un número: "))
    pregunta = input("¿Quieres seguir ingresando números? (Sí/No): ")

    if pregunta == "No":
        bandera = False

    suma += numero
    contador += 1

print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio es: {suma / contador}")