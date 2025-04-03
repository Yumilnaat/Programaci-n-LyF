a = ["Programacion Web"]
b = a + ["Prog Log y Func"]

# print(a)
# print(b)

def agregar_asignatura(lista, asig):
    return lista + [asig]

res= agregar_asignatura(a, input('Ingresa una nueva asignatura: '))
print(res)