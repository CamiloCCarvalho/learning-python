from fractions import Fraction

"""
ESTUDO COMPLETO DE PYTHON

    MODULO 1 - APRESENTAÇÃO DO CURSO
    MODULO 2 - PREPARANDO O AMBIENTE

"""

"""
MODULO 3 - INTRODUÇÃO A LINGUAGEM
    
    PEP8 - Boas Praticas
    Dir e Help

"""

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
     # """ this is string multiple lines"""
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
num3 = Fraction(3, 4) # Class Fraction return 3/4
num4 = Fraction(4.5) # return 9/2
num5 = Fraction('3/4') # return 3/4
num6 = int(num2) # casting
num7 = num1 / 3 # return float (int/int)
    
    # OBS.:
     # numbers not have limit in python (different of Java 2^63 and 1bit to assign)
     # fraction return a literal division to stay more precise result
     # Python enfer what's the type of result and return it

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

    
    