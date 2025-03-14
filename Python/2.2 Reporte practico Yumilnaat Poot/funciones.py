#CALLBACK
'''
def operar(n1, n2, funcion):
    return funcion(n1,n2)

def suma(a, b): #Funcion de primer orden
    return a + b

def resta(a, b):
    return a - b

resultado = operar(5, 3, suma) #Pasamos la funcion suma como argumento
print(resultado) #la funcion suma actua como callback
'''

#FUNCION DE PRIMERA CLASE   
'''
def saludo():
    return "Hola!"

mi_variable = saludo #Asignamos la funcion a una variable
print(mi_variable()) # Llamamos a la función a través de la variable

def saludo2():
    return "Que tal"

variable = saludo2
print(variable())
'''

#OPERACION DE ORDEN SUPERIOR
'''
def elegir_operacion(operacion):
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    
    if operacion == "multiplicar":
        return multiplicar
    else:
        return dividir
    
doble = elegir_operacion("multiplicar")
print(doble(10))
divide2 = elegir_operacion("dividir")
print(divide2(10))
'''

#FUNCION LAMBDA

doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney', 'Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola ' + nombre, alumnos))
print(saludar_alumnos)

#Sin lambda
def saludar(nombre):
    return 'Hola ' + nombre

lista_saludos = list(map(saludar, alumnos))
print(lista_saludos)