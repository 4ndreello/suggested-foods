"""
Authors: 
    Gabriel Andreello (202210183)
    Ricardo Altever Lessa (202210295)
    Henrique Scudeller (202210324)
    Lauren Gabrielle Fogaça (202210184)

Dependencies:
    pyswip
    prolog-8.4.3 (https://www.swi-prolog.org/download/stable/bin/swipl-8.4.3-1.x64.exe.envelope)
"""

from pyswip import Prolog
prolog = Prolog()

def comidas_possiveis(pessoa):
    prolog.consult("preferencias.pl")  

    comidas = []
    for solucao in prolog.query("comidas_possiveis({}, Comida)".format(pessoa)):
        comidas.append(solucao["Comida"])

    return comidas

def sugerir_restaurante(pessoa):
    prolog.consult("preferencias.pl") 

    restaurantes_sugeridos = []
    for solucao in prolog.query("sugerir_restaurante({}, Restaurante)".format(pessoa)):
        restaurantes_sugeridos.append(solucao['Restaurante'])

    return restaurantes_sugeridos

# Exemplo de uso
pessoa = "joao"

restaurantes_sugeridos = sugerir_restaurante(pessoa)
comidas = comidas_possiveis(pessoa)

if comidas:
    print("Comidas possíveis para {}: {}".format(pessoa, comidas))
else:
    print("{} não tem uma comida preferida registrada.".format(pessoa))

if restaurantes_sugeridos:
    print("Restaurantes sugeridos para {}: {}".format(pessoa, restaurantes_sugeridos))
else:
    print("Não há restaurantes sugeridos para {} com base nas preferências alimentares.".format(pessoa))

