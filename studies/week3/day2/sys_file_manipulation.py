"""_____ 2° DIA - 31/05/2023 (week 3 - total = 16)_____"""
""" 
 SISTEMA DE ARQUIVOS E MANIPULAÇÃO 
 https://docs.python.org/3/library/os.html?highlight=os#module-os
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
# os.makedirs('teste/pasta/ultimo', exist_ok=True) # caso exista só passa batido

# RENOMEANDO
# os.rename('teste', 'ash_pasta_teste')
# se o diretório não existir teremos um FilenotFoundError

# os.rename('ash_pasta_teste', 'nova_pasta')
# se o diretório que queremos renomear tiver conteudos OSError

# os.rename('ash_pasta_teste/pasta/ultimo/test.txt', 'ash_pasta_teste/pasta/ultimo/novo_arquivo_renomeado.txt')

# REMOVENDO ARQUIVOS
# ATENÇÃO ! Ao deletar arquivos eles não vão pra lixeira, eles somem.
# os.remove('ash_pasta_teste/pasta/ultimo/novo_arquivo_renomeado.txt')

# NO WINDOWS SE O ARQUIVO/DIR ESTIVER ABERTO OU EM USO POR ALGUM USUARIO VOCÊ RECEBERÁ UM ERRO SE TENTAR DELETAR

# SE VOCÊ PASSAR UM DIR E NÃO UM ARQUIVO VC RECEBE UM IsADirectoryError

# REMOVENDO DIRETÓRIOS - VAZIOS
# os.rmdir('teste/pasta/ultimo') # não pode ter nada dentro se não da erro

# REMOVENDO LISTA DE DIRETORIOS/ARQUIVOS NO MESMO DIR (VAZIOS)
#for arquivos in os.scandir('teste'):
#    if arquivos.is_file():
#        os.remove(arquivos.path)
#    if not arquivos.is_file():
#        os.rmdir(arquivos.path)

# LIB send2trash para enviar para lixeira (dir/files)
# para usar precisa atualizar o lsb-core da maquina
# sudo apt-get install lsb-core

# TRABALHANDO COM ARQUIVOS E DIRETORIOS TEMPORARIOS
import tempfile

#with tempfile.TemporaryDirectory() as dir_temp:
#    print(f'Criei o diretorio temporario em {dir_temp}')
#    with open(os.path.join(dir_temp, 'arquivo_temporario.txt'), 'w') as arquivo_temp:
#        arquivo_temp.write('Geek University\n')
#    input()

# ESTAMOS CRIANDO UM DIRETÓRIO TEMPORARIO
# ABRINDO O MESMO
# DENTRO DELE CRIANDO UM ARQUIVO E ESCREVENDO UM TEXTO
# INPUT APENAS PARA SEGURAR POIS O FIM DO WITH DELETA E FECHA OS MESMOS

# NÃO FUNCIONA NO WINDOWS, FUNCIONA DIFERENTE COM ARQUIVOS TEMPORARIOS


# CRIANDO ARQUIVOS TEMPORARIOS
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n') # ENTRADA SOMENTE DE BINARIO Bits
    tmp.seek(0)
    print(tmp.read())