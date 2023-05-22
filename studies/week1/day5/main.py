"""_____ 5° DIA - 20/05/2023 _____"""

# TAMBÉM FEITO ALGUNS EXERCICIOS
    # EX MODULO 4
    # EX MODULO 5



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

# Contar itens repetidos na lista
qtLetterE = lista5.count('e')
print(f'Contamos: {lista6.count(1)} , numeros (1) nesta lista.')
print(f'Contamos: {qtLetterE} , letras (E) nesta lista.')

# Adicionar elementos em listas com append (add end)

lista1.append(33) # Adiciona apenas 1 elemento por vez
lista1.append('Tria')
print(f'Lista com append: {lista1}')

# Lista com sublista
lista1.append([1, 2, 3])
print(f'Lista de Lista com append: {lista1}')

if [1, 2, 3] in lista1:
    print(f'Encontrei a lista procurada')
else:
    print('Lista não encontrada')

# Adicionando elementos SEM SER SUBLISTA
lista1.extend([99, 999, 9999])
print(lista1) # IMPORTANTE! só aceita iteraveis, não aceita valor unico

lista1.extend('Geek')
print(lista1)

# Adicionando com insert passando index
lista1.insert(2, 'Add via insert com Index')
print(lista1)

# Concatenando listas
lista7 = lista3 + lista5 # parecido com extend, porem criando a nova lista em outra variavel
print(lista7)

# Invertendo lista
lista3.reverse()
print(f'Lista invertida com reverse: {lista3} | não retonra nova lista, muda a original')
print(lista3[::-1]) # Mesmo efeito do reverse()

# Copiar lista
lista8 = lista3.copy() # Duvida? Por que usar copy e não atribuir direto ?

# Deletar ultimo elemento
# lista.pop() retorna o elemento retirado

# Deletar passando index
# lista.pop(2) indica o index a ser removido

# Tamanho da lista
# lista.len()

# Repetir listas com multiple
# lista = lista * 3

# Padrão split
# lista = lista.split() ira separar baseado no espaço entre palavras
# lista = lista.split(',') muda o padrão a ser usado para separar elementos

# Convertendo uma lista em string denovo 
# lista = ' '.join(lista)
# lista = '$'.join(lista) mudando o comportamento default

# OBS.: pode usar o for na lista
# OBS.: pode usar o while na lista

# INDICES negativos, percorre de tras pra frente a lista

# da pra passar enumerate dentro da lista
# lista = list(enumerate(lista)) gerando os pares de index e valor

# ENCONTRAR INDEX DO ELEMENTO
# lista.index(element) 
    # RETORNA O PRIMEIRO ELEMENTO ENCONTRADO
    # SE NÃO TIVER O ELEMENTO RETORNA UM ValueError

# lista.index(element, startAt)
# list.index(element, startAt, endAt) conferir se não é endBeforeAt

# REVISÃO SLICE
# lista[ start : endBeforeAt : step ]
# range( start: endBeforeAt: step )
