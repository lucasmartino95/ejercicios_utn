# Facturación del Servicio de Agua Potable
print()
consumo = int(input("Ingresa la cantidad de consumo en metros cúbicos: "))
tipo_de_cliente = input("Ingresa el tipo de cliente (residencial/" \
"comercial/industrial): ")
print()

cargo_fijo = 7000
costo_por_metro_cubico = 200
subtotal_de_consumo = cargo_fijo + costo_por_metro_cubico * consumo

bonificacion = 0
recargo = 0

if tipo_de_cliente == "residencial" and subtotal_de_consumo < 35000:
    print("5% de descuento adicional por no superar los $35000 de consumo")
    bonificacion = 5
    subtotal = subtotal_de_consumo - (subtotal_de_consumo * 0.05)

match tipo_de_cliente:
    case "residencial":
        if consumo < 30:
            bonificacion += 10
            subtotal = subtotal_de_consumo - (subtotal_de_consumo * bonificacion/100)
        elif consumo > 80:
            recargo = 15
            subtotal = subtotal_de_consumo + (subtotal_de_consumo * recargo/100)
    case "comercial":
        if consumo > 150:
            bonificacion = 8
            subtotal = subtotal_de_consumo - (subtotal_de_consumo * bonificacion/100)
        elif consumo > 300:
            bonificacion = 12
            subtotal = subtotal_de_consumo - (subtotal_de_consumo * bonificacion/100)
        elif consumo < 50:
            recargo = 5
            subtotal = subtotal_de_consumo + (subtotal_de_consumo * recargo/100)
    case "industrial":
        if consumo > 500:
            bonificacion = 20
            subtotal = subtotal_de_consumo - (subtotal_de_consumo * bonificacion/100)
        elif consumo > 1000:
            bonificacion = 30
            subtotal = subtotal_de_consumo - (subtotal_de_consumo * bonificacion/100)
        elif consumo < 200:
            recargo = 10
            subtotal = subtotal_de_consumo + (subtotal_de_consumo * recargo/100) 

iva_aplicado = subtotal * 0.21
total_a_pagar = subtotal + iva_aplicado

print(f"Subtotal de consumo: ${subtotal_de_consumo}\n\
Bonificaciones: {bonificacion}%\n\
Recargos: {recargo}%\n\
Subtotal: ${subtotal}\n\
IVA Aplicado: ${iva_aplicado}\n\
Total a pagar: ${total_a_pagar}")
print()
        