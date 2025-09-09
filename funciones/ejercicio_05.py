PI = 3.1416

def calcular_area_circulo(radio: float) -> float:
    area: float = PI * (radio ** 2)
    return area

print(calcular_area_circulo(12))