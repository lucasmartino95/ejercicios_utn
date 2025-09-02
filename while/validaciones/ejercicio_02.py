clave = "159abc"
clave_usuario = input("Ingresa una clave: ")
intentos = 0

while clave_usuario != clave and intentos < 2:
    clave_usuario = input("Ingresa una clave: ")
    intentos += 1

if clave_usuario == clave:
    print("Clave correcta") 
else:
    print(f"Fallaste el máximo de {intentos + 1} intentos permitidos")
