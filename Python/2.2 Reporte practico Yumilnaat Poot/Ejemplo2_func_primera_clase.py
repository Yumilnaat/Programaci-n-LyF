def es_aprobado(calificacion):
    return calificacion >= 70

def evaluar_alumno(func, calificacion): #La función es_aprobado(nota) es pasada como argumento a evaluar_alumno(func, nota).
    return "Aprobado" if func(calificacion) else "Reprobado"

calificacion_final = 68
print(f"Estado del estudiante: {evaluar_alumno(es_aprobado, calificacion_final)}") #evaluar_alumno ejecuta la función recibida
                                                                                    #(es_aprobado) sobre la nota dada
