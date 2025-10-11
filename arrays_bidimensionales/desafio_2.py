lista_legajos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

lineas = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def desplegar_menu_de_opciones() -> int:

    print("Menú de opciones")
    print("[1] Cargar planilla de recaudación ")
    print("[2] Mostrar la recaudación de cada coche y línea ")
    print("[3] Calcular y mostrar la recaudación por cada línea ")
    print("[4] Calcular y mostrar la recaudación por coche ")
    print("[5] Calcular y mostrar la recaudación total ")
    print("[6] Salir del programa ")
    eleccion_usuario = int(input("Elige lo que quieres hacer: "))

    return eleccion_usuario


def verificar_numero_legajo(n_legajo: int,
                    lista: list) -> None:
    
    for i in range(len(lista)):
        if n_legajo == lista[i]:
            return True
        
    return False
    

def cargar_planilla_de_recaudacion(indice_linea: int,
                                   indice_coche: int,
                                   recaudacion: int,
                                   lineas: list) -> None:
    
    if indice_linea <= len(lineas) and indice_coche <= len(lineas[indice_linea]):
        if recaudacion > 0:
            lineas[indice_linea][indice_coche] += recaudacion
        else:
            print("No se permite ingresar valores negativos en la recaudación")


def mostrar_recaudacion(lineas: list) -> None:

    for i in range(len(lineas)):
        print(f"Línea {i}")
        print(lineas[i])


def mostrar_recaudacion_linea(lista: list, n_linea: int):

    suma = 0

    for i in range(len(lista[n_linea])):
        suma += lista[n_linea][i]

    print(f"La recaudación de la línea {n_linea} es: ${suma}")


def mostrar_recaudacion_coche(lista: list, n_linea: int, n_coche: int) -> None:
    print(f"La recaudación del coche {n_coche} de la línea {n_linea} es: ${lista[n_linea][n_coche]}")


def mostrar_recaudacion_total(lista: list) -> None:

    suma = 0

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            suma += lista[i][j]

    print(f"La recaudación total es de: ${suma}")


def emparejar_opcion(opcion_elegida: int) -> None:

    n_legajo = int(input("Ingresa tu número de legajo: "))
    legajo_valido = verificar_numero_legajo(n_legajo, lista_legajos)

    # Falta agregar validaciones de línea y coche
    if legajo_valido:
        match opcion_elegida:
            case 1:
                indice_linea = int(input("Ingresa la línea (entre 0 y 2): "))
                while indice_linea < 0 or indice_linea > 2:
                    indice_linea = int(input("Ingresa la línea (entre 0 y 2): "))
                indice_coche = int(input("Ingresa el coche (entre 0 y 4): "))
                while indice_coche < 0 or indice_coche > 4:
                    indice_coche = int(input("Ingresa el coche (entre 0 y 4): "))
                recaudacion = int(input("Ingresa la recaudación (solo valores positivos): $"))
                while recaudacion < 0:
                    recaudacion = int(input("Ingresa la recaudación (solo valores positivos): $"))
                cargar_planilla_de_recaudacion(indice_linea,
                                               indice_coche,
                                               recaudacion,
                                               lineas)
            case 2:
                mostrar_recaudacion(lineas)
            case 3:
                n_linea = int(input("Ingresa el número de línea (entre 0 y 2): "))
                while n_linea < 0 or n_linea > 2:
                    n_linea = int(input("Ingresa el número de línea (entre 0 y 2): "))
                mostrar_recaudacion_linea(lineas, n_linea)
            case 4:
                n_linea = int(input("Ingresa el número de línea (entre 0 y 2): "))
                while n_linea < 0 or n_linea > 2:
                    n_linea = int(input("Ingresa el número de línea (entre 0 y 2): "))
                n_coche = int(input("Ingresa el número de coche (entre 0 y 4): "))
                while n_coche < 0 or n_coche > 4:
                    n_coche = int(input("Ingresa el número de coche (entre 0 y 4): "))
                mostrar_recaudacion_coche(lineas, n_linea, n_coche)
            case 5:
                mostrar_recaudacion_total(lineas)
    else:
        print("El legajo ingresado no es válido, vuelve a intentar")


while True:
    eleccion_usuario = desplegar_menu_de_opciones()

    if eleccion_usuario == 6:
        print("Programa terminado")
        break

    emparejar_opcion(eleccion_usuario)