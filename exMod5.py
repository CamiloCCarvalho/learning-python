import math

# MODULO 5 - EX01
def talestNumber():
    try:
        number1 = float(input('Digite um numero:'))
        number2 = float(input('Digite outro numero:'))

        if number1 > number2:
            print(f'O maior numero é: {number1}')
        elif number1 == number2:
            print(f'Os numeros são iguais')
        else:
            print(f'O maior numero é: {number2}')
    except ValueError:
        print('Error: Confira se você digitou numeros!')
        

# MODULO 5 - EX02
def squareRootOfNumber():
    try:
        number = float(input('Digite um numero:'))
        
        if number <= 0:
            raise ValueError
        else:
            print(f'A RAIZ quadrada do numero é: {math.sqrt(number)}')        
    except ValueError:
        print('Error: Você NÃO digitou um numero positivo!')
        
# MODULO 5 - EX03
def squareAndRoot():
    try:
        number = float(input('Digite um numero:'))
        
        if number <= 0:
            print(f'O quadrado do numero é: {number**2}')
        else:
            print(f'A RAIZ quadrada do numero é: {math.sqrt(number)}')        
    except ValueError:
        print('Error: Você NÃO digitou um numero positivo!')
        
# MODULO 5 - EX04 igual anterior sem retorno no negativo

# MODULO 5 - EX05
def isOdd():
    try:
        number = int(input('Digite um numero:'))
        
        if number % 2 == 0:
            print('O numero é par')
        else:
            print('O numero é impar')
    except ValueError:
        print('Error: Você NÃO digitou um numero INTEIRO!')


