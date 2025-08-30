""" 
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego 
mostrar un mensaje según el valor
"""

import random

nota = random.randint(1, 10)

if nota >= 6 and nota <= 10:
    print(f"Promoción directa, la nota es {nota}")
elif nota >= 4 and nota <= 5:
    print(f"Aprobado, la nota es: {nota}")
else:
    print(f"Desaprobado, la nota es: {nota}")