def mostrar_interseccion(lista_uno: list, lista_dos: list) -> list:

    if len(lista_uno) > len(lista_dos):
        cantidad_elementos = len(lista_dos)
    else:
        cantidad_elementos = len(lista_uno)

    interseccion = [False] * cantidad_elementos

    z = 0

    for i in range(len(lista_uno)):
        for j in range(len(lista_dos)):
            if lista_uno[i] == lista_dos[j]:
                interseccion[z] = lista_uno[i]
                z += 1
    
    return interseccion


mostrar_interseccion([1, 2, 3, 4, 5], [1, 2, 4, 5])
