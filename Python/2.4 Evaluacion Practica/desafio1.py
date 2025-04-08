import tkinter as tk
from tkinter import messagebox, simpledialog
from functools import reduce

# === VARIABLES GLOBALES ===

# Lista de materias a evaluar
materias = [
    "Programación web del lado del servidor",
    "Inteligencia Artificial",
    "Administración de redes"
]

# Aspectos que serán evaluados en cada materia
aspectos = [
    "Contenido",
    "Nivel de complejidad",
    "Herramientas o tecnologías",
    "Prácticas"
]

# Aqui se guardaran todas las encuestas realizadas por todos los alumnos, en forma de diccionario
encuestas = []

# === FUNCIONES DE ESTADÍSTICA (FUNCIONES PURAS) ===

# Calcula el promedio de una lista de valores
def promedio(valores):
    return reduce(lambda x, y: x + y, valores) / len(valores) if valores else 0

# Suma total de una lista
def total(valores):
    return reduce(lambda x, y: x + y, valores) if valores else 0

# Valor máximo de una lista
def maximo(valores):
    return reduce(lambda x, y: x if x > y else y, valores) if valores else 0

# Valor mínimo de una lista
def minimo(valores):
    return reduce(lambda x, y: x if x < y else y, valores) if valores else 0

# === FUNCIONES DE FILTRADO Y ANÁLISIS DE ENCUESTAS ===

# Filtra todas las encuestas que correspondan a la materia dada
def filtrar_encuestas_por_materia(materia):
    return list(filter(lambda e: e["materia"] == materia, encuestas))

# Filtra todas las encuestas hechas por un alumno específico
def filtrar_encuestas_por_alumno(nombre):
    return list(filter(lambda e: e["nombre"].lower() == nombre.lower(), encuestas))

# Extrae una lista de los valores numéricos de un aspecto para un conjunto de encuestas
def obtener_valores_aspecto(encuestas_local, aspecto_key):
    return list(map(lambda e: e[aspecto_key], encuestas_local))

# Calcula el promedio, total, máximo y mínimo por cada aspecto usando las encuestas de una materia
def obtener_estadisticas(encuestas_materia):
    resultado = {}
    for aspecto in aspectos:
        valores = obtener_valores_aspecto(encuestas_materia, aspecto)
        resultado[aspecto] = {
            "promedio": promedio(valores),
            "total": total(valores),
            "max": maximo(valores),
            "min": minimo(valores)
        }
    return resultado

# === FUNCIÓN RECURSIVA PARA MOSTRAR RESULTADOS ===

# Recorre un diccionario de estadísticas de manera recursiva (no usa for, sino llamadas a sí misma)
# para convertirlo en una cadena de texto formateada. Sirve para mostrar los resultados bonitos en messagebox.
def formatear_resultados(diccionario, claves=None, i=0):
    if claves is None:
        claves = list(diccionario.keys())
    if i >= len(claves):
        return ""
    
    clave = claves[i]
    valor = diccionario[clave]
    
    if isinstance(valor, dict):
        resultado = f"\n{clave}:\n"
        for subclave in valor:
            resultado += f"  {subclave.capitalize()}: {valor[subclave]:.2f}\n"
    else:
        resultado = f"{clave}: {valor:.2f}\n"
    
    return resultado + formatear_resultados(diccionario, claves, i + 1)

# === VALIDACIÓN DE CALIFICACIONES ===

# Filtra cualquier calificación fuera del rango de 1 a 5. Si no hay ninguna, retorna True, si hay al menos una, False.
def validar_rango(valores):
    return len(list(filter(lambda x: x < 1 or x > 5, valores))) == 0

# === FUNCIONES DE LA INTERFAZ ===

# Guarda los datos de una encuesta individual
def guardar_encuesta():
    try:
        # Toma el nombre del alumno y la materia seleccionada.
        calificaciones = list(map(int, [entry.get() for entry in entradas_aspectos]))
        if not validar_rango(calificaciones):
            messagebox.showerror("Error", "Las calificaciones deben estar entre 1 y 5")
            return
        
        # Toma las calificaciones de los 4 aspectos desde las cajas de entrada.
        # Valida que estén entre 1 y 5.
        # Si están bien, guarda los datos en un diccionario y lo añade a encuestas.
        encuesta = {
            "nombre": entry_nombre.get(),
            "materia": materia_var.get()
        }
        for i, aspecto in enumerate(aspectos):
            encuesta[aspecto] = calificaciones[i]
        
        encuestas.append(encuesta)
        messagebox.showinfo("Guardado", f"Evaluación guardada para {encuesta['materia']}")
        
        # Limpia los campos para otra encuesta
        for entry in entradas_aspectos:
            entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos del 1 al 5.")

# Muestra los resultados generales por asignatura:
# Recorre todas las materias.
# Para cada una, obtiene las encuestas hechas.
# Calcula las estadísticas de cada aspecto.
# Muestra los resultados con messagebox.
def ver_resultados_generales():
    if not encuestas:
        messagebox.showinfo("Sin datos", "Aún no se han registrado encuestas")
        return

    resultados = ""
    for materia in materias:
        encuestas_materia = filtrar_encuestas_por_materia(materia)
        if encuestas_materia:
            estadisticas = obtener_estadisticas(encuestas_materia)
            resultados += f"\n=== {materia.upper()} ===\n"
            resultados += formatear_resultados(estadisticas)
    messagebox.showinfo("Resultados Generales por Asignatura", resultados)

# Muestra los resultados individuales de un alumno:
# Pide el nombre del alumno con simpledialog.
# Filtra todas sus encuestas.
# Agrupa sus resultados por materia.
# Calcula estadísticas solo para ese alumno.
# Muestra los resultados por materia.
def ver_resultados_individuales():
    if not encuestas:
        messagebox.showinfo("Sin datos", "Aún no se han registrado encuestas")
        return

    nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del alumno:")
    if not nombre:
        return

    encuestas_alumno = filtrar_encuestas_por_alumno(nombre)
    if not encuestas_alumno:
        messagebox.showinfo("Sin datos", f"No hay encuestas para {nombre}")
        return

    resultados = ""
    for materia in materias:
        encuestas_materia = list(filter(lambda e, materia=materia: e["materia"] == materia, encuestas_alumno))
        if encuestas_materia:
            estadisticas = obtener_estadisticas(encuestas_materia)
            resultados += f"\n=== {materia.upper()} ===\n"
            resultados += formatear_resultados(estadisticas)
    messagebox.showinfo(f"Resultados de {nombre}", resultados)

# === CONSTRUCCIÓN DE LA INTERFAZ (GUI) ===

# Ventana principal
root = tk.Tk()
root.title("Evaluación de Asignaturas")

# Campo de nombre
tk.Label(root, text="Nombre del alumno:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

# Menú de selección de materia
tk.Label(root, text="Seleccione una materia:").pack()
materia_var = tk.StringVar(root)
materia_var.set(materias[0])
tk.OptionMenu(root, materia_var, *materias).pack()

# Entradas para los aspectos a evaluar
entradas_aspectos = []
for aspecto_local in aspectos:
    tk.Label(root, text=f"{aspecto_local} (1-5):").pack()
    e = tk.Entry(root)
    e.pack()
    entradas_aspectos.append(e)

# Botones de acción
tk.Button(root, text="Guardar evaluación", command=guardar_encuesta).pack(pady=5)
tk.Button(root, text="Ver resultados generales por asignatura", command=ver_resultados_generales).pack(pady=5)
tk.Button(root, text="Ver resultados individuales por alumno", command=ver_resultados_individuales).pack(pady=5)

# Inicia la GUI
root.mainloop()
