"""
Una agencia de viajes nos pide informar si hacemos viajes a lugares
según la estación del año. En caso de hacerlo mostrar por print 
el mensaje “Se viaja”, caso contrario mostrar “No se viaja”
"""

realiza_viaje = input("¿Realizará un viaje? (sí/no): ")

estacion = input("Ingrese la estación del año: ")

if realiza_viaje == "sí":
    mensaje = "Se viaja"
    match estacion:
        case "invierno":
            mensaje += "\nDestino: Bariloche"
        case "verano":
            mensaje += " \nDestino: Mar del Plata y Cataratas"
        case "otoño":
            mensaje += " \nDestino: Todos los lugares"
        case "primavera":
            mensaje += " \nDestino: Todos los lugares menos Bariloche"
    print(mensaje)
else:
    print("No se viaja")