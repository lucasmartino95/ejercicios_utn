def es_primo(numero: int) -> bool:
    divisores: int = 0
    for i in range(1, numero + 1):
        print(i, numero)
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False
    
print(es_primo(12))