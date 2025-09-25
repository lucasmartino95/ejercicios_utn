def mostrar_union(lista_uno: list, lista_dos: list) -> list:

    cantidad = len(lista_uno) + len(lista_dos)

    lista_retorno = [False] * cantidad

    z = 0

    for i in range(len(lista_uno)):
        lista_retorno[z] = lista_uno[i]
        z += 1

    for i in range(len(lista_dos)):
        bandera = False
        for j in range(len(lista_uno)):
            if lista_uno[j] == lista_dos[i]:
                bandera = True
                break
        if bandera == False:
            lista_retorno[z] = lista_dos[i]
            z += 1

    return lista_retorno

print(mostrar_union([1, 2, 3, 4, 5, 10], [4, 5, 7, 8, 9, 10, 11]))