def obtener_nombre(nombre: str) -> str:

    return nombre


def analizar_temperatura(temperatura: float) -> str:

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


def analizar_imc(peso: float, altura: float) -> str:
     
    imc = peso / (altura ** 2)

    if imc < 18.5:
        analisis_imc = "Es necesario aumentar la ingesta calórica."
    elif imc < 25:
        analisis_imc = "Peso equilibrado."
    else:
        analisis_imc = "Es necesario disminuir la ingesta calórica."
    
    return analisis_imc


def analizar_presion(presion_sistolica: float, presion_diastolica: float) -> str:
    
    if presion_sistolica < 90 or presion_diastolica < 60:
        analisis_presion = "Baja"
    elif presion_sistolica > 140 or presion_diastolica > 90:
        analisis_presion = "Alta"
    else:
        analisis_presion = "Normal"
    
    return analisis_presion


def enviar_mensaje_al_paciente() -> None:
    
    diagnostico = f"""
    Diágnostico del paciente: {obtener_nombre("Lucas")}
    Peso: {analizar_imc(70, 1.70)}
    Temperatura: {analizar_temperatura(37)}
    Presión: {analizar_presion(90, 61)}
    """

    print(diagnostico)


enviar_mensaje_al_paciente()