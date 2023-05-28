"""_____ 6° DIA - 28/05/2023 (week 2 - total = 13)_____"""
""" 
 DEBBUGGIN
 
 TEM COMO FAZER PELO PYCHARM, VSCODE, E PELO PROPRIO PYTHON
 
 IMPORTANDO A LIB PDB - Python DeBugger

"""
# COMANDOS PDB
# l (list - lista o codigo e onde estamos)
# c (continue - continua o codigo parando o debug)
# n (next - proxima linha no debugg)
# p (print - imprime a variavel) - em caso de variavel ter mesmo nome dos comandos


# import pdb; pdb.set_trace() # só 3.6- (3.7+ é built-in)
breakpoint()
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
