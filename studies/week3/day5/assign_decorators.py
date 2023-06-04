"""_____ 5° DIA - 02/06/2023 (week 3 - total = 19)_____"""

"""
    (MODULE) DECORATORS

    2 - COM DIFERENTES ASSINATURAS EM DECORADORES
        DECORATOR PATTERN (RESUMO: USAR *args **kwargs)
"""


"""
# NORMAL 
def gritar(func):
    def aumentar(nome):
        return func(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostatria de {principal}, acompanhado de {acompanhamento}, por favor.'


# print(ordenar('Picanha', 'Batata Frita'))
# ERRO POIS DECORATOR RECEBE APENAS 1 PARAMETRO

"""

# REFATORADO COM DECORATORS PATTERN


def gritar(func):
    def aumentar(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


print(saudacao('Alice'))
print(ordenar('Bisteca', 'Macarrão'))


# COM PARAMETROS DE ENTRADA

def verifica_primeiro_argumento(valor):
    def interna(func):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return func(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(5,20))