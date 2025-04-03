jugadores = [

    {"nombre":"Brandon", "Edad":22},
    {"nombre":"Alana", "Edad":23},
    {"nombre":"Oso", "Edad":24},
    {"nombre":"Kafai", "Edad":25}
]

#usar map para extraer nombre de jugadores

nombre_jugadores = list(map(lambda jugador: jugador["nombre"],jugadores))
print(nombre_jugadores)