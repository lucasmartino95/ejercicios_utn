def crear_array(tamaño: int) -> list:

    lista = [False] * tamaño

    for i in range(tamaño):
        lista[i] = int(input("Ingresa un número: "))

    return lista
