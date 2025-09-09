numero: int = int(input("Ingresa un número: "))

def es_par() -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par())