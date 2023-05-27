"""_____ 3° DIA - 25/05/2023 (week 2 - total = 10)_____"""
""" 
MAP

Com map, fazemos mapeamento de valores para função

"""
import math

def area(r):
    """Calcula a área de um círculo com raio 'r'"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# FORMA COMUM
areas_comum = []
for r in raios:
    areas_comum.append(area(r))
print(areas_comum)

# FORMA 2 COM MAP

areas = map(area, raios) # map(function, iteravel) retorna um objeto class map
print(areas)
print(type(areas))
print(list(areas)) # converte o obj map para lista

# FORMA 3 MAP COM LAMBDA
print(list(map(lambda r: math.pi * (r**2), raios)))

# APÓS USAR MAP, DEPOIS DA PRIMEIRA UTILIZAÇAO DO RESULT, ELE ZERA
