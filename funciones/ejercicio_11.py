def numeros_primos(numero_usuario: int) -> str:
    limite: int = numero_usuario + 1
    numeros_primos: int = 0
    divisores: int = 0
    
    for numero in range(2, limite):
        divisores = 0
        for numero_dos in range(1, numero + 1):
            if numero % numero_dos == 0:
                divisores += 1
        if divisores == 2:
            numeros_primos += 1
            print(numero)
    
    return f"La cantidad de números primos encontrados es: {numeros_primos}"

print(numeros_primos(20))