from validate import *

def get_int(mensaje: str,
            mensaje_error: str,
            minimo: int,
            maximo: int,
            reintentos: int) -> int|None:
    
    print(mensaje)

    numero: int = int(input("Ingresa un número: "))

    limite: int = 0

    bandera = True

    while bandera:
        if numero >= minimo and numero <= maximo:
            dato_salida = numero
            bandera = False
            return dato_salida
        else:
            # Le resto 1 a reintentos para que se tome
            # en cuenta el primer input que está fuera
            # del while
            if limite < (reintentos - 1):
                print(mensaje_error)
                limite += 1
                numero: int = int(input("Ingresa un número: "))
            else:
                bandera = False
                return None
            

def get_float(mensaje: str,
            mensaje_error: str,
            minimo: int,
            maximo: int,
            reintentos: int) -> float|None:
    
    print(mensaje)

    numero: float = float(input("Ingresa un número: "))

    limite: int = 0

    bandera = True

    while bandera:
        if numero >= minimo and numero <= maximo:
            dato_salida = numero
            bandera = False
            return dato_salida
        else:
            # Le resto 1 a reintentos para que se tome
            # en cuenta el primer input que está fuera
            # del while
            if limite < (reintentos - 1):
                print(mensaje_error)
                limite += 1
                numero: float = float(input("Ingresa un número: "))
            else:
                bandera = False
                return None


def get_string(mensaje: str,
               mensaje_error: str,
               longitud: int,
               reintentos: int) -> str|None:

    print(mensaje)

    cadena: str = input(f"Escribe algo de {longitud} caracteres: ")

    bandera = True

    limite = 0

    while bandera:
        if len(cadena) != longitud:
            # Le resto 1 a reintentos para que se tome
            # en cuenta el primer input que está fuera
            # del while
            if limite < reintentos - 1:
                print(mensaje_error)
                cadena: str = input(f"Escribe algo de {longitud} caracteres: ")
                limite += 1
            else:
                bandera = False
                return None
        else:
            bandera = False
            dato_salida = cadena
            return dato_salida


entero = get_int("Pedir número entero", "Número inválido", 1, 10, 3)

numero_decimal = get_float("Pedir número con decimales", "Número inválido", 1, 10, 3)

texto = get_string("Pedir cadena de caracteres", "Texto inválido", 5, 3)
