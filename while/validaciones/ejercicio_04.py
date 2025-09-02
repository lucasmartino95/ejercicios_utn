color_usuario = input("Ingresa un color (Rojo/Verde/Azul): ")

while color_usuario != "Rojo" and color_usuario != "Verde" and color_usuario != "Azul":
    color_usuario = input("Ingresa un color: ")

print(f"Ingresaste el color: {color_usuario}")