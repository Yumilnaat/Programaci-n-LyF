def registrar_asistencia(nombre, callback): #ejecuta la función enviar_correo() después de registrar la asistencia.
    print(f"Asistencia registrada para {nombre}")
    callback()

def enviar_correo():
    print("Correo de confirmación enviado al estudiante.")

registrar_asistencia("Yumilnaat Poot", enviar_correo)
