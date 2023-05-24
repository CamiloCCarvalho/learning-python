"""_____ 7° DIA - 22/05/2023 (week 1 - total = 7) _____"""
# FEITO EXERCICIOS MODULO 7

# DRY - Don't Repeat Yourself



# NORMAL
def diz_oi():
    return print("Olá")
diz_oi()

# ATRIBUINDO FUNÇÃO EM VARIAVEL
ola = diz_oi()
ola  # aqui precisa fica sem parenteses, pois ja usa na atribuição

# OU
ola2 = diz_oi
ola2()  # nesse caso pode deixar com ou sem parenteses



# FALOU SOBRE REFATORAÇÃO
# RETURN -- finaliza a função

# keyword  arguments
def nome_completo(nome, sobrenome):
    return print(f'{nome} {sobrenome}')
nome_completo(sobrenome="Costa", nome="Camilo")

# FUNCTION COM PARAMETRO DEFAULT
def exponencial(numero, potencia=2): # obrigatório estar no fim dos paremetros
    return print(numero ** potencia)

exponencial(5)

# FUNCTION QUE CHAMA OURTA FUNCTION

def soma(num1, num2):
    return print(num1 + num2)

def subtracao(num1, num2):
    return print(num1 - num2)

def calc(num1, num2, func=soma):
    return func(num1, num2)

calc(5, 5, subtracao)

# ESCOPOS

varTest = 'python'

def curso():
    varTest = 'javascript' # escopo local tem preferencia
    return print(varTest)

print(varTest) # porem fora do bloco existe apenas a de escopo global
curso()

# OBS.: PROCURAR EVITAR USAR VARIAVEIS GLOBAIS

# USANDO VARIAVEL GLOBAL DENTRO DO ESCOPO LOCAL
total = 0
def incrementa():
    global total
    total = total + 1
    return total

print(incrementa())


# USANDO VARIAVEL LOCAL EM SUBLOCAL DENTRO DO ESCOPO MENOR
def fora():
    contador = 0
    
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())

""" 
DOCUMENTAÇÃO DE FUNÇOES - DOCSTRINGS

    podemos ter acesso a documentação de uma função em python
    __doc__
    
    podemos fazer acesso tambem com
    help()

"""

def diz_ola():
    """ Uma função simples que retorna uma string 'Oi' """
    return 'Oi'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que desejamos usar para gerar exponencial, por padrão 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """

#print(help(diz_ola))
#print(exponencial.__doc__)



"""
 ARGS - *args
 
    Parâmetro como qualquer outro, poderia chamar de xuxu, porem a comunidade de desenvolvimento decidiu adotar o nome args < *args >.
    
    Utilizado em função para colocar valores extras informados como entrada em uma tupla. Lembre-se que tuplas são imutáveis.
    
"""

# EXEMPLO
def soma_todos(n1, n2, n3):
    return n1 + n2 + n3

print(soma_todos(1,2,3))

# COM < *args >

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(2))
print(sum_all(2, 4))
print(sum_all(2, 6, 4))
print(sum_all(2, 7))

# REFATORADO
def soma_todos_valores(*args):
    return sum(args)

# TAMBÉM PODE TER PARAMETROS OBRIGATÓRIOS
def exemple(param1, param2, *args):
    return sum(args)

# * COMO DESEMPACOTADOR (SIMILAR A DESESTRUTURAÇÃO JS)
lista = [1 ,2 , 3, 4]
print(soma_todos_valores(*lista))

#OBS.: * INFORMA QUE ESTAMOS PASSANDO COMO ARGUMENTO UMA COLLECTION, FAZENDO DESEMPACOTAMENTO ANTES DA EXECUÇÃO 
    # FUNCIONA COM [ LISTA ]
    # FUNCIONA COM SET { CONJUNTO }
    # FUNCIONA COM ( TUPLAS )
    
    # NÃO FUNCIONA COM [ KEY : DICT ]
    
"""
 **KWARGS - *kwargs
 
    Parâmetro como qualquer outro, poderia chamar de xuxu, porem a comunidade de desenvolvimento decidiu adotar o nome kwargs < **kwargs >.
    
    Utilizado em função para colocar valores extras informados como entrada porem exigindo que usamos parâmetros NOMEADOS e transforma esses parametros extras em um DICT
    
