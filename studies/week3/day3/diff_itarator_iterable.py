"""_____ 3° DIA - 01/06/2023 (week 3 - total = 17)_____"""
""" 
 ENTENDENDO ITERATOR E ITERABLE
 
 ITERATOR -> um objeto que pode ser iterado
    retorna um dado, sendo um elemento por vez quando a função next() é chamada
    
 ITERABLE -> um objeto que retorna um iterator quando a função iter() é chamada
 
"""

# EXEMPLO DE ITERABLE
name = 'geek'
numbers = [1, 2, 3, 4, 5, 6]

it1 = iter(name)
it2 = iter(numbers)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
