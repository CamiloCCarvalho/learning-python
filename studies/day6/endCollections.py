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
