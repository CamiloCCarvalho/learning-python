from fractions import Fraction

"""_____ 1° DIA - 16/05/2023 _____"""

"""
ESTUDO COMPLETO DE PYTHON

    MODULO 1 - APRESENTAÇÃO DO CURSO
    MODULO 2 - PREPARANDO O AMBIENTE
    MODULO 3 - INTRODUÇÃO A LINGUAGEM
    
        PEP8 - Boas Praticas
        Dir e Help
        dir(variable) ex: dir(name)
            lista todos metodos e propriedades que pode usar com esse tipo de dado
        help(command) ex: help(print)
"""


"""_____ 2° DIA - 17/05/2023 _____"""

# STRINGS WITH FORMATs

message:str = 'World'
print(f"Hello {message}") # python3.6+
print('''Hello %s''' % message) # similar to c (language)
print("Hello {}".format(message)) # method of class str
print ("Hello World") # normal string
print(message[::-1]) # *OBS1
print(message[0:3]) # slice() return "Wor" (startAt : endBeforeThis)
print(message.replace('W', 'U')) # swap in string W by U (allIndexs & caseSensitive)

    # OBS.:
     # 'this is string' | "this is string" | '''this is string'''
     # """ this is string multiple lines AND comment without var/function"""
     # upper() return FOO
     # lower() return foo
     # split() return ["foo", "bar"]
     # split()[index] return elementOfIndex
     # *OBS1 [::-1] -> (: start index0) & (: end indexLast) & (-1 run inverse)

# Professor problem to reverse without [::-1] solved:
newMessage = list(message)
newMessage.reverse()
print(''.join(newMessage))



"""MODULO 4 - TIPOS DE VARIAVEIS"""

# NUMBER WITH FORMATS
num1:int = 10 # int
num2:float = 4.5 # float
num3 = Fraction(3, 4) # return 3/4 (Class Fraction)
num4 = Fraction(4.5) # return 9/2
num5 = Fraction('3/4') # return 3/4
num6 = int(num2) # casting
num7 = num1 / 3 # return float (int/int --> infers result float)
    
    # OBS.:
     # your RAM is the limit!
     # numbers not have limit in python (different of Java 2^63 and 1bit to assign)
     # fraction return a literal division to stay more precise result
     # Python infers what's the type of result and return it

# BOOLEAN
isFemale:bool = True
isMarried:bool = False
isMale:bool = not False # return True

    # OBS.:
     # true table


# ESCOPE
number:int = 5
if number > 3:
    newNumber = number + 10
    print(f"number GlobalScope:{number} | number localScope:{newNumber}")


"""_____ 3° DIA - 18/05/2023 _____"""

"""MODULO 5 - ESTRUTURAS (LOGICA E CONDICIONAL)"""

# IF, ELSE, ELIF
age:int = 17
if age < 18:
    print(f'\nA pessoa MENOR de idade, tem: {age} anos')
elif age == 18:
    print(f'A pessoa acabou de fazer 18 anos')
else:
    print(f'A pessoa é maior de idade!')
    
# AND, OR, NOT, IS
if num1 > 5 and num2 > 5:
    print('comparação com AND: ambos numeros são maior que 5')
elif num1 > 5 or num2 > 5:
    print('comparação com OR: pelo menos um dos argumentos é maior que 5')
elif not num1 > 5:
    print('comparaçao com NOT (negação): mente que numero NÃO é ou não maior que 5, sempre o oposto')
elif num1 is num2:
    print('comparação com IS: retorna verdadeiro somente se variavel/objeto forem o mesmo na memoria')
print()


    
"""MODULO 6 - ESTRUTURAS (REPETIÇÃO E RANGE)"""

# FOR
name: str = 'Geek University'
lista: list = [1, 3, 5, 7, 9]

#exemplo iterando string
for caract in name: #percorre o iteravel inteiro
    print(caract)
print()

#exemplo iterando em range
for i in range(1, 10): #percorre um range  usando (startAt, endBeforeIt)
    print(i)
print()

#exemplo iterando lista
for number in lista:
    print(number)
print()


# ENUMERATE

#exemplo com enumerate (generate simillar tupla)
for keyIndex, keyValue in enumerate(name):
    print(f'Key: {keyIndex} | ValueAt: {keyValue}')

#possivel ignorar argumentos
for _, keyValue in enumerate(name):
    print(f'keyValue: {keyValue}')

for itemKey in enumerate(name):
    print(f'index0: {itemKey[0]}')
    
for itemEnumarate in enumerate(name):
    print(f'pair: {itemEnumarate}')

