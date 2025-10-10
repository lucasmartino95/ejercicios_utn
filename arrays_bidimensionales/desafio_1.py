mi_orden = int(input("Ingresa el orden de la matriz: "))


def crear_matriz(orden: int) -> list:

    mi_matriz = [0] * orden

    for i in range(orden):
        mi_matriz[i] = [0] * orden

    return mi_matriz


def mostrar_matriz(matriz: list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def cargar_matriz(matriz: list) -> list:

    for i in range(len(matriz)):
        print(f"Fila {i}")
        for j in range(len(matriz[i])):
            print(f"Columna {j}")
            matriz[i][j] = int(input("Ingresa un número: "))
            # Falta comprobar que los números no se repitan
            while matriz[i][j] < 1: 
                print("Debes ingresar números mayores que 1")
                matriz[i][j] = int(input("Ingresa un número: "))

    return matriz


mi_matriz = crear_matriz(mi_orden)
mi_matriz = cargar_matriz(mi_matriz)
mostrar_matriz(mi_matriz)