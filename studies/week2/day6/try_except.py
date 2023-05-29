"""_____ 6° DIA - 28/05/2023 (week 2 - total = 13)_____"""
""" 
 BLOCO TRY / EXCEPT
 
 Conhecido como Try / Cacth em outras linguagens
 
 * PROCURAR SEMPRE TRATAR ERROS DE FORMA ESPECIFICA 
 
"""

# Exemplo: tratando diversos erros de uma vez

try:
    print('geet'[9])
except NameError as err_a:
    print(f'Deu NameError: {err_a}')
except TypeError as err_b:
    print(f'Deu TypeError: {err_b}')
except:
    print(f'Deu um erro diferente')

# TAMBÉM USAR EM FUNÇÕES COMO JÁ É DE COSTUME
