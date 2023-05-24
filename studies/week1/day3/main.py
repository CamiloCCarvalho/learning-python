from fractions import Fraction
"""_____ 3° DIA - 18/05/2023 (week 1 - total = 3)_____"""



"""MODULO 5 - ESTRUTURAS (LOGICA E CONDICIONAL)"""
# NUMBER WITH FORMATS
num1:int = 10 # int
num2:float = 4.5 # float
num3 = Fraction(3, 4) # return 3/4 (Class Fraction)
num4 = Fraction(4.5) # return 9/2
num5 = Fraction('3/4') # return 3/4
num6 = int(num2) # casting
num7 = num1 / 3 # return float (int/int --> infers result float)


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
