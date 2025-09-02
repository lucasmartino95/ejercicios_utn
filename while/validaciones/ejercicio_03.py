nota = int(input("Ingresa una nota: "))

while nota < 1 or nota > 10:
    print("La nota debe ser del 1 al 10 inclusive")
    nota = int(input("Ingresa una nota: "))

print(f"La nota es: {nota}")