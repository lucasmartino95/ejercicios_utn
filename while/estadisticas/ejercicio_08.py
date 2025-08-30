numero_a = int(input("Ingresa un número: "))
numero_b = int(input("Ingresa un número: "))

if numero_a > numero_b:
    maximo = numero_a
    minimo = numero_b
else:
    maximo = numero_b
    minimo = numero_a

contador = 0

while contador < 8:
    numero_c = int(input("Ingresa un número: "))

    if numero_c > maximo:
        maximo = numero_c

    if numero_c < minimo:
        minimo = numero_c

    contador += 1

if maximo == minimo:
    print(f"El máximo y el mínimo son iguales: {maximo}")
else:
    print(f"El número máximo es: {maximo}\nEl número mínimo es: {minimo}")