"""_____ 2° DIA - 24/05/2023 (week 2 - total = 9)_____"""

"""
    ATIPICO
        -> Devido a imprevisto Udemy
        -> Estudo de POO - Python
"""

# CLASSES
    # Classes são uma forma de "modelar" determinadas variaveis e funções agrupando-as em um conjunto pré-estabelecido, formando um novo contexto de uso.
    # Também permite inumeras melhorias de codigo, no que diz respeito a limitações de acesso, uso, e escopo para definir, e separar tarefas e demais quesitos.
    
class Carro:
    
    numero_rodas = 4 # equal in each instance of this class
    
    # similar constructor in JS
    def __init__(self, nome, marca, preco, esta_ligado=False) -> None:
        self.nome = nome
        self.__marca = marca # atribute private
        self.preco = preco
        self.esta_ligado = esta_ligado
        
    def ligar(self) -> str:
        if self.esta_ligado == False:
            self.esta_ligado = True
            return print(f"Seu {self.nome} esta Ligando...")
        else:
            return print(f"Seu {self.nome} já esta Ligado")
        
    def desligar(self) -> str: 
        if self.esta_ligado == True:
            self.esta_ligado = False
            return print(f"Seu {self.nome} esta Desligando...")
        else:
            return print(f"Seu {self.nome} já esta Desligado")
        
    def mostra_marca(self) -> str: # more security to acess atribute private
        return self.__marca
        
primeiroCarro = Carro('Gol', 'VolksWagen', 70000)
print(primeiroCarro.mostra_marca())


# primeiroCarro.__marca  -> not exist in context of instance, just in context Class Access
# self --> reference of the same instance of called
