from auxiliares import recortar_lista

def calcular_diferencia(conjunto_1: list,
                        conjunto_2: list) -> list:
    '''
    '''

    diferencia = [False] * len(conjunto_1)

    z = 0

    for i in range(len(conjunto_1)):
        bandera = True

        for j in range(len(conjunto_2)):
            if conjunto_1[i] == conjunto_2[j]:
                bandera = False
                break

        if bandera == True:
            diferencia[z] = conjunto_1[i]
            z += 1
        
    lista_retorno = recortar_lista(diferencia)

    return lista_retorno


mi_lista = [1, 2, 3]

mi_lista_2 = [3, 4, 5]

print(calcular_diferencia(mi_lista, mi_lista_2))

