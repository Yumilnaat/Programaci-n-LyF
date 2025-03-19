def transformar_calificaciones(funcion, calificaciones): #recibe una función y una lista.
    return [funcion(calificacion) for calificacion in calificaciones]

def curva(calificacion): #es pasada como argumento y se aplica a cada calificación en la lista.
    return min(calificacion + 5, 100)  # Aumenta 5 puntos sin superar 100

calificacion = [70, 85, 90, 78, 60]
print(f"Calificaciones ajustadas: {transformar_calificaciones(curva, calificacion)}")
