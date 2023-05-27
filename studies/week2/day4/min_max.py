"""_____ 4° DIA - 26/05/2023 (week 2 - total = 11)_____"""
""" 
MIN E MAX

 - max() retorna o mairo valor em um iteravel ou o maior de dois ou mais elementos
 
 - min() retorna o menor valor de um iteravel ou o menor de dois ou mais elementos
 
"""

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) # retorn 129

tupla = 1, 8, 4, 99, 34, 129
print(max(tupla)) # retorn 129

set_conjunto = {1, 8, 4, 99, 34, 129}
print(max(set_conjunto)) # retorn 129

dictionary = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dictionary.values())) # retorn 129
print(max(dictionary)) # retorn f (pois pega o max pela KEY não pelo VALUE)



# FAÇA UM PROGRAMA QUE RECEBE DOIS VALORES DE USUARIO E MOSTRE O MAIOR DELES
[value1, value2] = [int(input("digite um numeros: ")), int(input("digite outro numeros: "))]
print(f'O maior numero digitado foi: {max(value1, value2)}')

# NUMERO DE CARACTERES STRING
print(max('a', 'abc', 'abcde', 'ABC'))

# VALOR NA LISTA DE CARACTERES ALFANUMERICOS
print(max('a', 'b', 'h', 'z'))

# mesmo de antes, funciona com strings de multiplos char
print(max('Geek University'))

# COM ARRAY DE NOMES CONSIDERA A INICIAL NA LSTA ALFANUMERICA

# PEGANDO PELO TAMANHO DO NOME
nomes = ['Arya', 'Ka', 'Tim', "Olivieira", 'Zed']
print(max(nomes, key=lambda nome: len(nome))) # retorna maior string
print(min(nomes, key=lambda nome: len(nome))) # retorna menor string

# DESAFIO PEGAR LISTA DE MUSICA, RETORNAR A MAIS TOCADA E MENOS TOCADA, APENAS APRESENTANDO O TITULO DA MUSICA

musicas = [
    {'Titulo':'Neffex','Album': 'unknow','Tocou': 2, 'Favorit': True},
    {'Titulo':'Annita','Album': 'unknow', 'Tocou': 1, 'Favorit': False},
    {'Titulo':'Beyonce','Album': 'unknow', 'Tocou': 20, 'Favorit': False},
    {'Titulo':'Shakira','Album': 'unknow', 'Tocou': 56,'Favorit': True},
    {'Titulo':'Akon','Album': 'unknow', 'Tocou': 18, 'Favorit': True},
    {'Titulo':'Eminem','Album': 'unknow', 'Tocou': 100,'Favorit': True}
]

# SOLUÇÃO 1 MAIS TOCADA
print((max(musicas, key=lambda musica: musica['Tocou']))['Titulo'])

# SOLUÇÃO 2 MAIS TOCADA
print((max(musicas, key=lambda musica: musica['Tocou'])).get('Titulo'))

# SOLUÇÃO 3 evitando erro se não tiver titulo MAIS TOCADA
print((max(musicas, key=lambda musica: musica['Tocou'])).get('Titulo', 'Titulo não encontrado')) 



# SOLUÇÃO 1 MENOS TOCADA
print((min(musicas, key=lambda musica: musica['Tocou']))['Titulo'])

# SOLUÇÃO 2 MENOS TOCADA
print((min(musicas, key=lambda musica: musica['Tocou'])).get('Titulo'))

# SOLUÇÃO 3 evitando erro se não tiver titulo MENOS TOCADA
print((min(musicas, key=lambda musica: musica['Tocou'])).get('Titulo', 'Titulo não encontrado')) 

# Retorna em forma de lista apenas os Titulos
print(list([music['Titulo'] for music in musicas]))

# DESAFIO 2 COMO ENCONTRAR A MUSICA MAIS TOCADA E MENOS TOCADA SEM MAX SEM MIN E SEM LAMBDA

max_tocada = 0
title = ''
for element in musicas:
    if element['Tocou'] > max_tocada:
        max_tocada = element['Tocou']
        title = element['Titulo']

print(f'A musica MAIS tocada sem MAX,MIN,LAMBDA é: {title}, e Tocou: {max_tocada}')

# DESAFIO 2 COM MENOS TOCADA
min_tocada = ''
title = ''
for element in musicas:
    if musicas[0] == element:
        min_tocada = element['Tocou']
        
    if element['Tocou'] < min_tocada:
        max_tocada = element['Tocou']
        title = element['Titulo']

print(f'A musica MENOS tocada sem MAX,MIN,LAMBDA é: {title}, e Tocou: {min_tocada}')
