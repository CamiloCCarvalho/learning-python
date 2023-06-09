"""_____ 6° DIA - 04/06/2023 (week 3 - total = 20)_____"""

"""
    CSV E JSON

    1 ESCREVENDO ARQUIVO
    
    reader() -> leitor
    writer() -> escritor
    writerow() -> escreve uma linha  
    
    2 PRIMEIRA FORMA
        from csv import writer

        with open('filmes.csv', 'w') as arquivo:
            escritor_csv = writer(arquivo)
            filme = None
            escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
            while filme != 'sair':
                filme = input('Informe o nome do filme: ')
                if filme != 'sair':
                    genero = input('Informe o gênero: ')
                    duracao = input('Informe a duraçao (em minutos): ')
                    escritor_csv.writerow([filme, genero, duracao])
  
    3 SEGUNDA FORMA
"""

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho) # parametro args passa um container
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duraao (em minutos): ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})
