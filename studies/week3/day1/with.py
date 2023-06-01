"""_____ 1° DIA - 30/05/2023 (week 3 - total = 15)_____"""
""" 
 BLOCO WITH 
    PASSOS PARA TRABALHRA COM ARQUIVOS
    1 - ABERTURA
    2 - MANIPULAÇÃO
    3 - FECHAR CONEXÃO DE STREAM
    
    WITH, UTILIZADO PARA CRIAR UM CONTEXTO DE TRABALHO, FAZENDO QUE SEJA FECHADO A CONEXÃO QUANDO TERMINADO O BLOCO 
"""

with open('textoexemplo.txt') as arquivo:
    print(arquivo.readlines())

# ele realiza abertora e fechamento dentro do bloco não precisando se preocupar em fechar o arquivo depois da manipulação

