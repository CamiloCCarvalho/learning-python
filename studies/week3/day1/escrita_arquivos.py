"""_____ 1° DIA - 30/05/2023 (week 3 - total = 15)_____"""
""" 
 ESCRITA EM ARQUIVOS

    AO ABRIR UM ARQUIVO PARA LEITURA, NÃO PODEMOS ESCREVER
    O MESMO VALE NO INVERSO 
    
    - AO ABRIR UM ARQUIVO PARA ESCRITA, CASO ELE NÃO EXISTA ELE É CRIADO NO SISTEMA OPERACIONAL 
    - write('string') não pode receber numeros
    - ABRINDO O MESMO ARQUIVO PARA ESCRITA DENOVO, ELE SERA SOBRE-ESCRITO
"""

# EXEMPLO DE ESCRITA
with open('novo_arquivo_texto.txt', 'w') as arquivo: # se o arquivo não existe ele cria
    arquivo.write('Escrever em arquivos é muito facil\n')
    arquivo.write('Esta é a ultima linha que estamos escrevendo \n')
