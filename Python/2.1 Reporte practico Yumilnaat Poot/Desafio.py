# Desafío: Sombrero Seleccionador de Ramas de Sistemas Computacionales
"""
Este script simula un sombrero seleccionador que ayuda a los alumnos de ISC a descubrir cuál de las ramas de sistemas
computacionales es la más recomendable, basándose en sus respuestas a una serie de preguntas.
Variables:
    redes (int): Contador de puntos para la rama de Redes.
    bases_de_datos (int): Contador de puntos para la rama de Bases de Datos.
    desarrollo_software (int): Contador de puntos para la rama de Desarrollo de Software.
    programacion_hardware (int): Contador de puntos para la rama de Programación Hardware.
    modelado_3d (int): Contador de puntos para la rama de Modelado 3D.
    gestion_proyectos (int): Contador de puntos para la rama de Gestión de Proyectos de Software.
"""

# Inicialización de los contadores de puntos
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

"""
Flujo del programa:  
1. Imprime el título del programa.  
"""

print('========--')  
print('Sombrero Seleccionador de Ramas de Sistemas Computacionales 💡')  
print('========--')  

"""
2. Realiza las preguntas y actualiza los puntos de las ramas según la respuesta.  
3. Determina y anuncia la rama a la que el alumno ha sido asignado, basada en los puntos acumulados.  
Preguntas:  
1. ¿Qué te interesa más?  
   - 1) Configurar y mantener redes de computadoras.  
   - 2) Diseñar y gestionar bases de datos.  
   - 3) Desarrollar aplicaciones y software.  
   - 4) Programar y trabajar con hardware.  
   - 5) Crear modelos y animaciones en 3D.  
   - 6) Planificar y gestionar proyectos de software.  
"""

# ...... Pregunta 1 ......

print('P1) ¿Qué te interesa más?')

print(' 1) Configurar y mantener redes de computadoras.')
print(' 2) Diseñar y gestionar bases de datos.')
print(' 3) Desarrollar aplicaciones y software.')
print(' 4) Programar y trabajar con hardware.')
print(' 5) Crear modelos y animaciones en 3D.')
print(' 6) Planificar y gestionar proyectos de software.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# ...... Pregunta 2 ......

print('\nP2) ¿Qué tipo de proyectos te gustaría liderar?')

print(' 1) Implementación de infraestructuras de red.')
print(' 2) Optimización de bases de datos.')
print(' 3) Desarrollo de aplicaciones móviles.')
print(' 4) Diseño de circuitos y sistemas embebidos.')
print(' 5) Creación de animaciones y efectos visuales.')
print(' 6) Coordinación de equipos de desarrollo.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# ...... Pregunta 3 ......

print('\nP3) ¿Qué te parece más interesante?')

print(' 1) Resolver problemas de conectividad.')
print(' 2) Diseñar esquemas de bases de datos.')
print(' 3) Escribir código para aplicaciones.')
print(' 4) Trabajar con microcontroladores.')
print(' 5) Crear modelos 3D para videojuegos.')
print(' 6) Gestionar plazos y recursos en proyectos.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# ...... Pregunta 4 ......

print('\nP4) ¿En qué área te gustaría especializarte?')

print(' 1) Seguridad en redes.')
print(' 2) Big Data y análisis de datos.')
print(' 3) Desarrollo de aplicaciones web.')
print(' 4) Sistemas embebidos y IoT.')
print(' 5) Animación y diseño 3D.')
print(' 6) Metodologías ágiles y Scrum.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# ...... Pregunta 5 ......

print('\nP5) ¿Qué tipo de herramientas prefieres usar?')

print(' 1) Herramientas de configuración de redes.')
print(' 2) Sistemas de gestión de bases de datos.')
print(' 3) Entornos de desarrollo integrados (IDEs).')
print(' 4) Herramientas de programación de hardware.')
print(' 5) Software de modelado 3D.')
print(' 6) Herramientas de gestión de proyectos.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

"""
Resultados:

- Imprime los puntos acumulados para cada rama.
- Anuncia la rama a la que el alumno ha sido asignado, basada en los puntos acumulados.
"""

print("\nResultados:")
print("Redes: ", redes)
print("Bases de Datos: ", bases_de_datos)
print("Desarrollo de Software: ", desarrollo_software)
print("Programación Hardware: ", programacion_hardware)
print("Modelado 3D: ", modelado_3d)
print("Gestión de Proyectos de Software: ", gestion_proyectos)

# Determinar la rama con el puntaje más alto
puntajes = {
    "Redes": redes,
    "Bases de Datos": bases_de_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos de Software": gestion_proyectos
}

rama_seleccionada = max(puntajes, key=puntajes.get)
print(f'\n¡La rama más recomendable para ti es: {rama_seleccionada}!')