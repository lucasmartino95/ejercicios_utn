mi_orden = int(input("Ingresa el orden de la matriz: "))


def crear_matriz(orden: int) -> list:

    mi_matriz = [0] * orden

    for i in range(orden):
        mi_matriz[i] = [0] * orden

    return mi_matriz


def mostrar_matriz(matriz: list) -> bool|None:
    
    if matriz == False:
        print("La matriz no se pudo cargar porque hay números repetidos")
        return False
        
    print("La matriz es:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def cargar_matriz(matriz: list) -> list:

    lista_numeros = []
    repetido = False

    for i in range(len(matriz)):
        print(f"Fila {i}")
        for j in range(len(matriz[i])):
            print(f"Columna {j}")
            matriz[i][j] = int(input("Ingresa un número: "))
            lista_numeros = lista_numeros + [matriz[i][j]]
            while matriz[i][j] < 1: 
                print("Debes ingresar números mayores que 1")
                matriz[i][j] = int(input("Ingresa un número: "))
    
    for i in range(len(lista_numeros)):
        for j in range(i + 1, len(lista_numeros)):
            if lista_numeros[i] == lista_numeros[j]:
                repetido = True
                break

        if repetido:
            break

    if repetido:
        return False

    return matriz


def calcular_constante_magica(matriz: list) -> int:

    constante_magica = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            constante_magica += matriz[i][j]

    constante_magica = constante_magica / len(matriz)

    return constante_magica


# Falta hacer la suma de cada fila, cada columna y las dos diagonales
# principales y ver si son iguales a la constante mágica
def sumar_elementos(matriz: list, constante_magica: int) -> int:
    pass


mi_matriz = crear_matriz(mi_orden)
mi_matriz = cargar_matriz(mi_matriz)
mostrar_matriz(mi_matriz)
constante_magica = calcular_constante_magica(mi_matriz)
sumar_elementos(mi_matriz, constante_magica)