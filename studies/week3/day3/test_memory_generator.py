"""_____ 3° DIA - 01/06/2023 (week 3 - total = 17)_____"""
""" 
TESTE DE MEMORIA COM GENERATOR
 
SEQUÊNCIA DE FIBONACCI:
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, ...
 
"""

# TESTE 1 FUNÇÃO DE LISTA
def fibonacci_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# TESTE 2 FUNÇÃO DE GENERATOR
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


def test_with_list(): # 22MB
    for n in fibonacci_list(20000):
        print(n)


def test_with_gen(): # 3MB
    for n in fib_gen(20000):
        print(n)


# test_with_list()
test_with_gen()
