"""_____ 1° DIA - 30/05/2023 (week 3 - total = 15)_____"""
""" 
 SISTEMA DE ARQUIVOS E NAVEGAÇÃO 
 
 PARA FAZER USO E MANIPULAÇÃO DE ARQUIVOS DO SISTEMA OPERACIONAL, PRECISAMOS IMPORTAR E FAZER USO DO MODULO OS
 
 OS -> OPERATING SYSTEM - SISTEMA OPERACIONAL
 
"""

import os

# getcwd() -> Get Current Work Directorey. Diretório de trabalho corrente. retorna o path caminho absoluto
print(os.getcwd())

# chdir() -> podemos utilizar para mudar de diretório
os.chdir('..')
print(os.getcwd())

# Pdemos chegar se um determinado diretório é absoluto ou relativo
print(os.path.isabs('home/CamiloCostadeCarvalh')) # POSIX

# OBS.: SISTEMA WINDOWS USA \ COMO SEPARADOR E NÃO COMO CARACTERE DE SCAPE
# NESTE CASO:
print(os.path.isabs('C:\\Users\\CamiloCostadeCarvalh')) # NT

# PODEMOS TAMBÉM IDENTIFICACR O SISTEMA OPERACIONAL COM MODULO OS
#print(os.name) # nt (WINDOWS) | POSIX (LINUX e MAC)

# DETALHES
# print(os.uname()) apenas no POSIX

# WINDOWS
# import sys
# print(sys.platform) # devolve se é win32 ou 64 e ainda erra

# MUDANDO DE DIRETORIO
print(os.getcwd()) # C:\Users\CamiloCostadeCarvalh\PycharmProjects\pythonudemy\python\studies\week3
res = os.path.join(os.getcwd(), 'day1') # C:\Users\CamiloCostadeCarvalh\PycharmProjects\pythonudemy\python\studies\week3/day1

os.chdir(res)
print(os.getcwd()) # vantagem ele usa / no posix, e no nt usa \\ para estrutura do windows

# PODEMOS LISTAR DIRETORIOS
print(os.listdir()) # retorna uma lista

# vendo quantos itens tem
print(len(os.listdir()))

# MAIS DETALHES
scanner = os.scandir()
print(list(scanner)) # devolve um iterator, por isso usamos list

arquivos = list(scanner)

print(dir(arquivos[0]))

print(arquivos[0].inode()) # Identificador do "nó"
print(arquivos[0].is_dir()) # é diretório? False
print(arquivos[0].is_file()) # é arquivo ? True
print(arquivos[0].is_symlink()) # é link simbolico? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # status, varias info, st_size=tamanho_em_bytes

# USANDO SCANDIR PRECISAMOS FECHAMO IGUAL COM ARQUIVOS E OPEN...
scanner.close()
