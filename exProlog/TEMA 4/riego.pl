/**humedad()
temperatura()
hora_adecuada()
probabilidad_lluvia()
*/

% Estado de sensores
humedad(baja).
temperatura(35).
hora(20).
probabilidad_lluvia(false).

% Regla: Es hora adecuada para regar
hora_adecuada :- hora(H), (H < 10 ; H > 18).

% Regla principal: ¿Cuándo se debe activar el riego?
activar_riego :- 
    humedad(baja),
    probabilidad_lluvia(false),
    hora_adecuada.

% Diagnóstico del sistema
estado_riego('Activado') :- activar_riego.
estado_riego('Desactivado') :- \+ activar_riego.

% Regla para alerta de temperatura extrema
alerta_calor :- 
    temperatura(T), 
    T >= 32.

% Mensaje de alerta si se activa el riego con calor extremo
recomendacion :- 
    activar_riego,
    alerta_calor, !,
    writeln('Alerta: riego activado con temperatura extrema. Considere riego por la noche o por goteo').

recomendacion :- 
    writeln('Sin recomendaciones especiales para el riego').
