# MODULO 6 - EXERCICIO 1
number = 1
count = 5
for number in range(1, count+1):
    print(f'multiplo de 3: {number * 3}')
print()

# MODULO 6 - EXERCICIO 2

# versão com for
level = 1
for level in range(1, 101):
    print(level, " ", end="")
    level += 1
print()

# versão com while
n = 1
while n < 101:
    print(n, " ", end="")
    n += 1
print()

# versão com o que seria do while pois python não tem esta estrutura
num = 1
while 1:
    print(num, " ", end="")
    num += 1
    if num > 100:
        break
print()
print()
    
# MODULO 6 - EXERCICIO 3
numb = 11
while numb > -1:
    numb -= 1
    print(numb, ' ', end='')
    if numb == 0:
        print('FIM !')
        break
print(), print()

# MODULO 6 - EXERCICIO 4
numInt = 0
limit = 100000
while numInt <= limit:
    print(numInt)
    numInt += 1000

# MODULO 6 - EXERCICIO 5
listNums = []
limitX = 10
while limitX > 0:
    listNums.append(int(input('Digite um numero: ')))
    limitX -= 1

print(f'A soma é: {sum(listNums)}', )
    