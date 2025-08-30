bandera = True
suma = 0
producto = 1

while bandera:
    numero = int(input("Ingresa un número: "))
    pregunta = input("¿Quieres ingresar otro número? (Sí/No): ")

    if pregunta == "No":
        bandera = False

    if numero >= 0:
        suma += numero
    else:
        producto *= numero

print(f"La suma de los número positivos ingresados es: {suma}")

if producto == 1:
    producto = 0

print(f"El producto de los números negativos ingresados es: {producto}")
