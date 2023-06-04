"""_____ 5° DIA - 03/06/2023 (week 3 - total = 19)_____"""

"""
    (MODULE) DECORATORS

    2 - O QUE SÃO DECORATORS?
        - são funções
        - envolvem outras funçoes e aprimoram seus comportamentos
        - também são exemplos de HOF
        - sintaxe propria com @
        
        - Syntact Sugar (Açucar Sintático)
"""

# EXEMPLO

def seja_educado(func): # DECORATOR SEM SYNTACT SUGAR
    def sendo():
        print('FOi um prazer conhecer você!')
        func()
        print('tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) á Geek University')


teste = seja_educado(saudacao)
teste()


# COM SYNTACT SUGAR


def seja_educado_mesmo(func):
    def sendo_mesmo():
        print('Foi um prazer muito grande conhecer a vossa magestade!')
        func()
        print('Tenha um excelente dia meretissimo!')


@seja_educado_mesmo
def apresentando():
    print('meu nome é Pedro')


apresentando()
