enteros = [3, 4, -3, 7, -2]

def calcular_promedio_positivos(lista: list) -> float:

    suma = 0
    contador = 0

    for i in range(len(enteros)):
        if enteros[i] > 0:
            suma += enteros[i]
            contador += 1

    return suma / contador


print(f"El promedio es: {calcular_promedio_positivos(enteros)}")