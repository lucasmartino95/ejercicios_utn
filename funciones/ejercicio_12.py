def crear_tabla_de_multiplicar(inicio: int = 1, fin: int = 10) -> str:
    for inicio in range(inicio, fin + 1):
        resultado = inicio * fin
        tabla = str(f"{fin} x {inicio} = {resultado}")
        print(tabla)


crear_tabla_de_multiplicar(1, 5)