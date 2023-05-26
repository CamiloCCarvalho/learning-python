"""_____ 2° DIA - 24/05/2023 (week 2 - total = 8)_____"""

"""
MODULO 10 - EXPRESSÕES LAMBDA E FUNÇÕES INTEGRADAS
"""

""" EXPRESSOES LAMBDA """

lambda x: 3 * x + 1 # expressão parametro: retorno

# UTILIZANDO LAMBDA (FORMA NÃO DIGNA DE USAR)

calc = lambda x: 3 * x +1 
print(calc(4))
print(calc(7))

# PODE TER MULTIPLAS ENTRADAS
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' angelina   ', ' JOILE          '))
# SE PASSARMOS MAIS ARGUMENTOS DO QUE PARAMETROS TEREMOS TypeError


autores = ['Issac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Doublas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

# Com lambda organizar via SOBRENOME
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower()) # sort muda o array original 
# para cada item em autores, usa o elemento como argumento lambda, separa os nomes da pessoa por split via espaço, dentro desse nome pega o ultmio nome com -1 usando caixa baixa
print(autores)

# Função Quadratica
# f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """Retorna a funçao f(x) = a*x² + b*x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# sem variavel
print(geradora_funcao_quadratica(3, 0, 1)(2))
