"""_____ 4° DIA - 26/05/2023 (week 2 - total = 11)_____"""
""" 
REVERSED

 - não confundir com reverse(), reverse() só funciona com lista
 
 - reversed() funciona com qualque iteravel
 - depois de usar o resultado o dado é apagado da memoria assim como no map e filter
 
"""

# EXEMPLO
lista = [1,2,3,4,5]

res_list = reversed(lista)
print(type(res_list)) # retorna um OBJ do tipo <class 'list_reverseiterator'>

# SOLUÇÃO
print(list(res_list))

res_tuple = reversed(lista)
print(tuple(res_tuple))

res_set = reversed(lista)
print(set(res_set), ' <- Note que este não funciona pois SET não organiza os elementos') # não faz reverse pois não tem ordem em SET

# REVERSED STRING
for letra in reversed('Geek University'):
    print(letra, end='')
print()
    
# FAZENDO O MESMO SEM O FOR
print(''.join(list(reversed('Geek University'))))

# FORMA MAIS SIMPLES
print('Geek University'[::-1])

# USANDO REVERSED PARA FAZER LOOP INVERTIDO
for n in reversed(range(0,10)):
    print(f'numero é: {n}')

# INVERTENDO O REVERSED DO LOOP INVERTIDO
for n in reversed(range(0,10)[::-1]):
    print(f'numero é: {n}')
