mi_matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8]]


def validar_matriz(mi_matriz: list) -> bool:

    numero_anterior = 0

    for i in range(len(mi_matriz)):
        for j in range(len(mi_matriz[i])):
            if mi_matriz[i][j] >= 1:
                continue
            else:
                print("Los valores deben ser mayor o igual que 1")
                return False
        
    return True


matriz_validada = validar_matriz(mi_matriz)


def mostrar_matriz(mi_matriz: list) -> None:
    for i in range(len(mi_matriz)):
        for j in range(len(mi_matriz[i])):
            print(mi_matriz[i][j], end=" ")
        print()


if matriz_validada:
    mostrar_matriz(mi_matriz)
else:
    print("La matriz ingresada no es válida")


def calcular_constante_magica(mi_matriz: list) -> bool:

    suma_fila = 0

    for i in range(len(mi_matriz)):
        for j in range(len(mi_matriz[i])):
            print(mi_matriz[i][j])
            suma_fila += mi_matriz[i][j]



calcular_constante_magica(mi_matriz)