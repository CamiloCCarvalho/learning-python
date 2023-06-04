"""_____ 5° DIA - 03/06/2023 (week 3 - total = 19)_____"""

"""
    (MODULE) DECORATORS
    
    1 - FUNÇÕES DE MAIOR GRANDEZA (IGUAL JS)
            HIGH ORDEM FUNCTIONS 
                - RETORNAM OUTRAS FUNÇÕES. 
                - PODEMOS PASSAR OUTRAS FUNÇÕES COMO ARGUMENTOS
                - CRIAR VARIAVEL RECEBENDO FUNÇÕES COMO VALOR
                
                
    2 - EM PYTHON, FUNÇÕES SÃO CIDADÕES DE PRIMEIRA CLASSE
        First Class Citizen
            (funções de maior grandeza / high ordem functions)
        
    3 - NESTED FUNCTIONS (FUNÇÕES ANINHADAS IGUAL JS) (INNER FUNCTIONS)
"""
from random import choice

def somar(a:int, b:int):
    return int(a) + int(b)


def subtrair(a:int, b:int):
    return int(a) - int(b)


def multiplicar(a:int, b:int):
    return int(a) * int(b)


def dividir(a:int, b:int):
    return float(a) / float(b)


def calcular(num1, num2, func):
    return func(num1, num2)


print(calcular(10, 5, multiplicar))


# NESTED FUNCTIONS (INNER FUNCTIONS)

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Alice '))


# RETORNANDO FUNÇÕES DE OUTRAS FUNÇÕES


def faz_me_rir():
    def rir():
        return choice(('hahaha', 'kkkkk', 'yayyayaya'))
    return rir


rindo = faz_me_rir()

print(rindo())
