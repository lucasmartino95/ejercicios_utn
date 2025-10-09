mi_orden = int(input("Ingresa el orden de la matriz: "))


def crear_matriz(orden: int) -> list:

    mi_matriz = [[0] * orden] * orden 

    return mi_matriz


def mostrar_matriz(matriz: list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()



mi_matriz = crear_matriz(mi_orden)
mostrar_matriz(mi_matriz)