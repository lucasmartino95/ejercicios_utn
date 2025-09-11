# Preguntar a qué se refiere con especializar funciones
# y cuál es el desafío for

def devolver_numero_entero() -> int:
    numero: int = int(input("Ingresa un número entero: "))
    return numero


def devolver_numero_flotante() -> float:
    numero: float = float(input("Ingresa un número con decimales: "))
    return numero


def devolver_cadena() -> str:
    cadena: str = input("Escribe algo: ")
    return cadena


print(devolver_numero_entero())

print(devolver_numero_flotante())

print(devolver_cadena())