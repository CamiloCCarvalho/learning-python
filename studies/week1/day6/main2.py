from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque
"""_____ 6° DIA - 21/05/2023 _____"""

# MODULO 7 - COLLECTIONS (AULA( 37:42 ))

# COLLECTIONS - HIGH PERFORMANCE CONTAINER DATATYPES
    # Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com u dicionáro
        # CHAVE -> contem o elemento
        # VALOR -> quantidade de ocorrencias
        

# USO
lista = [1,1,2,1,2,2,3,4,5,6,6,7,7,4,2,1,3] # pode ser qualquer iterável
res = Counter(lista)
print(type(res))
print(res) # Counter({1: 4, 2: 4, 3: 2, 4: 2, 6: 2, 7: 2, 5: 1})


# USO 2
print(Counter('Geek University'))
print()

# USO 3
texto = """Wikipedia is a multilingual, free, online encyclopedia written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and using a wiki-based editing system called MediaWiki. Wikipedia is the largest and most-read reference work in history."""

palavras = texto.split() # lista de palavras
qt_palavras = Counter(palavras) # quantia repetição de palavras
print(qt_palavras)
print()
print(qt_palavras.most_common(5)) # as top 5 que aparecem nesta lista



""" COLLECTIONS - DEFAULT DICT"""
# MUDA O COMPORTAMENTO DO DICIONARIO
    # CRIAR UM DICT DO TIPO DEFAULT
    # NÃO DA ERRO SE KEY NÃO EXISTIR
    # CRIAR NOVO ELEMENTO COM VALOR DEFAULT DE UMA FUNÇÃO LAMBDA
    # A ORDEM DE INSERT DOS ELEMENTOS NÃO É GARANTIDO

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['qualquer']) # no comum KeyError, aqui não 
print(dicionario) # inclui o anterior com valor default do lambda
print()



""" COLLECTIONS - ORDERED DICT"""
# EM UM DICIONARIO A ORDEM DE INSERT DOS ELEMENTOS NÃO É GERANTIDO 
    # GARANTE A ORDEM DE INSERT DOS ELEMENTOS

dicionario2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario2.items():
    print(f'chave: {chave} | valor: {valor}')
    
# DIFERENÇA DO DICT COMUM
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2) # True pois a ordem não importa

# DIFERENÇA DO ORDERED DICT
dict3 = OrderedDict({'a': 1, 'b': 2})
dict4 = OrderedDict({'b': 2, 'a': 1})
print(dict3 == dict4) # False Ordered a ordem importa



""" COLLECTIONS - NAMED TUPLE"""
# Tupla comum
tupla1 = 1, 2, 3
print(tupla1[1])

# Nomeamos a Tupla e parametros

# DECLARAÇÃO
# forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3
cachorro = namedtuple('cahcorro', ['idade', 'raca', 'nome']) # PREFERENCIA

# ATRIBUIÇÃO
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)
print()

# ACESSO
print(ray[0])
print(ray[1])
print(ray[2])

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow')) # qts ocorrences



""" COLLECTIONS - DECK"""
# RESUMINDO É UM TIPO DE LISTA

deq = deque('geek')
print(deq)

# ADD ELEMENT LIST
# lista1 = list('geek')
# lista1.append('y') # add no final 

# ADD ELEMENT
deq.append('y')
deq.appendleft('g')
print(deq)

# REMOVE ELEMENT
deq.pop()
print(deq)
deq.popleft()
print(deq)


