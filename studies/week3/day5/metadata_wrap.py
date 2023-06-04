"""_____ 5° DIA - 02/06/2023 (week 3 - total = 19)_____"""

"""
    (MODULE) DECORATORS

    2 - PRESERVANDO METADADOS E WRAP
    
    -> O problema que costuma ocorrer é com:
    sua_func.__name__
    sua_func.__doc__
        -> usando DECORATOR, ela devolve o name e a doc da função decoradora
        -> talvez o mesmo valha pra arquivos
           MetaDados sobreescrevendo os valores
           
"""

# RESOLVENDO PROBLEMA DE METADADOS SOBREESCRITOS COM WRAPS DE FUNCTOOLS
from functools import wraps


def ver_log(func):
    @wraps(func)
    def logar(*args, **kwargs):
        """Eu sou uma função de log dentro de outra"""
        print(f'Nome da função chamada: {func.__name__}')
        print(f'Documentação da Func chamada: {func.__doc__}')
        return func(*args, **kwargs)
    return logar

@ver_log
def soma(a: int, b: int):
    """Função que soma dois valores INTEIROS"""
    return int(a) + int(b)


soma(10, 20)
print(soma.__name__)
print(soma.__doc__)
