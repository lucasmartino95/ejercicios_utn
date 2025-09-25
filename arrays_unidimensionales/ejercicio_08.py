nombres = ["Lucas", "Juan", "Fernando", "Juan"]


def reemplazar_nombre(lista_nombres: list,
                      nombre_antiguo: str,
                      nombre_nuevo: str) -> int:
    
    reemplazos = 0

    for i in range(len(lista_nombres)):
        if nombre_antiguo == lista_nombres[i]:
            lista_nombres[i] = nombre_nuevo
            reemplazos += 1
        
    return reemplazos


print(reemplazar_nombre(nombres, "Juan", "Daniel"))