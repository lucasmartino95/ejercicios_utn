nombre = input("Ingresa tu nombre: ")
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

temperatura = float(input("Ingresa tu temperatura: "))
presion_sistolica = float(input("Ingresa tu presión sistolica: "))
presion_diastolica = float(input("Ingresa tu presión diastolica: "))


def obtener_nombre() -> str:
    
    return nombre


def analizar_temperatura() -> str:

    if temperatura > 41:
        fiebre = "Muy alta."
    elif temperatura > 39:
        fiebre = "Alta."
    elif temperatura >= 38:
        fiebre = "Fiebre moderada."
    elif temperatura > 37.3:
        fiebre = "Febrícula."
    else:
        fiebre = "Temperatura normal."
    
    return fiebre


def analizar_imc() -> str:
     
    imc = peso / (altura ** 2)

    if imc < 18.5:
        analisis_imc = "Es necesario aumentar la ingesta calórica."
    elif imc < 25:
        analisis_imc = "Peso equilibrado."
    else:
        analisis_imc = "Es necesario disminuir la ingesta calórica."
    
    return analisis_imc


def analizar_presion() -> str:
    
    if presion_sistolica < 90 or presion_diastolica < 60:
        analisis_presion = "Baja"
    elif presion_sistolica > 140 or presion_diastolica > 90:
        analisis_presion = "Alta"
    else:
        analisis_presion = "Normal"
    
    return analisis_presion


def enviar_mensaje_al_paciente() -> None:

    diagnostico = f"""
    Diágnostico del paciente: {obtener_nombre()}
    Peso: {analizar_imc()}
    Temperatura: {analizar_temperatura()}
    Presión: {analizar_presion()}
    """

    print(diagnostico)


enviar_mensaje_al_paciente()