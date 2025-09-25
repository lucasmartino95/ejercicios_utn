mi_lista = [3, 4, 5]

def calcular_producto(lista: list) -> int:

    resultado = 1

    for i in range(len(lista)):
        resultado *= lista[i]

    return resultado


print(f"El producto de los números es: {calcular_producto(mi_lista)}")