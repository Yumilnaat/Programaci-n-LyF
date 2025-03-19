def ejecutar_simulacion(callback): #recibe una función y la ejecuta al finalizar la simulación.
    print("Ejecutando simulación de tráfico de red...")
    callback()

def notificar_fin(): #es pasada como argumento y se ejecuta después.
    print("Simulación completada. Revisa los resultados.")

ejecutar_simulacion(notificar_fin)
