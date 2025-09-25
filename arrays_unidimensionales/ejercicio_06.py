mi_lista = [4, 5, 3, 10, 7, 1, -5, -3, 0]

def encontrar_maximo(lista: list) -> int:
    for i in range(len(lista)):
        if i == 0:
            maximo = lista[i]
        if maximo < lista[i]:
            maximo = lista[i]
    return maximo

print(encontrar_maximo(mi_lista))