jugadores = [

    {"nombre":"Brandon", "Edad":22},
    {"nombre":"Alana", "Edad":23},
    {"nombre":"Oso", "Edad":24},
    {"nombre":"Kafai", "Edad":25}
]

#usar filter para obtenr jugadores mayores a 23 anios
jugadores_mayores = list(filter(lambda jugador: jugador["Edad"]>23, jugadores))#propiedad edad

print(jugadores_mayores)