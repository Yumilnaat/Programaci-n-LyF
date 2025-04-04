aliemtos_bebidas = ["Frijoles Refritos","Coca Cola","Zumo de Naranja", "Café de Olla", "Gorditas de Chicharrón", "Huevos Motuleños"]

lista_ordenada = sorted(aliemtos_bebidas)

cadena = ", ".join(lista_ordenada)

lista_slug = list(map (lambda nombre: nombre.lower().replace(" ","-"),lista_ordenada))


print("lista de slugs: ", lista_slug)
print("Cadena de nombres en orden alfabetico: ", cadena)