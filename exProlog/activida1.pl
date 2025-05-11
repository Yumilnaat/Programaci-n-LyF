%hechos que representan el arbol
mujer(rosa).
mujer(paloma).
mujer(fabiola).
mujer(susuki).

madre(rosa, paloma).
madre(rosa, fabiola).
madre(rosa, susuki).

%Datos sobre empleados
empleado(juan, 35, ingeniero).
empleado(maria, 28, analista).
empleado(pedro, 40, gerente).

%Pregunta y respuesta
saludo_respuesta(Saludo) :-
    member(Saludo, ["Hola", "Como estas?", "Buenos dias", "Que tal?"]),
    responder_saludo(Saludo).

%Regla auxiliar para responder a saludos específicos
responder_saludo("Hola") :-
    write('¡Hola! ¿En qué puedo ayudarte?'), nl.
responder_saludo("Como estas?") :-
    write('Estoy bien, gracias por preguntar.'), nl.
responder_saludo("Buenos dias") :-
    write('¡Buenos días! ¿Cómo puedo ayudarte hoy?'), nl.
responder_saludo("Que tal?") :-
    write('Todo bien, ¿y tú?'), nl.
responder_saludo(_) :-
    write('Lo siento, no entendí tu saludo.'), nl.
