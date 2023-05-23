import math
import random

# MODULO 5 - EX01
def talest_number():
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
def sqr_root_number():
    try:
        number = float(input('Digite um numero:'))
        
        if number <= 0:
            raise ValueError
        else:
            print(f'A RAIZ quadrada do numero é: {math.sqrt(number)}')        
    except ValueError:
        print('Error: Você NÃO digitou um numero positivo!')
        
# MODULO 5 - EX03
def square_and_root():
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
def is_odd_even():
    try:
        number = int(input('Digite um numero:'))
        
        if number % 2 == 0:
            print('O numero é par')
        else:
            print('O numero é impar')
    except ValueError:
        print('Error: Você NÃO digitou um numero INTEIRO!')
print()

# MODULO 5 - EX06
print(" MODULO 5 - EXERCICIO 6")
num1 = random.randint(-1000, 1000)
num2 = random.randint(-1000, 1000)
print(f'DADOS OS NUMEROS {num1} e {num2}')

if num1 > num2:
    print(f'O maior é: {num1} | diferença: {num1-num2}')
elif num1 == num2:
    print(" Numeros Iguais")
else:
    print(f'O maior é: {num2} | diferença: {num2-num1}')
    
# MODULO 5 - EX07
print(" MODULO 5 - EXERCICIO 7")
num1 = random.randint(-1000, 1000)
num2 = random.randint(-1000, 1000)
print(f'DADOS OS NUMEROS {num1} e {num2}')

if num1 > num2:
    print(f'O maior é: {num1} | diferença: {num1-num2}')
elif num1 == num2:
    print(" Numeros Iguais")
else:
    print(f'O maior é: {num2} | diferença: {num2-num1}')
    
print()

# MODULO 5 - EX08
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if (nota1 < 0.0 or nota1 > 10.0) and (nota2 < 0.0 or nota2 > 10.0):
    print(f'confira as notas digitas NOTA1: {nota1} e NOTA2: {nota2} | AMBAS precisam estar entre 0.0 e 10.0')
else:
    print(f'A média do aluno é: {(nota1+nota2)/2}')
   
print() 
    
# MODULO 5 - EX09
salario = float(input('Digite o valor do salario: '))
prest = float(input('Digite o valor da prestação: '))

if prest > (salario * 0.2):
    print(f'Empréstimo não concedido. Prestação muito alta')
else:
    print(f'Emprestimo concedido')

print()

# MODULO 5 - EX10
h = float(input('Digite a Altura: '))
gen = str(input('Digite o sexo: "F" para Feminino / "M" para Masculino: '))

if gen == 'F' or 'f':
    print(f'Peso ideal Feminino: {round((62.1 * h) - 44.7, 2)} Kg')
elif gen == 'M' or 'm':
    print(f'Peso ideal Masculino: {round((72.7 * h) - 58, 2)} Kg')
else:
    print('Por favor confira os dados digitados!')
    