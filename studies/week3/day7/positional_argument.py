"""_____ 7° DIA - 05/06/2023 (week 3 - total = 21)_____"""

"""
    ARGUMENTO POSICIONAL
        -> Algumas funções recebem um parametro passado como argumento,
        porem não podemos usar o recurso de passar argumentos nomeados.
         Este é o ARGUMENTO POSICIONAL

        -> Ja esta ai a muito tempo, porem podemos criar funções desse tipo agora:
            def my_func(arg, /):
                return arg
"""


# EXEMPLO
def mostra_nome(nome, /):
    return print(nome)

# TUDO QUE ESTA A ESQUEDA <- DA / É SÓ POSICIONAL
# não pode nomear: (nome='May')


mostra_nome('May')


# INVERSO - OBRIGATÓRIO USO DE NOMEAÇÃO

def cumprimenta(*, nome):
    return f'olá {nome}'


cumprimenta(nome='May Shiranui')

# TODOS ARGS DEPOIS DO * -> DEVEM SER INFORMADO O NOME DO PARAMETRO
