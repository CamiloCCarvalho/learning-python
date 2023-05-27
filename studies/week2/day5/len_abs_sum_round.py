"""_____ 5° DIA - 27/05/2023 (week 2 - total = 12)_____"""
""" 
LEN, ABS, SUM, ROUND
 
"""


# len() - ja foi visto retorna o tamanho do iteravel
print('Geek University'.__len__()) # por baixo dos panos usa do_under_len_do_under

# abs() - retorna o valor absoluto de um numero (sem sinal)

# sum() soma os elementos, tem inicial default = 0
print(sum([1,2,3,4,5])) # return 15
print(sum([1,2,3,4,5], 10)) # return 25 (segundo argumento é o parametro de valor inicial)

# COM STRING NÃO FUNCIONA USAR ''.join(seq)

# round() - RETORNA UM INTEIRO() se a precisão não for informada, caso contrario retorna float com a precisão informada.

print(round(10.2))
print(round(10.5)) # até .5 arredonda pra baixo
print(round(10.2515315, 2)) # segundo arg é a precisão de casas
