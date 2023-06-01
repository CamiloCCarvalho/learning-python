"""_____ 1° DIA - 30/05/2023 (week 3 - total = 15)_____"""
""" 
 MODOS - R, W ...

    https://docs.python.org/3/library/functions.html#open
    r - Abre para leitura - padrão
    w - Abre para escrita - sobreescreve arquivo caso já exista.
    x - Abre para escrita - somente se o arquivo não existe.
    a - Abre para escrita com Append - podendo adicionar no final do arquivo
    + - Abre para modo Update (Read and Write)
    r+ , w+, a+
"""

with open('textoexemplo.txt', 'x') as arquivo:
    arquivo.write('Testando o modo X \n')
