def generar_descuento(porcentaje): #devuelve una función lambda que calcula el precio con descuento.
    return lambda costo: costo - (costo * porcentaje / 100)

descuento_estudiante = generar_descuento(15) #almacena la función generada con 15% de descuento y la aplica al costo de inscripción.
costo_inscripcion = 5000
print(f"Costo con descuento de estudiante: ${descuento_estudiante(costo_inscripcion)}")
