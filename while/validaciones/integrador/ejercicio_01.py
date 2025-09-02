apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
estado_civil = input("Ingresa tu estado civil: "
"(Soltero/a - Casado/a - Divorciado/a - Viudo/a): ")
numero_de_legajo = int(input("Ingresa tu número de legajo (4 cifras): "))

while edad < 18 or edad > 90:
    print("La edad permitida es entre 18 a 90 años inclusive")
    edad = int(input("Ingresa tu edad: "))

while (estado_civil != "Soltero" and estado_civil != "Soltera") and \
    (estado_civil != "Casado" and estado_civil != "Casada") and \
    (estado_civil != "Divorciado" and estado_civil != "Divorciada") and \
    (estado_civil != "Viudo" and estado_civil != "Viuda"):
        print("No ingresaste un estado de civil válido")
        estado_civil = input("Ingresa tu estado civil "
        "(Soltero/a - Casado/a - Divorciado/a - Viudo/a): ")

while numero_de_legajo < 1000 or numero_de_legajo >= 10000:
      print("No ingresaste un número de legajo válido")
      numero_de_legajo = int(input("Ingresa tu número de legajo (4 cifras): "))

print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Número de legajo: {numero_de_legajo}")
