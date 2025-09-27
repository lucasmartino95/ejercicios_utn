def crear_lista(usuario: int, tamaño: int) -> list:

    print(f"Crear lista de compras del usuario {usuario}")

    lista = [False] * tamaño

    for i in range(tamaño):
        lista[i] = input("Ingresa un producto: ")

    return lista


def comparar_productos(lista_1: list, lista_2: list) -> None:

    tamaño = 0

    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                tamaño += 1

    lista_retorno = [False] * tamaño
    z = 0

    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                lista_retorno[z] = lista_1[i]
                z += 1

    if len(lista_retorno) == 0:
        print("No hay productos en común")
    else:
        print(f"Ambos usuarios compraron: {lista_retorno}")


def comparar_productos_exclusivos(lista_1: list, lista_2: list) -> None:

    print("Productos exclusivos que compró el usuario 1:")
    
    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] != lista_2[j]:
                producto_exclusivo = True
            else:
                producto_exclusivo = False
                break
        
        if producto_exclusivo == True:
            print(lista_1[i])


    print("Productos exclusivos que compró el usuario 2:")

    for i in range(len(lista_2)):
        for j in range(len(lista_1)):
            if lista_2[i] != lista_1[j]:
                producto_exclusivo = True
            else:
                producto_exclusivo = False
                break
        
        if producto_exclusivo == True:
            print(lista_2[i])


def mostrar_catalogo_total(lista_1: list,
                            lista_2: list) -> None:
    
    tamaño = 0

    for i in range(len(lista_1)):
        tamaño += 1

    for j in range(len(lista_2)):
        tamaño += 1

    lista_retorno = [False] * tamaño

    z = 0

    for i in range(len(lista_1)):
        lista_retorno[z] = lista_1[i]
        z += 1
    
    for j in range(len(lista_2)):
        lista_retorno[z] = lista_2[j]
        z += 1

    print("El catálogo total es:")
    print(lista_retorno)


def dar_recomendaciones(lista_1: list, lista_2: list) -> None:

    print("Recomendación de compras para el usuario 1:")

    for i in range(len(lista_2)):
        for j in range(len(lista_1)):
            if lista_2[i] != lista_1[j]:
                producto_exclusivo = True
            else:
                producto_exclusivo = False
                break
        
        if producto_exclusivo:
            print(lista_2[i])

    print("Recomendación de compras para el usuario 2:")

    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] != lista_2[j]:
                producto_exclusivo = True
            else:
                producto_exclusivo = False
                break
        
        if producto_exclusivo:
            print(lista_1[i])

