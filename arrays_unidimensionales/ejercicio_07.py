mi_lista = [4, 5, 3, 10, 7, 1, -5, -3, 0]

def encontrar_posicion_maximo(lista: list) -> None:

    indice = 0

    for i in range(len(lista)):
        if i == 0:
            maximo = lista[i]
        if maximo < lista[i]:
            maximo = lista[i]
            indice = i

    print(f"La posición donde se encuentra el número más grande es: {indice}")

encontrar_posicion_maximo(mi_lista)