% Zonas definidas
zona(norte).
zona(sur).
zona(este).
zona(oeste).

% Hechos específicos por zona
humedad(norte, baja).
humedad(sur, media).
humedad(este, alta).
humedad(oeste, baja).

temperatura(norte, 35).
temperatura(sur, 29).
temperatura(este, 31).
temperatura(oeste, 33).

hora(norte, 20).
hora(sur, 9).
hora(este, 12).
hora(oeste, 7).

probabilidad_lluvia(norte, false).
probabilidad_lluvia(sur, true).
probabilidad_lluvia(este, false).
probabilidad_lluvia(oeste, false).

% Tipo de riego por zona (opcional, para recomendaciones)
tipo_riego(norte, goteo).
tipo_riego(sur, aspersion).
tipo_riego(este, manual).
tipo_riego(oeste, goteo).

% Umbral de temperatura extrema (se puede ajustar por zona)
umbral_calor(32).

% Reglas generales

hora_adecuada(Zona) :-
    hora(Zona, H), (H < 10 ; H > 18).

alerta_calor(Zona) :-
    temperatura(Zona, T),
    umbral_calor(Umbral),
    T >= Umbral.

activar_riego(Zona) :-
    humedad(Zona, baja),
    probabilidad_lluvia(Zona, false),
    hora_adecuada(Zona).

estado_riego(Zona, 'Activado') :-
    activar_riego(Zona).
estado_riego(Zona, 'Desactivado') :-
    \+ activar_riego(Zona).

recomendacion(Zona) :-
    activar_riego(Zona),
    alerta_calor(Zona),
    tipo_riego(Zona, Tipo),
    format('Alerta: riego activado con temperatura extrema en la zona ~w. Considere riego por la noche o con sistema ~w.~n', [Zona, Tipo]).

recomendacion(Zona) :-
    format('Zona ~w: Sin recomendaciones especiales para el riego.~n', [Zona]).
