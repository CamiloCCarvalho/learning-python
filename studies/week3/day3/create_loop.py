"""_____ 3° DIA - 01/06/2023 (week 3 - total = 17)_____"""
""" 
 CRIANDO LOOP
"""


def meu_for(iteravel):
    item = iter(iteravel)
    while True:
        try:
            print(next(item))
        except StopIteration:
            break


name = 'Geek University'
numbers = [1, 2, 3, 3, 5]

meu_for(name)
print()
meu_for(numbers)
