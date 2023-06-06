"""_____ 7° DIA - 05/06/2023 (week 3 - total = 21)_____"""

"""
    É POSSIVEL SIMPLIFICAR O DEBUG VIA FSTRING
        -> EXEMPLO:
            => geek: str = 'Geek University'
            => print(f'{geek=}')
"""

nome: str = 'May Shiranui'
print(f"nome='{nome}'")

print(f'{nome=}')

# MAIS COMPLEXO
print(f'{nome.upper()[::-1] =}')