for itemValue in enumerate(name):
    print(f'index1: {itemValue[1]}')
print()

    # TIP: IN PYCHAMR CTRL+CLICK JUMP TO DOCUMENTATION CODE WITH IT


# RANGE
    # Use General: generate numbers sequence, not random
    # Increment is default of 1 in 1 | start default 0

# form 1
print('RANGE FORMA 1')
for numb in range(11): # define just: (endBeforeIt)
    print(numb)
print()

# form 2
print('RANGE FORMA 2')
for numb in range(1, 11): # define: (startAt, endBeforeIt)
    print(numb)
print()

# form 3
print('RANGE FORMA 3')
for numb in range(5, 50, 5): # define: (startAt, endBeforeIt, increment)
    print(numb)
print()

# form 4
print('RANGE FORMA 4 (INVERSE)')
for numb in range(20, -1, -5): # define: (endBeforeIt, startAt, decrement)
    print(numb)
print()
    
# generate list with range
newList = list(range(10))
print(f'Lista gerada com Range: {newList}')

    
    
"""_____ 4° DIA - 19/05/2023 _____"""

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


"""_____ 5° DIA - 20/05/2023 _____"""

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

# EXERCICIOS MODULO 4 E 5


"""_____ 6° DIA - 21/05/2023 _____"""

# lista[::-1] 

# INVERTENDO ORDEM DOS ELEMENTOS
# lista[0], lista[1] = lista[1], lista[0] similiar a usar reverse, invertendo os elementos

# COM NUMEROS
# sum(lista) soma de todos elementos
# max(lista) retorna o maior numero
# min(lista) retorna o menor valor
# len(lista) retorna o tamanho da lista

# DESEMPACOTAMENTO DE LISTA (precisam ter o mesmo numero de variaveis)
# lista = [1,2,3]
# num1, num2, num3 = lista    similiar a desestruturação por associação no JS

# DEEP COPY
# usando copy() a lista copiada não afeta a original 

# SHALLOW COPY
# lista= [1,2,3]
# novalista = lista
# novalista.append(4)
    # COPIA VIA ATRIBUIÇÃO AFETA A ORIGINAL


# TUPLE
    # TUPLAS SÃO REPRESENTADAS POR PARENTESES
    # TUPLAS SÃO IMUTAVEIS
    # TODA OPERAÇÃO EM TUPLA GERA UMA NOVA TUPLA

# tuple1 = (1,2,3)  is tuple
# tuple2 = 1,2,3    is tuple
# tuple3 = (5)      isn't tuple (is int)
# tuple4 = (5,)     is tuple
# tuple5 = 5,       is tuple
    # TUPLAS SÃO DEFINIDAS PELA VIRGULA E NÃO PELO PARENTESES

# GERANDO TUPLA COM RANGE
# tuple = tuple(range(11))

# DESEMPACOTAMENTO DE TUPLA
# tuple = ('Geek University', 'Curso essencial Python')
# school, course = tuple

# NÃO POSSUI METODOS DE ADD E REMOVE (É IMUTAVEL)

# sum(tuple)
# max(tuple)
# min(tuple)
# len(tuple)
# tuple.count(element)
# school = tuple('Geek University')
# tuple[2] return value of index
# tuple.index(element) return index of it element
# pode usar for e while normal
# tuple[::] slicing igual na list


# USO EM CASOS QUE NÃO PRECISAMOS MUDAR OS DADOS CONTIDOS EM UMA COLEÇÃO
    # EXEMPLO:
        # MESES DO ANO
        # DIAS DA SEMANA
    
# CIENCIA DE DADOS, BIG DATA
    # USO DE TUPLAS É MAIS RAPIDO
    # DEIXAM O CODIGO MAIS SEGURO


# EM TUPLAS NÃO TEMOS O PROBLEMA DE SHALLOW COPÝ


# DICTIONARY (DICT)

countrys = {'br':'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'} # comum recomendado
otherCountrys = dict(br='Brasil', eua='Estados Unidos', py='Paraguai') # incomum

# ACESSANDO ELEMENTOS

# FORMA 1 - VIA CHAVE (IGUAL LISTA E TUPLA)
print(countrys['br'])

# print(countrys['test']) return KeyError

    
# FORMA 2 - VIA GET (RECOMENDADO)
print(countrys.get('br'))
print(countrys.get('test')) # return type None (sempre é False)

# Caso não tenha pode colocar valor default
country = countrys.get('ru', 'Não encontrado') # get('key', 'value default if not exists')

