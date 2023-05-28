"""_____ 6° DIA - 28/05/2023 (week 2 - total = 13)_____"""
""" 
 RAISE
 
 Levantando os proprios erros com Raise. 
 - É uma palavra reservada do python.
 - criar mensagens personalizadas de erros para nossos codigos e bibliotecas
 
 - forma geral de utilização:
 raise TipoDeErro('mensagem personalizada para o erro')
 
 * PARECIDO COM CONSOLE.ERROR() JS
 * LANÇAR ERRO É LANÇAR EXCESSÃO 
 
"""

def set_color(texto, cor):
    cores = {'verde', 'amarelo', 'azul'}
    if type(texto) is not str:
        raise TypeError('O primeiro argumento "texto" deve ser uma string')
    if type(cor) is not str:
        raise TypeError('O segundo argumento "cor" deve ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto: {texto} sera impresso na cor: {cor}')

set_color('True', 'vermelho') # cai no raise

# NADA APOS O RAISE É EXECUTADO (IGUAL O RETURN)