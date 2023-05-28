"""_____ 6° DIA - 28/05/2023 (week 2 - total = 13)_____"""
""" 
 BLOCO TRY / EXCEPT / ELSE / FINALLY
 
 * PROCURAR SEMPRE TRATAR ERROS DE FORMA ESPECIFICA 
 
 - DICA DE QUANDO E ONDE TRATAR
    TODA ENTRADA DE DADOS DEVE SER TRATADA
    
    
 --> A MISSÃO DO USUARIO É DESTRUIR SEU SISTEMA
"""

# EM QUAL PARTE DO MEU CODIGO PRECISO TRATAR OS ERROS ?
num = 0
try:
    num = int(input('Digite um numero: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou: {num}')

# USAR ELSE E FINALLY
try:
    num = int(input('Digite um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou: {num}')
finally:
    print('Finally sempre é executado')
    
# finally sempre é executado tendo ou não caido no except
# GERALMENTE UTILIZADO PARA FECHAR OU DESALOCAR RECURSOS, EX: ABRIR CONEXÃO BANCO DE DADOS, ENTÃO USA FINALLY PARA FECHAR ESSA EXECUÇÃO

# FORMA CORRETA DE TRATAR OS ERROS

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except (ZeroDivisionError, TypeError):
        return 'Não é possivel dividir um numero por zero'

num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

print(dividir(num1, num2))
