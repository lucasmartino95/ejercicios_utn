def crear_lista(usuario: int, tamaño: int) -> list:

    print(f"Crear lista de compras del usuario {usuario}")

    lista = [False] * tamaño

    for i in range(tamaño):
        lista[i] = input("Ingresa un producto: ")

    return lista