"""_____ 4° DIA - 19/05/2023 _____"""


"""MODULO 6 - ESTRUTURAS (REPETIÇÃO E RANGE) - CONTINUAÇÃO"""

    # Revisão ambientes Virtuais
    # Revisão instalação Linux
    
# WHILE
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
 
    # Python don't have do while
    

# BREAK
i = 0
for i in range(1, 11):
    if i == 6:
        break
    else:
        print(i)
print("sai do loop")
print()
      

 
"""MODULO 7 - COLEÇÕES (LISTAS | TUPLAS | DICIONARIOS | MAPAS | CONJUNTOS)"""

# COLEÇÕES SÃO UMA PARTE MUITO IMPORTANTE, POIS É MUITO UTILIZADA EM CIENCIAS DE DADOS, MACHINE LEARNING, IA, BIOTECNOLOGIA(SEQUENCIAMENTO DE DNA) E ANALISE DE DADOS

# LIST
    # Listas em Python funcional como vetores/matrizes (arryas) de outras linguagens, com a diferença de serem *DINAMICAS e também de podermos colocar *QUALQUER tipo de dado.
    
    # - Dinamico: em C ou Java tamanho e tipo fixo
    # - em Python NÃO tem tamanho fixo
    # - em Python listas são representadas usando conchetes []

lista1 = []
lista2 = [1, 2, 3, 4, 5]
lista3 = ["G", "e", "e", "k"]
lista4 = list(range(11))
lista5 = list("Geek University")
lista6 = [1, 99, 50, 2, 1505, 27, 33, 1, 54, 99, 1]
print(lista4)

# Verificar se o valor esta contido na lista
if 4 in lista2:
    print('Encontrei o numero 4')
else:
    print('Não encontrei o numero 4')
    
# Ordenar lista de valores
lista6.sort()
print(f'lista numerica ordenada:  {lista6}') 
    # Duvida? por que não pode fazer print(lista6.sort())
    # Duvida? por que o retorno é none, equivale a null de js ?

# Ordenar lista de string
lista5.sort()
print(lista5)
