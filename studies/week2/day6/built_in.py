"""_____ 6° DIA - 28/05/2023 (week 2 - total = 13)_____"""
""" 
 MODULOS (LIBS)
 
 - BUILT-IN (MODULOS JA INTEGRADOS NA LINGUAGEM PYTHON PRECISANDO APENAS FAZER IMPORTAÇÃO E NÃO PRECISANDO INSTALAR AS LIB OU PACOTES)

    INSTALADO POR PADRÃO:
         ___________________________
        | PYTHON | MODULES BUILT-IN |
        -----------------------------
         default |    via  import 

https://docs.python.org/3/py-modindex.html

"""


# ALIAS
# import random as rd
# from random import randint as rdi, choice as ch
# print(rd.random())

# IMPORT ALL FUNCTIONS *

# from random import *
# print(random()) # não precisa chama o modulo, as funções ja estão disponive

# COSTUMAMOS USAR TUPLE PARA MULTIPLOS IMPORT DO MESMO MODULO
from random import (
    random,
    randint,
    shuffle,
    choice
)