"""

# EXEMPLO
def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é a cor: {cor}')

cores_fav(marcos='azul', juliana='vermelho', joao='verde')

# EXEMPLO MAIS COMPLEXO
def cumprimento_esp(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return print('Ola Geek! Meus cumprimentos Pythonico!')
    
cumprimento_esp(geek='Python')

# PARAMETROS OBRIGATORIOS
# *ARGS
# PARAMETROS DEFAULT (NAO OBRIGATORIOS)
# **KWARGS

def minha_func(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('SOLTEIRO(A)')
    else:
        print('CASADO(A)')
    print(kwargs)

minha_func(8, 'Julia')
minha_func(18, 'Felicity', 4, 5, 6, solteiro=True)
minha_func(34, 'Felipe', eu="nao", voce="vai")


""" ____MODULO 9_____ """

"""
LIST COMPREHENSION
    sintaxe:
        level 1:
            variavel = [ dadoQqueremos     for dadoQqueremos in iteravel ]
        level 2:
            variavel = [ dadoQqueremos     for dadoQqueremos in iteravel   if  condiçao ]
        
        OBS.: Como LC retorna não é obrigatório atribuir a uma variavel
        
"""

# EXEMPLO
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# VERSÃO LEVEL 2
even = [number  for number in numbers if number % 2 == 0]
odd = [number  for number in numbers if number % 2 != 0]

# REFATORADO
even = [number for number in numbers if not number % 2]
odd = [number for number in numbers if number % 2]

res = [number * 2 if number % 2 == 0 else number / 2 for number in numbers]

"""
LISTAS ANINHADAS - NESTED LISTS
    - Em outras linguas costumam ter Arrays/Vetores e Matrizes
    - Em Python temos Listas
    
"""

listas = [[1,2,3], [4,5,6], [7,8,9]]

print(listas)
print(type(listas))

# ACESSO     L  C
print(listas[0][1])

# ITERANDO
for lista in listas:
    for num in lista:
        print(num)
        
# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

# EXEMPLO TABULEIRO
tabuleiro = [[numero for numero in range(1,4)] for valor in range(1, 4)]
print(tabuleiro)

# JOGADAS JOGO DA VELHA
velha = [['x' if numero % 2 == 0 else 'O' for numero in range(1,4)] for valor in range(1,4)]
print(velha)

# INICIANDO TABULEIRO COM VALOR DEFAULT EM BRANCO
print([['*' for i in range(1,4)] for j in range(1,4)])


"""
DICTIONARY COMPREHENSION

    - se quisermos uma lista:
    lista = [1,2,3,4]
    
    - se for tupla:
    tupla = (1,2,3,4)
    
    - set ou conjunto:
    set = {1, 2, 3}     # não aceita valores repetidos, e a ordem não é garantida
    
    - dict:
    {'a': 1, 'b': 2}   # não pode repetir a chave
    
    
    
    # Sintaxe:
    { chave:valor    for valor in iteravel}
    
"""

num_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

sqr_num_dic = {chave: valor ** 2 for chave, valor in num_dic.items()}
print(sqr_num_dic)

# DE LIST PARA DICT
test = [1,2,3,4,5]
quadrado = {valor: valor ** 2 for valor in test}
print(quadrado)

# funciona com SET, CONJUNTO, LIIST, TUPLE

# MIX DATA
chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

evenOdds = [1,2,3,4,5]
resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in evenOdds}
print(resultado)


"""
SET COMPREHENSION

    SINTAXE:
    {num for num in range(1,7)}
    
"""