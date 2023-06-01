"""_____ 1° DIA - 30/05/2023 (week 3 - total = 15)_____"""
""" 
 SEEK AND CURSORS

"""

arquiv = open("textoexemplo.txt") # abertura
print('first')
print(arquiv.read()) # read(limitIndex)
print()

# PARA MOVER O CURSOR
arquiv.seek(0)
print('second')
print(arquiv.read())

# LEITURA POR LINHAS
arquiv.seek(0)
print(arquiv.readline()) # retorna <class 'str'>  NÃO Lê LINHAS EM BRANCO

arquiv.seek(0)
print(arquiv.readlines()) # retorna uma lista de linhas de leitura, util para saber quantas linhas tem o arquivo


# FECHANDO ARQUIVO
if not arquiv.closed:
    arquiv.close()

