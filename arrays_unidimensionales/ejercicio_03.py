enteros = [3, 4, 5, 7]

def calcular_promedio(lista: list) -> float:

    suma = 0

    for i in range(len(enteros)):
        suma += enteros[i]

    return suma / len(enteros)


print(f"El promedio es: {calcular_promedio(enteros)}")