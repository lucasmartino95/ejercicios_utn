def mostrar_union(lista_uno: list, lista_dos: list) -> list:

    tamaño_lista = len(lista_uno) + len(lista_dos)

    for i in range(len(lista_uno)):
        for j in range(len(lista_dos)):
            if lista_uno[i] == lista_dos[j]:
                tamaño_lista -= 1

    union = [False] * tamaño_lista

    print(union)

mostrar_union([1, 2, 3, 4, 5, 10], [4, 5, 7, 8, 9, 10, 11])
