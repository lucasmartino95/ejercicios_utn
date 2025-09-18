def devolver_numero_entero_positivo() -> int:

    while True:
        numero: int = int(input("Ingresa un número positivo: "))
        if numero > 0:
            return numero
        print("El número debe ser mayor que 0")


def devolver_numero_flotante_positivo() -> float:

    while True:
        numero: float = float(input("Ingresa un número positivo con decimales: "))
        if numero > 0:
            return numero
        print("El número debe ser mayor que 0")


def devolver_cadena(longitud: int) -> str:

    cadena: str = input(f"Escribe algo de {longitud} caracteres: ")
    while True:
        if len(cadena) != longitud:
            print(len(cadena), longitud)
            cadena: str = input(f"Escribe algo de {longitud} caracteres: ")
        else:
            return cadena


print(devolver_numero_entero_positivo())

print(devolver_numero_flotante_positivo())

print(devolver_cadena(5))