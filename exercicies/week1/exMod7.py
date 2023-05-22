import random
# MODULO 7 - EXERCICIO 1

# LISTA 1 - EX1
a = [1, 0, 5, -2, -5, 7]
sumNum = a[0] + a[1] + a[5]
print(f'a Soma é: {sumNum}')

a[3] = 100
for index, item in enumerate(a):
    print(f'index: {index} | valor: {item}')

# LISTA 1 - EX2
vet = []
limit = 6

while limit > 0:
    #vet.append(int(input('Digite um numero inteiro: ')))
    limit -= 1

print(vet)

# LISTA 1 - EX3
# elements = []
# squareElements = []
# for i in range(10):
#     elements.append(float(input('Digite um numero Real: ')))
#     squareElements.append(elements[i]**2)
# 
# print(squareElements)

# LISTA 1 - EX4
random_list = [random.uniform(0, 100) for i in range(8)]
x = random_list[random.randint(0, 8)]
y = random_list[random.randint(0, 8)]
print(f'Lista gerada automaticamente: \n {random_list}')
print(f'A soma de X e Y é: {x+y}')

# LISTA 1 - EX5
random_list2 = [random.randint(-100, 100) for i in range(10)]
odds = 0
res_list = []
for item in random_list2:
    if (item % 2 == 0):
        odds += 1
        res_list.append(item)
print(f'Lista de Pares encontrados: {res_list}')
print(f'Quantidade de numeros pares: {odds}')
