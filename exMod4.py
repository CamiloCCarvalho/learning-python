# MODULO 4 - EX01
def showNumberInt():
    try:
        number = int(input("Digite um número inteiro: "))
        print("O número digitado foi:", number)
    except ValueError:
        print("Você não digitou um número inteiro!")
        
# MODULO 4 - EX02
def showNumberFloat():
    try:
        number = float(input("Digite um número REAL: "))
        if int(number) == number:
            raise ValueError("O numero NÃO é REAL!")
        print("O número digitado foi:", number)
    except ValueError as error:
        print(error)
        
# MODULO 4 - EX03
def sumNumbers():
    try:
        listNumber = list([int(input("Digite um numero:")),
                           int(input("Digite um numero:")),
                           int(input("Digite um numero:"))])
        sum = 0
        for number in listNumber:
            sum += number
        print(f'A soma dos numeros é: {sum}')
    except ValueError as e:
        print(e)

# MODULO 4 - EX04
def squareNumber():
    try:
        number = float(input('Digite um numero para saber o quadrado do mesmo:'))
        number = number**2
        print(number)
    except ValueError as e:
        print(e)

# MODULO 4 - EX05
def partNumber():
    try:
        number = float(input("Digite um número REAL: "))
        if int(number) == number and not '.':
            raise ValueError("O numero NÃO é REAL!")
        print("A quinta parte do numero é:", (number/5))
    except ValueError as error:
        print(error)
       
