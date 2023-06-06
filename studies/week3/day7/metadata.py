"""_____ 7° DIA - 05/06/2023 (week 3 - total = 21)_____"""

"""
    METADATA
        -> Tem pacote para ver metadata, versão entre outros detalhes...
"""

from importlib import metadata

print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip') # tipo Dict
print(list(metadados_pip)) # List

print(metadados_pip['Project-URL'])

# quantor arquivos tem neste versão do pip
print(len(metadata.files('pip')))

# o que precisa pra instalar o pip?
print(metadata.requires('pip'))
