"""_____ 4° DIA - 01/06/2023 (week 3 - total = 18)_____"""

"""
    POO - PYTHON - MULTIPARADIGMA
    
    1 METODO INIT
        __init__ -> metodo construtor (similar a constructor JS)
    
    2 PROPRIEDADE DICT    
        obj.__dict__ -> devolve as propriedades do objeto
    
    3 EXPLICAÇÃO
        __variable -> variavel privada
        __method -> metodo privado
    
    4 DUNDER
        __NO INICIO E FIM__
        
        NÃO É DUNDER O DE BAIXO
        __ -> representa o privado similar ao Java (conhecido como Name Mangling)
        cria uma forma de acessar coisas privadas
            obj._ClassName__AttributePrivate
    
    5 SELF
        self -> representa o proprio obj (similar ao this do JS)
    
    6 INSTÂNCIA
        instância -> obj criado da Classe em questão
    
    
    7 ATRIBUTOS ESTATICOS (DE CLASSE):
        Em memoria é separado apenas 1 unico espaço para alocação
        Diferente de Atributos de instancia que é separado um espaço para alocação
        de cada instância.
        
        
    8 ATRIBUTOS DINÂMICOS (CRIADO EM TEMPO DE EXECUÇÃO)
        - sera exclusivo da instancia que o cria, demais objs não vão ter
        
        
    9 METODO PRIVADO:
        def __my_method(self, things):
            # do anything
        
        geralmente usado pela propria classe para fazer algo
        
        
    10 METODO ESTATICO:
        @staticmethod
        def methodo():
            # do anything
        
        não recebe cls nem self
        
        
    11 GETTERS E SETTERS
        GETTERS:
            @property
            def name_method(self):
                # do anything
        
        SETTERS:
            @name_method.setter
            def name_method(self, new_var):
                self.__old_var = new_var
                
                
    12 HERANÇA:
        class Pessoa:
            def __init__(self, nome, idade)
            self.__nome = nome
            self.__idade = idade
            
        
        class Funcionario(Pessoa):
            def __init__(self, nome, idade, matricula)
            
            super().__init__(nome, idade)
            # ou
            Pessoa.__init__(self, nome, idade)
            
            self.__matricula = matricula
            
            
    13 POlIMORFISMO: ( similar @override de android, reescrevendo-os)
        só escrever denovo a função na classe filha
        
        -> caso queira deixa a parte de cada classe filha:
            class Pai:
                # do anything
                def method(self):
                    raise NotImplementedError('classe filha precisa implements')
            
            class Filha:
                # do anything
                def method(self):
                    # implements here! note: This is the same method above
        
        
    14 METODOS ABSTRATOS NO PYTHON:
        -> são estes igual exemplificado acima para deixar a classe filha
           implementalos para usar polimorfismo.
                
    
    15 METODO COMO PROPRIEDADE
        @property
        def my_func(self, anything)
            # do anything
            
        chamada:
            obj.my_func 
            
            OBS.: CHAMA A FUNÇÃO IGUAL ATRIBUTO, PARECE METODO ESTATICO DO JS
    
        
    16 MRO - METHOD RESOLUTION ORDER (ORDEM DE RESOLUÇÃO DE METODOS)
        -> CASO:
            Com multiploas heranças e polimorfismos de metodos
            pode existir uma mudança na decisão de qual metodo acionar se houver
            mais de um disponivel
            exemplo:
                class Pinguim(Terrestre, Aquatico):
                    # imagine que ambas classe super tem metodos para
                    mostrar que o bixo é da terra ou da agua
                    nesse caso Pinguim ira executar o que veio primeiro nos parametros
                    
            RESOLUTION: 
                -> via propriedade: __mro__
                -> via method: mro()
                -> via help
                
                -> USANDO MRO
                from mro import Pinguim
                    => Pinguim.__mro__
            
    
    17 CURIOSIDADES:
        PASSLIB - CRIPTOGRAFIA DE SENHA
            pip install passlib
        
        COMANDO exit(number) # força parada do programa antes de termina as linhas
            exit(1)
"""


from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:
    # Atributos de classe (similar a estaticos em JAVA)
    imposto = 1.05 # 5%
    contador = 0

    @classmethod # METODO DE CLASSE
    def conta_lampadas(cls): # cls É A PROPRIA CLASSE PASSA SOZINHA IGUAL SELF
        print(f'Temos {cls.contador} lampadas criadas')
    @staticmethod # METODO ESTATICO
    def codigo_produto():
        return print('Prudoto codigo: 45FD369A')

    def __init__(self, voltagem, cor, valor, senha): # METODO DE INSTÂNCIA
        self.__id = Lampada.contador + 1 # ATRIBUTO DE INSTÂNCIA
        self.__voltagem = voltagem
        self.__cor = cor
        self.ligada = False
        self.__valor = (valor * Lampada.imposto)
        self.__desconto = 0
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Lampada.contador = self.__id

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def desconto(self, porcentagem): # acesso: Class.desconto(obj, 10)
        """Retorna o valor do produto com desconto."""
        self.__desconto = self.__gera_desconto() * ((100 - porcentagem)/100)
        return (self.__valor * (100 - porcentagem)) / 100

    def __gera_desconto(self): # METODO PRIVADO
        return self.__valor


lamp1 = Lampada(110, 'blue', 5000, '123456')
lamp2 = Lampada(220, 'red', 6000, '4a450f11')
print(f'lampada 1 id: {lamp1._Lampada__id}')
print(f'lampada 2 id: {lamp2._Lampada__id}')

print(lamp1.ligada) # return False (attr public)
# print(lamp1.__cor) # AttributeError: (because it's private)

# DETALHE
print(dir(lamp1)) # '_Lampada__cor'
print(lamp1._Lampada__cor) # 'blue' (access by class, low security)
print(lamp1._Lampada__valor) # 5250.0

# FORMA CORRETA DE ACESSAR ATRIBUTO DE CLASSE
print(Lampada.imposto)

# ATRIBUTO DINÂMICO - CRIADO EM TEMPO DE EXECUÇÃO
lamp2.peso = '102g'
print(lamp2.__dict__) # ver propriedades

# DELETANDO ATRIBUTOS DINÂMICAMENTE
del lamp2.peso
# print(lamp2.peso)

# ERRADO
# print(Lampada.desconto(40))

# CERTO
print(lamp2.desconto(40))

# POREM
print(Lampada.desconto(lamp2, 50)) # NÃO RECOMENDADO

print(lamp1._Lampada__senha)
print(lamp2._Lampada__senha)

# METODO DE CLASSE (metodo estatico, geralmente não precisa acessar nada da instância)
Lampada.conta_lampadas()

# POSSIVEL MAIS INCORRETO
lamp2.conta_lampadas()
