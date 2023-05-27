"""_____ 3° DIA - 24/05/2023 (week 2 - total = 10)_____"""
""" 
GENERATORS EXPRESSION

 Ja vimos:
    - List Comprehension
    - Dictionary Comprehension
    - Set Comprehension

 Não vimos:
    - Tuple Comprehension, se chama GENERATORS

 - Assim como Map, Filter depois de usar o resultado , se auto deleta
 
"""
from sys import getsizeof

nomes = ['Carlos', 'Camilo', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]   # Ocupa mais recurso em memoria
print(type(res))
print(res)


# Generator
result = (nome[0] == "C" for nome in nomes) # Mais Performatico
print(type(result))
print(result)


# Entendendo melhor uso de memoria 
print(getsizeof('')) # 49 bytes
print(getsizeof('g')) # 50 bytes
print(getsizeof('G')) # 50 bytes
print(getsizeof('Geek')) # 53 bytes
print(getsizeof(0)) # 28 bytes
print(getsizeof(1)) # 28 bytes
print(getsizeof(9)) # 28 bytes
print(getsizeof(20)) # 28 bytes
print(getsizeof(2000000000)) # 32 bytes

# COMPARAÇAO

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

gen = getsizeof(x * 10 for x in range(1000))

print(f'GASTO EM MEMORIA\n LIST COMPREHENSION: {list_comp} bytes\n SET COMPREHENSION: {set_comp} bytes\n DICTIONARY COMPREHENSION: {dict_comp} bytes\n GENERATOR: {gen} bytes')

# PRINCIPAL DIFERENÇA:
    # GENERATOR NÃO GERA OS VALORES, ELE PREPARA PARA GERAR APENAS QUANDO VOCÊ FOR USAR
    # POR ISSO USA TÃO POUCO ESPAÇO
    # OS DEMAIS COMPREHENSION USAM ESPAÇO NA MEMORIA ATÉ O FIM DO PROGRAMA
    