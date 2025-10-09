mi_lista = [5, 3, 4, 2, 8]


def ordenar_array(lista: list, ordenar_descendente: bool = False) -> None:

    tamaño_lista = len(lista)

    if ordenar_descendente == False:
        for i in range(tamaño_lista - 1):
            for j in range(tamaño_lista - 1 - i):
                if lista[j] > lista[j + 1]:
                    temp = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temp

    else:
        for i in range(tamaño_lista - 1):
           for j in range(tamaño_lista - 1 - i):
                if lista[j] < lista[j + 1]:
                    temp = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temp

    print(mi_lista)


ordenar_array(mi_lista, True)