"""_____ 6° DIA - 04/06/2023 (week 3 - total = 20)_____"""

"""
    DUNDER METHODS - MÉTODOS MAGICOS
    
    OBS: ESSES METODOS SÃO DA CLASSE < object >
    
    1 __init__ 
        -> ja vimos
    
    2- __repr__ 
        -> pega a representação comum <objType - memoryReferencef125x13514f>
        -> muda para o que vc quer, faz override do metodo dentro da sua classe
        exemplo:
        class MyClass:
            __repr__(self):
                return f'overriding method'
    
    3- __str__(self):
        -> pega a representação igual o __repr__ porem ja devolve string
        exemplo:
            __str__(self):
                return self.__my_attribute
    
    4- __del__(self):
        return print("sobreescreve o metodo de deletar, podendo dar feedback")
        
    5- __add__(self, other):
        return f'{self} - {other}'
            # neste estamos mudando o comportamento padrão do print por exemplo:
                print(obj + obj) => fazendo ele "concatenar" os objetos.
                
                OBS: PARA FUNCIONAR PRECISA FAZER OVERRIDE DOS METODOS:
                    __repr__ ou __str__ para devolver string
                    
    6- __len__(self):
        return self.__my_attribute
    
    7- __mul__
        -> referente ao sinal de multiplicação
        exemplo:
            -> print(obj * 3)
                => __mul__(self, other):
                    if isinstance(other, int):
                    msg = ''
                    for n in range(other):
                        msg += ' ' + str(self)
                    return msg
                return 'Não é possivel multiplicar'
            
            --> resumindo: Se for String o que vier em self, o Other sendo int multiplica a string
                lembrando a base para funcionar é alterar __repr__ ou __str__ para mudar o valor
                retornado no  SELF 
"""
