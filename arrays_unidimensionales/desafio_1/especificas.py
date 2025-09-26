def determinar_positivo(numero: int) -> bool:

    if numero > 0:
        return True
    else:
        return False
    

def determinar_negativo(numero: int) -> bool:

    if numero < 0:
        return True
    else:
        return False
    

def determinar_numero_par(numero: int) -> bool:
    
    if (numero % 2) == 0:
        return True
    else:
        return False