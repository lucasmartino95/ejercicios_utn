mi_matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8]]


def validar_matriz(mi_matriz: list) -> bool:

    numero = 0

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
    print("La matriz creada es: ")
    mostrar_matriz(mi_matriz)
else:
    print("La matriz ingresada no es válida")