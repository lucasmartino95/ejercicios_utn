mi_matriz = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]


def mostrar_matriz(matriz: list) -> None:

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def calcular_constante_magica(matriz: list) -> int:

    n = len(matriz)
    n = (n * ((n ** 2) + 1)) / 2
    return n


constante_magica = calcular_constante_magica(mi_matriz)
print(constante_magica)