print('br' in countrys) # True
print('ru' in countrys) # False
print('Estados Unidos' in countrys) # False (só busca pela chave)


# ADICIONANDO ELEMENTOS NO DICT (Comum)
receita = { 'jan': 400, 'fev': 500, 'mar': 250}
receita['abr'] = 350
print(receita)

# ADICIONANDO FORMA 2
new_data = {'mai': 100}
receita.update(new_data)
print(receita)

# ATUALIZANDO DADOS DICT
receita['mai'] = 5050

# RETIRANDO ELEMENTOS (se não tiver retorna KeyError)
receita.pop('mai') # RETURN value .Obrigatório passar chave
del receita['fev'] # também deleta mas não retorna

# METHODOS
# receita.clear() limpa por inteiro
# receita.copy() Deep Copy
# novaReceira = receita Shallow Copy
# fromkeys(iteravel, value)


# FORMA NÃO USUAL DE CRIAR DICIONARIO
outro = {}.fromkeys('a', 'b') 


#         createDict ([         keys(iteravel)           ] ,    value    ) 
usuario = {}.fromkeys(['nome', 'idade', 'email', 'perfil'], 'Não Definido')
print(usuario)

# pode usar inclusive o range
# {}.fromkeys(range(1,11), 'default value')


# MAP

# LOOPS COM DICT
for chave in receita:
    print(chave)
    
for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f' {chave} : {receita[chave]}')
    
# ACESSANDO TODAS CHAVES
print(receita.keys())

# RECOMENDADO
for chave in receita.keys():
    print(receita[chave])
    
    
# ACESSANDO TODOS VALUES
print(receita.values())

# RECOMENDADO
for value in receita.values():
    print(value)


# DESENPACOTAMENTO DE DICIONARIOS
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# sum(receita.values())
# max(receita.values())
# min(receita.values())
# len(receita)


# CONJUNTO
    # NÃO TEM VALORES DUPLICADOS
    # NÃO TEM CHAVES, APENAS VALORES
    # NA DECLARAÇÃO/ATRIBUIÇÃO IGNORA REPETIÇOES
    
s = {1,2,3,4,5,6,2,5,1,8}
print(s)
print(type(s))

# CONFERIR SE ESTA CONTIDO NO CONJUNTO 

if 3 in s:
    print('este numero esta contido')
else:
    print('este numero NÃO esta contido')
    
    # LISTA ACEITA VALORES DUPLICADOS
    # TUPLAS ACEITAM VALORES DUPLICADOS
    # DICIONARIOS NÃO ACEITA CHAVES DUPLICADAS, VALORES SIM
    # CONJUNTOS NÃO ACEITAM DUPLICADOS, SÓ TEM VALORES
    # CONJUNTOS NÃO GERAM NUMEROS EM ORDEM
    # CONJUNTOS SÃO MUTAVEIS
    # TODOS CONJUNTOS PODEM MISTURAR DADOS
    # POSSIVEL ITERAR NORMALMENTE EM CONJUNTOS
    
# USO DE SETS
    # EXEMPLO:
        # VISITANTE NUM MUSEU

cidades = ['cuiaba', 'campo grande', 'sao paulo', 'cuiaba', 'belo horizonte', 'sao paulo']

# total de visitas
print(len(cidades))

# para saber o numero de cidades distintas 
print(len(set(cidades)))

# METHODS
# s.add(variable) - se ja tiver só ignora sem erros
# s.remove(variable) - se não tiver, Error keyError (Não retorna o que tirou)
# s.discard(variable) - se não tiver, só ignora sem erros
# s.copy() - Deep Copy
# s.clear() - limpa o conjunto inteiro

# METHODS MATH
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ellen', 'Pedro', 'Patricia'}

# SABER OS UNICOS
# FORMA 1 - USAR UNION (MATH)

unicos1 = estudantes_python.union(estudantes_java) # RECOMENDADO
print(unicos1)

# FORMA 2 -  USAR CARACTERE PIPE | (UNION)
unicos2 = estudantes_python | estudantes_java # ESSE É MAIS LEGAL
print(unicos2)


# SABER OS QUE CURSAM AMBOS
# FORMA 1 - USAR INTERSECTION
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# FORMA 2 - USANDO & (E COMMERCIAL)
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# SABER APENAS OS QUE PARTICIPAM DE UM UNICO CURSO
so_python = estudantes_python.difference(estudantes_java)
so_java = estudantes_java.difference(estudantes_python)
print(so_python)
print(so_java)


# sum(set)
# max(set)
# min(set)
# len(set)

