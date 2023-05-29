"""_____ 6° DIA - 28/05/2023 (week 2 - total = 13)_____"""
""" 
 MODULOS (LIBS)
 
 - RANDOM (GERAR NUMEROS RANDOMICOS - PSEUDO ALEATÓRIOS)

"""

# EXISTEM DUAS FORMAS DE USAR MODULO OU UMA FUNÇÃO DESTE 

# FORMA 1 - importa o modulo inteiro (não recomendado - todas funçoes ficam ocupando espaço na memoria)
import random

print(random.random())
#     modulo.function()

# FORMA 2 - IMPORTANDO APENAS A FUNÇAO ESPECIFICA DO MODULO (recomendado)
from random import random

for n in range(9):
    print(random())

# REAIS ACIMA DE 1 UNIDADE - uniform(startAt, endBeforeIt)


from random import uniform

for i in range(9):
    print(uniform(3,7))
    
# NUMEROS INTEIROS - randint(startAt, endBeforeIt)
from random import randint

for i in range(6):
    print(randint(1,61), end=', ')
    
# ESCOLHAS NUM INTERVALO - choice(iteravel)

from random import choice
jogadas=  ['papel', 'pedra', 'tesolra']

print(choice(jogadas))

# aceita string
print(choice('Geek University'))

# EMBARALHAMENTO - Shuffle(iteravel)
from random import shuffle

cartas = ['K', 'Q', 'J', '7', '6', '5', '4', '3', '2', 'A']
shuffle(cartas) # não retorna valor, muda o original 
print(cartas)
