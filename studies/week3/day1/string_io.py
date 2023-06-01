"""_____ 1° DIA - 30/05/2023 (week 3 - total = 15)_____"""
""" 
 STRING IO
 
 - LEITURA E ESCRITA DE ARQUIVOS, O SOFTWARE PRECISA DE PERMISSÃO PARA LEITURA E ESCRITA.
 - Utilizado para ler e criar arquivos em memória
"""

from io import StringIO

mensagem = 'Esta é apenas uma simples mensagem em formato string'

arquivo = StringIO(mensagem)

print(arquivo.read())
arquivo.write('Outro texto digitado')
arquivo.seek(0)
print(arquivo.read())
