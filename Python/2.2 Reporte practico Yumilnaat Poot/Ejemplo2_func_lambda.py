estudiantes = [{"nombre": "Ana", "nota": 85}, {"nombre": "Luis", "nota": 78}, {"nombre": "Carlos", "nota": 92}]
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["nota"], reverse=True)
print(f"Estudiantes ordenados por nota: {estudiantes_ordenados}")
#lambda x: x["nota"] se usa como criterio de ordenación en sorted().
#Se ordena la lista de diccionarios por calificación en orden descendente.
