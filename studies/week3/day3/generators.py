"""_____ 3° DIA - 01/06/2023 (week 3 - total = 17)_____"""
""" 
 GENERATORS
 
    TODO GENERATOR É UM ITERATOR, MAS NEM TODO ITERATOR É UM GENERATOR
    
    GENERATORS PODEM SER CRIADOS COM FUNÇOES GERADORAS:
        UTILIZAM A PALAVRA RESERVADA yield
    
    GENERATORS PODEM SER CRIADOS COM EXPRESSÕES GERADORAS
    
DIFERENÇAS COM FUNÇÕES COMUM
    
__________________________________________________________________
| Function                        | Generator Function           |
__________________________________________________________________
| return                          | yield                        |
__________________________________________________________________
| retrun apenas uma vez           | multiplas vezes              |
__________________________________________________________________
| executada, return valor         | executada, retorna generator |
------------------------------------------------------------------
"""

# EXEMPLO DE FUNÇÃO GERADORA


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(5)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
