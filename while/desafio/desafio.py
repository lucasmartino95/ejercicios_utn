empleados = 0
empleados_masculino_ia = 0
empleados_no_ia = 0

while empleados < 2:
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

    if genero == "Masculino" and (tecnologia_elegida == "IA" or tecnologia_elegida == "IOT") and (edad >= 25 and edad <= 50):
        empleados_masculino_ia += 1
    
    if genero != "Femenino" and (edad >= 33 and edad <= 40) and tecnologia_elegida != "IA":
        empleados_no_ia += 1

    # Falta item 3 
    empleados += 1
    porcentaje_no_ia = empleados_no_ia * 100 / empleados

print("[1] Genero masculino y edad entre 25 a 50 años (inclusive) que votó por IA o IOT:")
print(f"La cantidad de empleados es: {empleados_masculino_ia}")

print("[2] No voto por IA, no es femenino y su edad está entre 33 y 40 años:")
print(f"El porcentaje es: {porcentaje_no_ia}%")

# print(f"[3] El empleado masculino de mayor edad es: {nombre_edad_maxima} y votó: {tecnologia_edad_maxima}")