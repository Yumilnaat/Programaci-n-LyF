def convertir_mg_a_gb(mb): #La función recibe un número en megabytes y lo convierte a gigabytes
    return mb / 1024

almacenamiento_mb = 20480
print(f"El almacenamiento en GB es: {convertir_mg_a_gb(almacenamiento_mb)} GB")
