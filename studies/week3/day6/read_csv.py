"""_____ 6° DIA - 04/06/2023 (week 3 - total = 20)_____"""

"""
    CSV E JSON
        --> CSV arquivo de dados, porem geralmente pode abrir como arquivo de texto
    
    1 LENDO ARQUIVO CSV
        --> Comma Separated Values - Valores separados por virgula
            -> pode ter outro tipo de separador ( ; | <space> )
            -> importante ter um padrão
            
    2 LUGAR PARA PEGAR DADOS:
        http://dados.gov.br/dataset
        
        
    3 PROCESSO DE LIMPEZA DE DADOS - FORMA NÃO IDEAL
        with open('lutadores.csv') as arquivo:
            dados = arquivo.read()
            print(type(dados)) # str
            dados = dados.split(',')
            print(dados) # retorna o conteudo em si em string mesmo
            
    4 FORMAS DE LER CSV (PYTHON TEM MAIS DE UMA)]
        -> reader: permite iterar sobre as linhas do arquivo CSV como listas
        -> DictReader: permite iterar sobre as linhas do arquivo CSV como OrderedDict
        
    4.1 READER
        from csv import reader

        with open('lutadores.csv') as arquivo:
            leitor_csv = reader(arquivo)
            next(leitor_csv) # iterator tem next, pulando o cabeçalho dessa forma
                for linha in leitor_csv:
                # cada linha é uma lista
                print(f'{linha[0]} local de nascimento:{linha[1]} altura:{linha[2]} centimetros')
                
    4.2 ORDERED DICT
"""

# ORDERED DICT
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',') # segundo parametro pode especificar separador
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nascido(a) em {linha['País']} e mede {linha['Altura (em cm)']}")
