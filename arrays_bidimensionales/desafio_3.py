filas = int(input("Ingresa cantidad de filas: "))
columnas = int(input("Ingresa cantidad de columnas: "))


def crear_matriz(filas: int, columnas: int) -> list:
    
    mi_matriz = [0] * filas

    for i in range(filas):
        filas = [0] * columnas
        mi_matriz[i] = filas

    return mi_matriz


def cargar_matriz(matriz: list) -> None: 

    for i in range(len(matriz)):
        print(f"Fila {i}")
        for j in range(len(matriz[i])):
            print(f"Columna {j}")
            numero = int(input("Ingresa un número entero: "))
            matriz[i][j] = numero


def mostrar_matriz(matriz: list) -> None:

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def verificar_secuencia_numeros_pares(mi_matriz: list) -> None:
    
    contador = 0

    for i in range(len(mi_matriz)):
        longitud_secuencia = 0
        for j in range(len(mi_matriz[i])):
            if matriz[i][j] % 2 == 0:
                longitud_secuencia += 1
            else:
                if longitud_secuencia >= 2:
                    contador += 1
                longitud_secuencia = 0
        if longitud_secuencia >= 2:
            contador += 1
            
    if contador > 0:
        print("EXISTEN NÚMEROS CONSECUTIVOS PARES")
    else:
        print("NO EXISTEN NÚMEROS CONSECUTIVOS PARES")

    print(f"Cantidad de secuencias de números pares: {contador}")


def determinar_secuencia_mas_corta(mi_matriz: list) -> None:
    pass

matriz = crear_matriz(filas, columnas)
cargar_matriz(matriz)
mostrar_matriz(matriz)
verificar_secuencia_numeros_pares(matriz)