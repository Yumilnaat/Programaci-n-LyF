def calcular_promedio(calificaciones): #recibe una lista de calificaciones y devuelve su promedio
    return sum(calificaciones) / len(calificaciones)

calif_finales = [85, 90, 78, 92, 88]
promedio = calcular_promedio(calif_finales)
print("El promedio del estudiante es: ", promedio)
