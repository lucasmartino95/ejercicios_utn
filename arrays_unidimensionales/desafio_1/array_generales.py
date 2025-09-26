from especificas import *

def sumar_numeros_pares(lista_numeros_pares: list) -> None:

    suma = 0

    for i in range(len(lista_numeros_pares)):
        if (determinar_numero_par(lista_numeros_pares[i])):
            suma += lista_numeros_pares[i]
    
    print(f"La suma de los números pares es: {suma}")


def mostrar_cantidad_positivos_y_negativos(mi_lista: list) -> None:

    cantidad_positivos = 0
    
    cantidad_negativos = 0

    for i in range(len(mi_lista)):
        if determinar_positivo(mi_lista[i]):
            cantidad_positivos += 1
        elif determinar_negativo(mi_lista[i]):
            cantidad_negativos += 1

    print(f"Cantidad de números positivos ingresados: {cantidad_positivos}")
    print(f"Cantidad de números negativos ingresados: {cantidad_negativos}")


def mostrar_mayor_numero_impar(mi_lista: list) -> None:

    primer_numero_impar = 0

    for i in range(len(mi_lista)):
        if determinar_numero_par(mi_lista[i]) == False:

            primer_numero_impar += 1

            if primer_numero_impar == 1:
                numero_impar_maximo = mi_lista[i]
            elif mi_lista[i] > numero_impar_maximo:
                numero_impar_maximo = mi_lista[i]

    if primer_numero_impar == 0:
        numero_impar_maximo = "No ingresaste ningún número impar"

    print(f"El mayor número impar ingresado es: {numero_impar_maximo}")


def mostrar_numeros_ingresados(mi_lista: list) -> None:

    lista = [False] * len(mi_lista)

    for i in range(len(lista)):
        lista[i] = mi_lista[i]

    print(f"Los números ingresados son: {lista}")


def mostrar_solo_numeros_pares(mi_lista: list) -> None:

    tamaño = 0
    z = 0

    for i in range(len(mi_lista)):
        if determinar_numero_par(mi_lista[i]):
            tamaño += 1
    
    lista_retorno = [False] * tamaño

    for i in range(len(mi_lista)):
        if determinar_numero_par(mi_lista[i]):
            lista_retorno[z] = mi_lista[i]
            z += 1


    print(f"Los números pares ingresados son: {lista_retorno}")


def mostrar_numeros_en_posiciones_impares(mi_lista: list) -> None:

    tamaño = 0

    z = 0

    for i in range(len(mi_lista)):
        if (i % 2) != 0:
            tamaño += 1

    lista_retorno = [False] * tamaño

    for i in range(len(mi_lista)):
        if (i % 2) != 0:
            lista_retorno[z] = mi_lista[i]
            z += 1

    print(f"Los números en posiciones impares son: {lista_retorno}")