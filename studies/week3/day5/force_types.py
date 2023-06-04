"""_____ 5° DIA - 03/06/2023 (week 3 - total = 19)_____"""

"""
    (MODULE) DECORATORS

     - FORÇANDO TIPOS
     
     LEMBRAR DE ZIP
        a = (1, 2, 3)
        b = (4, 5, 6)
        c = zip(a, b)
        
        c => (1, 4), (2, 5), (3, 6)

"""

def forca_tipo(*tipos):
    def decorador(func):
        def converter(*args, **kwargs):
            novo_arg = []
            for(valor, tipo) in zip(args, tipos):
                novo_arg.append(tipo(valor))
            return func(*novo_arg, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Ola Geek Universitario! ', '2')
