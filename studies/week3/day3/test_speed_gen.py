"""_____ 3° DIA - 01/06/2023 (week 3 - total = 17)_____"""
import time
""" 
TESTE DE VELOCIDADE COM GENERATOR
"""

# GENERATOR EXPRESSION - CONTANDO ATÉ 1 BILHÃO
gen_init = time.time()
print(sum(num for num in range(1000000000))) # 1 BILHÃO
gen_finished = time.time()


# LIST COMPREHENSION - CONTANDO ATÉ 100 MILHÕES
list_init = time.time()
print(sum([num for num in range(1000000000)])) # 1 BILHÃO
list_finished = time.time()

print(f'Generator Tempo: {(gen_finished - gen_init):.2f} segundos')
print(f'List Comprehension Tempo: {(list_finished - list_init):.2f} segundos')
