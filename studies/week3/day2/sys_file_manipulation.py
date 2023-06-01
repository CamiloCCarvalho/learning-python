"""_____ 2° DIA - 31/05/2023 (week 3 - total = 16)_____"""
""" 
 SISTEMA DE ARQUIVOS E MANIPULAÇÃO 

    
"""
import os
# DESCOBRINDO SE UM DIRETORIO OU ARQUIVO EXISTE

print(os.path.exists('arquivo.txt')) # no diretorio local onde esta sendo chamado este arquivo
print(os.path.exists('frutas.txt')) # True
print(os.path.exists('pasta')) # False

# CRIAR ARQUIVOS COMO JA VIMOS ANTES

# lembrando sem especificar o local vai ser na onde o arquivo esta sendo executado
open('arquivo_teste.txt', 'w').close()

# forma 2
open('arquivo_teste2.txt', 'a').close()

# forma 3
with open('arquivo_teste3.txt', 'w') as arquivo:
    # codigo se for usar
    # pass -> palavra reservada para passar, sem precisar preencher o bloco
    pass


# FORMA MAIS INDICADA

# cria um diretório por vez
# os.mkdir('pasta_teste') # ira criar no diretorio atual
#os.mknod('C:\\Users\\CamiloCostadeCarvalh\\PycharmProjects\\'
         #'pythonudemy\\python\\studies\\week3\\day2\\arquivo_teste5.txt')

# OBS.: NO MAC PODE DAR PROBLEMA
# OBS.: CRIANDO ARQUIVO COM MKNOD() SE JA EXISTIR DA ERRO FileExistsError

# MULTIPLOS DIRETORIOS
# os.makedirs('teste/pasta/ultimo')

# CASO JA EXISTAM PARA IGNORAR O ERRO DE FileExistsError
os.makedirs('teste/pasta/ultimo', exist_ok=True) # caso exista só passa batido

# RENOMEANDO
os.rename('teste', 'ash_pasta_teste')

# continue ...