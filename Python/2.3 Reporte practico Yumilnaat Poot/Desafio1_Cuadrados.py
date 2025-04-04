def cuadradosLista(arreglo):
    
    # Filtrar solo los números enteros positivos con filter
    enteros_positivos = filter(lambda x: isinstance(x, int) and x > 0, arreglo)
    
    # Elevar al cuadrado los números filtrados con map
    cuadrados = map(lambda x: x**2, enteros_positivos)
    
    return list(cuadrados)

# Ejemplo de uso
cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)
