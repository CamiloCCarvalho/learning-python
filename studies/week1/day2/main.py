from fractions import Fraction

"""_____ 2° DIA - 17/05/2023 (week 1 - total = 2) _____"""

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
    
# TAMBÉM PESQUISADO SOBRE NUMEROS IMAGINARIOS
