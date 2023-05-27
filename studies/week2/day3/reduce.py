"""_____ 3° DIA - 25/05/2023 (week 2 - total = 10)_____"""
"""
REDUCE

a partir do python3+ não é mais uma função built-in. Agora temos que importa-lá e utilizar esta função a partir do modulo 'functools'

Guido Van Rossum: Utilize a função reduce() se vc realmente precisa dela.
Em 99% das vezes um loop for é mais legível.

forma utilização
reduce(function(a, b), iteravel)

- parecido com reduce de JS para somar todos elementos
"""

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = lambda x, y: x + y
res = reduce(soma, dados)
print(res)
