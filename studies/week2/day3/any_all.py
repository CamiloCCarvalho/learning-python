"""_____ 3° DIA - 25/05/2023 (week 2 - total = 10)_____"""
""" 
ANY ALL

all() --> True se toods elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio

any() --> True se qualquer um dos elementos for verdadeiro, mesmo que seja só um. Se o iteravel estiver vazio False

"""
# all()
print(all([num for num in [4,2,10,6,8] if num % 2 == 0])) # Retorna True por que gera uma lista, vazia ou com algum elemento. Só da False se algum elemento nesta lista for False (0 no caso, ou '' string vazia, ou valor bool False)

# any()

print(any([])) # False
print(any([0,0,0,0])) # False
print(any([False, '', 0])) # False
print(any([0,1, '', False, {'key': 12}])) # True

# Resumo? só retorna False se TUDO for FALSE, ou Iteravel Vazio
