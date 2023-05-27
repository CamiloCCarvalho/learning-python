"""_____ 5° DIA - 27/05/2023 (week 2 - total = 12)_____"""
""" 
ZIP

 zip() - Cria um iteravel.(zip obj) que agrega elemento de cada um dos iteraveis passados como entrada em pares
 
"""

# EXEMPLOS      - COM DICT
lista1 = [1,2,3]  # KEY
lista2 = [4,5,6]  # VALUE

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# PODEMOS GERAR UM SET, TUPLA , LISTA OU DICIONARIO 
# OS ELEMENTOS SÃO ORGANIZADOS EM DUPLAS SENDO TUPLAS
# DEPOIS DE USAR O RESULTADO ELE É APAGADO DA MEMORIA

print(list(zip1))
zip1 = zip(lista1, lista2)
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))  # só o dicionario que não devolve em formato de tupla de duplo valores
zip1 = zip(lista1, lista2)
print(set(zip1))

# LISTAS DE TAMANHO DIFERENTE
lista3 = ["A", "B", "C", "F", "G", "H"]
# A ORDEM DA LISTA SÓ MUDA A ORDEM DOS ELEMENTOS NA TUPLA, A LISTA REF CONTINUA SENDO A MENOR
print(list(zip(lista1, lista2, lista3))) # IGNORA ELEMENTOS A MAIS SEM PARES DAS DEMAIS LISTAS

# LISTA DE TUPLAS
dados = [(0, 1), (1,2), (2,3), (3,4)]
print(list(zip(*dados)))


# EXEMPLO MAIS COMPLEXO
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
#                                             [(maria, 80, 98), (pedro, 91, 89)]
print(final)

# COM MAP
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final2))
