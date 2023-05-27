"""_____ 4° DIA - 26/05/2023 (week 2 - total = 11)_____"""
""" 
SORTED

 - não confundir com sort(), sort() só funciona com lista
 
 - sorted() funciona com qualque iteravel
 
"""

# sort() de LISTAS
lista = [2,5,3,4,1]
lista.sort()  # ALTERA A LISTA ORIGINAL NÃO GERA UMA NOVA E NÃO RETORNA VALORES
print(lista)

# sorted
lista2 = [5,6,4,12,1] # PODE SER SET, TUPLE, QUALQUER ITERAVEL
print(lista2)
print(sorted(lista2)) # RETORNA SEMPRESS RETORNA LISTA E NÃO MUDA A ORIGINAL 
print(lista2)

# PARAMETROS
numeros = (2,5,4,2,3,5,1,5,6,8)
print(numeros)
print(sorted(numeros, reverse=True)) # Decrescente

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


# ORDENANDO PELO USERNAME, CASESENSITIVE
print(sorted(usuarios, key=lambda user: user['username']))
print()


# ORDENANDO PELO NUMERO DE TWEETS
print(sorted(usuarios, key=lambda user: len(user['tweets'])))

# EXEMPLO MUSICAS MAIS E MENOS TOCADAS

musicas = [
    {'Titulo':'Neffex','Album': 'unknow','Tocou': 2, 'Favorit': True},
    {'Titulo':'Annita','Album': 'unknow', 'Tocou': 1, 'Favorit': False},
    {'Titulo':'Beyonce','Album': 'unknow', 'Tocou': 20, 'Favorit': False},
    {'Titulo':'Shakira','Album': 'unknow', 'Tocou': 56,'Favorit': True},
    {'Titulo':'Akon','Album': 'unknow', 'Tocou': 18, 'Favorit': True},
    {'Titulo':'Eminem','Album': 'unknow', 'Tocou': 100,'Favorit': True}
]

# ordenando pela mais tocada
print(sorted(musicas, key=lambda music: music['Tocou'], reverse=True))

# ordenando pela menos tocada
print(sorted(musicas, key=lambda music: music['Tocou']))
