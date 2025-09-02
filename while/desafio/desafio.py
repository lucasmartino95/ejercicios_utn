empleados = 0
empleados_masculino_ia = 0
empleados_no_ia = 0

while empleados < 4:
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    while edad < 18:
        print("La edad debe ser de 18 años o más")
        edad = int(input("Ingresa tu edad: "))

    genero = input("Ingresa tu genero: (Masculino - Femenino - Otro): ")

    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        print("No seleccionaste la opción correcta")
        genero = input("Ingresa tu genero: (Masculino - Femenino - Otro): ")
    
    tecnologia_elegida = input("Ingresa la tecnología elegida (IA - RV/RA - IOT): ")

    while tecnologia_elegida != "IA" and tecnologia_elegida != "RV/RA" and \
    tecnologia_elegida != "IOT":
        print("No seleccionaste la tecnología correcta")
        tecnologia_elegida = input("Ingresa la tecnología elegida (IA - RV/RA - IOT): ")

    if genero == "Masculino" and tecnologia_elegida == "IA" and (edad >= 25 and edad <= 50):
        empleados_masculino_ia += 1
    
    if genero != "Femenino" and (edad >= 33 and edad <= 40) and tecnologia_elegida != "IA":
        empleados_no_ia += 1
    
    if empleados == 0:
        edad_maxima = edad
        nombre_edad_maxima = nombre
        tecnologia_edad_maxima = tecnologia_elegida

    if edad > edad_maxima:
        edad_maxima = edad
        nombre_edad_maxima = nombre
        tecnologia_edad_maxima = tecnologia_elegida

    empleados += 1
    porcentaje_no_ia = empleados_no_ia * 100 / empleados

print(f"Cantidad de empleados masculinos que votaron por IA: {empleados_masculino_ia}")
print(f"El porcentaje de empleados que no votó por IA según los requisitos es: {porcentaje_no_ia}%")
print(f"El empleado masculino de mayor edad es: {nombre_edad_maxima} y votó: {tecnologia_edad_maxima}")