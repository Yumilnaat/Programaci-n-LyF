def agregar_asignatura(lista):
    asig_nueva = input("Agrega una nueva asignatura o 'no' para salir: ")
    if asig_nueva == "no":
        return lista
    return agregar_asignatura(lista + [asig_nueva]) #recursion

asingaturas = ["Graficacion", "Automatas", "Investigacion"]

nueva_list = agregar_asignatura(asingaturas)

print(nueva_list)
