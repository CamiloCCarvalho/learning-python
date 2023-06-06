"""_____ 7° DIA - 05/06/2023 (week 3 - total = 21)_____"""

"""
    WALRUS
        -> Podemos agora declarar uma variavel, atribuir um valor,
        deixando-a ja disponivel para retornar o valor na declaração.
        
        -> syntax:
            variavel := value # with return able
"""

# FORMA COMUM
nome = 'Geek University'
print(nome)

# WALRUS
print(nome_completo := 'May Shiranui')

# EXEMPLO DE USO
cesta = []
while fruta := input('Digite o nome de uma fruta: ') != 'jaca':
    cesta.append(fruta)
