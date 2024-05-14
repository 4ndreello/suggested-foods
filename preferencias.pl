% Preferências de comida
gosta_de(joao, pizza).
gosta_de(joao, sushi).
gosta_de(joao, carne).
gosta_de(maria, sushi).
gosta_de(pedro, lasanha).
gosta_de(ana, salada).
gosta_de(ana, tomate).
gosta_de(lucas, frutas).
gosta_de(carla, tofu).

% Preferências de dieta
vegetariano(joao).
vegetariano(ana).
vegano(ana).
vegano(lucas).

% Restrições alimentares
alergico(maria, camarao).
alergico(ana, tomate).
alergico(pedro, lactose).

% Restaurantes e tipos de cozinha
restaurante(pizzaria, italiana).
restaurante(sushi_bar, japonesa).

% Pratos servidos em cada restaurante
prato(pizzaria, pizza).
prato(sushi_bar, camarao).
prato(sushi_bar, sushi).

% Regra para determinar as comidas possíveis para uma pessoa
comidas_possiveis(Pessoa, Comida) :-
    gosta_de(Pessoa, Comida),
    \+ alergico(Pessoa, Comida),
    \+ (vegetariano(Pessoa), Comida = carne),
    \+ (vegano(Pessoa), (Comida = carne ; Comida = laticinios)).

% Regra para sugerir restaurantes com base nas preferências de comida
sugerir_restaurante(Pessoa, Restaurante) :-
    gosta_de(Pessoa, Comida),
    prato(Restaurante, Comida),
    \+ alergico(Pessoa, Comida),
    \+ (vegetariano(Pessoa), Comida = carne),
    restaurante(Restaurante, _).