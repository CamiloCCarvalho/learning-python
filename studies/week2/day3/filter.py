"""_____ 2° DIA - 24/05/2023 (week 2 - total = 8)_____"""
""" 
FILTER

filtras dados de uma determinada collection

"""

import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# mean() -> da lib importada, devolve a media dos valores
media = statistics.mean(dados)

# ASSIM COMO MAP, USA 2 PARAMETROS, FILTER(FUNC, ITERAVEL) 
res = filter(lambda x: x> media, dados)
print(type(res)) # retorna um Obj Filter iteravel
print(f'Media é: {media}')
print(list(res))
# DEPOIS DE USAR O RESULTADO DE FILTER , ELE É APAGADO TAMBÉM


paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)
result = filter(None, paises)
print(list(result))

# EXEMPLO MAIS REALISTA

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas também']},
    {'username': 'Dan', 'tweets': ['Eu adoro pizzas também']},
    {'username': 'Ash', 'tweets': ['Bora programar', 'Codando o dia todo']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Carla', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas também']},
    {'username': 'Julia', 'tweets': []},
    {'username': 'Marcos', 'tweets': []},
    {'username': 'Juliana', 'tweets': ['gosto de cachorros', 'Vou sair hoje']},
    {'username': 'Guh_', 'tweets': ['Eu adoro bolos']},
]

print(usuarios)
# FILTRAR OS USUARIOS QUE ESTÃO INATIVOS NO TWITTER