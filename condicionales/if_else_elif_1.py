"""
Determinar la posición de un jugador de baloncesto en base
a su altura
"""

altura = int(input("Ingresa la altura del jugador de baloncesto (cms): "))

if altura < 160:
    print("La posición del jugador es Base")
elif altura <= 179:
    print("La posición del jugador es Escolta")
elif altura <= 199:
    print("La posición del jugador es Alero")
else:
    print("La posición del jugador es Ala-Pivot o Pivot")
