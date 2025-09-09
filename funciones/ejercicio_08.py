def encontrar_el_maximo(numero_uno: int,
                        numero_dos: int,
                        numero_tres: int,) -> int:
    if numero_uno > numero_dos and numero_uno > numero_tres:
        maximo = numero_uno
    elif numero_dos > numero_uno and numero_dos > numero_tres:
        maximo = numero_dos
    else:
        maximo = numero_tres

    return maximo

print(encontrar_el_maximo(5, 10, 2))