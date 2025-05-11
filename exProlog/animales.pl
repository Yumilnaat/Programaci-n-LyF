% --- Hechos sobre las características físicas de los animales ---
tiene(pelaje, fido).    % Fido tiene pelaje
tiene(pelaje, misifu).  % Misifu tiene pelaje
tiene(plumas, piolin).  % Piolín tiene plumas

% --- Hechos sobre el comportamiento de los animales ---
ladra(fido).            % Fido ladra
maulla(misifu).         % Misifu maúlla
vuela(piolin).          % Piolín vuela

% --- Reglas para determinar el tipo de animal basado en sus propiedades ---
tipo(perro) :- tiene(pelaje, X), ladra(X).     % Un animal es un perro si tiene pelaje y ladra
tipo(gato) :- tiene(pelaje, X), maulla(X).     % Un animal es un gato si tiene pelaje y maúlla
tipo(pajaro) :- tiene(plumas, X), vuela(X).    % Un animal es un pájaro si tiene plumas y vuela
