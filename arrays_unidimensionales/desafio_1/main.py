from array_generales import *

mi_lista = [False] * 10

for i in range(10):

    numero = int(input("Ingresa un número (entre -1000 y 1000): "))

    while numero < -1000 or numero > 1000:
        print("El número que ingresaste no está dentro del rango")
        numero = int(input("Ingresa un número (entre -1000 y 1000): "))
    
    mi_lista[i] = numero

mostrar_cantidad_positivos_y_negativos(mi_lista)
sumar_numeros_pares(mi_lista)
mostrar_mayor_numero_impar(mi_lista)
mostrar_numeros_ingresados(mi_lista)
mostrar_solo_numeros_pares(mi_lista)
mostrar_numeros_en_posiciones_impares(mi_lista)