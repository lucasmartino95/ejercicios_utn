bandera = True
suma_negativos = 0
suma_positivos = 0
cantidad_negativos_ingresados = 0
iteracion = 0
total_numeros_ingresados = 0
cantidad_positivos_ingresados = 0

while bandera:
    numero = int(input("Ingresa un número (para terminar, ingresa 0): "))

    if numero != 0:
        if numero < 0:
            cantidad_negativos_ingresados += 1
            suma_negativos += numero
        else:
            if iteracion == 0:
                maximo = numero
            if numero > maximo:
                maximo = numero
            cantidad_positivos_ingresados += 1
            suma_positivos += numero
        total_numeros_ingresados = cantidad_negativos_ingresados + cantidad_positivos_ingresados
    else:
        bandera = False

    iteracion += 1


print()
print(f"La suma acumulada de números negativos es: {suma_negativos}")
print(f"La suma acumulada de números positivos es: {suma_positivos}")
print(f"La cantidad de números negativos ingresados es: {cantidad_negativos_ingresados}")

if cantidad_negativos_ingresados != 0:
    print(f"El promedio de los números negativos es: {suma_negativos/cantidad_negativos_ingresados}")
else:
    print("No hay promedio de números negativos")

if cantidad_positivos_ingresados != 0:
    print(f"El número positivo ingresado más grande es: {maximo}")
else:
    print("No ingresaste ningún número positivo")

if cantidad_negativos_ingresados != 0:
    print(f"El porcentaje de números negativos ingresados es: {cantidad_negativos_ingresados * 100 / total_numeros_ingresados}%")
else:
    print("No hay porcentaje de números negativos ingresados")
print()
        