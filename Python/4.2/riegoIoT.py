# Sistema de riego inteligente
# Basado en la lógica declarativa del archivo Prolog: riegoIoT.pl


# BASE DE CONOCIMIENTOS (HECHOS)
# Humedad por zona
humedad = {
    "norte": "baja",
    "sur": "media",
    "este": "alta",
    "oeste": "baja"
}

# Temperatura por zona (en grados Celsius)
temperatura = {
    "norte": 35,
    "sur": 29,
    "este": 31,
    "oeste": 33
}

# Hora actual por zona (en formato de 24h)
hora = {
    "norte": 20,
    "sur": 9,
    "este": 12,
    "oeste": 7
}

# Probabilidad de lluvia (True = hay posibilidad)
probabilidad_lluvia = {
    "norte": False,
    "sur": True,
    "este": False,
    "oeste": False
}

# Tipo de riego recomendado por zona
tipo_riego = {
    "norte": "goteo",
    "sur": "aspersion",
    "este": "manual",
    "oeste": "goteo"
}

# Umbral de temperatura para activar alerta de calor
umbral_calor = 32


# REGLAS DEL SISTEMA (FUNCIONES PURAS)

def hora_adecuada(zona):
    # Devuelve True si la hora en la zona es antes de las 10 o después de las 18.
    h = hora[zona]
    return h < 10 or h > 18

def alerta_calor(zona):
    # Devuelve True si la temperatura en la zona supera el umbral.
    return temperatura[zona] >= umbral_calor

def activar_riego(zona):
    """
    Determina si se debe activar el riego:
    - La humedad es baja
    - No hay probabilidad de lluvia
    - Es una hora adecuada
    """
    return (humedad[zona] == "baja"
            and not probabilidad_lluvia[zona]
            and hora_adecuada(zona))

def estado_riego(zona):
    # Devuelve el estado del riego como 'Activado' o 'Desactivado'.
    return "Activado" if activar_riego(zona) else "Desactivado"

def recomendacion(zona):
    """
    Genera una recomendación basada en:
    - Si el riego se activa y hay calor extremo, sugerir riego nocturno o específico
    - Si no, indicar que no hay recomendaciones especiales
    """
    if activar_riego(zona) and alerta_calor(zona):
        tipo = tipo_riego[zona]
        return (f"Alerta: riego activado con temperatura extrema en la zona {zona}. "
                f"Considere riego por la noche o con sistema {tipo}.")
    return f"Zona {zona}: Sin recomendaciones especiales para el riego."


# EJECUCION DEL SISTEMA POR CADA ZONA

def evaluar_zonas(zonas):
    # Itera sobre todas las zonas, mostrando estado del riego y recomendaciones.
    for z in zonas:
        print(f"Zona: {z}")
        print(f"  Estado del riego: {estado_riego(z)}")
        print(f"  Recomendación: {recomendacion(z)}")
        print()  # Separador

# Lista de zonas definidas
zonas = ["norte", "sur", "este", "oeste"]

# Llamada al sistema
evaluar_zonas(zonas)

