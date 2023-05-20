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
lista6 = [1, 99, 50, 2, 1505, 27, 33]
print(lista4)

# Verificar se o valor esta contido na lista
if 4 in lista2:
    print('Encontrei o numero 4')
else:
    print('Não encontrei o numero 4')
    
# Ordenar lista
lista6.sort()
print('lista numerica ordenada: %s ' {lista6}) 
    # Duvida? por que não pode fazer print(lista6.sort())
    # Duvida? por que o retorno é none, equivale a null de js ?

lista5.sort()
print(lista5)


"""_____ 5° DIA - 20/05/2023 _____"""
# TUPLE

# DICTIONARY (DICT)

# MAP

# CONJUNTO

# MODULE COLLECTION
    # COUNTER
    # DEFAULT DICT
    # ORDERED DICT
    # DEQUE


"""MODULO 8 - FUNÇÕES"""
