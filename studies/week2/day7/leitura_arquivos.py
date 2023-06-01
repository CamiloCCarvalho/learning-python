"""_____ 7° DIA - 29/05/2023 (week 2 - total = 14)_____"""
""" 
 LEITURA DE ARQUIVOS
 
 - PARA O CONTEUDO DE UM ARQUIVO PYTHON UTILIZAMOS A FUNÇAO INTEGRADA open()
 
 - open() -> Na forma mais simples passamos um paramentro como argumento, sendo o caminho do arquivo que deve ser lido. e retorna:
     - _io.TextIOWrapper e é com ele que trabalhamos.
     
    https://docs.python.org/3/library/functions.html#open
    
    # OBS.: Por padrão, a função open() abre o arquivo para leitura, Este arquivo deve existir, ou então teremos o erro FileNotFoundError

"""
arquivo = open('text.txt')
print(arquivo)
print(type(arquivo))
print(arquivo.read())
# Python usa recurso para trabalha com arquivo chamado cursor, funciona como o cursor quando estmaos escrevendo
