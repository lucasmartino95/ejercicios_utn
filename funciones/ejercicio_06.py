numero: int = int(input("Ingresa un número: "))

def es_par_o_impar() -> None:
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

es_par_o_impar()