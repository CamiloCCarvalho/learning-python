"""
DUVIDAS

    1- IMPORTANCIA OU NECESSIDADE DA IDE ESPECIFICA PYCHARM
    2- SE USADO VSCODE, COMO CRIAR A MESMA ESTRUTURA

    
    6- *PYTHON USA PASSAGEM POR VALOR OU REFERENCIA ? COMO SÃO AMBAS
        6.1- * https://acervolima.com/passe-por-referencia-vs-valor-em-python/
        6.2 - O QUE SÃO PKDs NO PYTHON ?
        6.3- PASSAGEM POR REFERÊNCIA DE OBJETO ?
    

    

    
    10- IMPORTS É COMO IMPORTAR O QUE JA ESTA INSTALADO VIA NPM NA NODE_MODULES EM JS?
        10.1 - POR QUE NÃO PRECISA INDICAR O CAMINHO DE ONDE ESTA IMPORTANDO ?
        

    
"""


"""
    RESOLVIDAS:
    
    8- solved
        lista = [1, 99, 50, 2, 1505, 27, 33, 1, 54, 99, 1]
        lista.sort() # não pode fazer dentro do print, pois não retorna nada, muda a original
    
    4- solved
    
    5- solved
        -> shallow copy - espelha mudança no original 
        -> deep copy - novo dado, não afeta o original
        
    9- DIFERENÇA DE USAR < is > e < == > FALTA DO < === >
        double equal -> == (checa os valores)
        is -> checa se os objs são os mesmos (similar a === triple equal)
    
    11- CURIOSIDADE: 
        dentro de print() se chamar uma função sem passar parenteses,
        ela devolve o endereço na memória ?
            -> Sim e não. Ele devolve uma representação, e esta sim contem o endereço
                porem poderia não trazer esta informação (não é intrinseco)
                
    7- O tipo <None> equivale ao Null de JS ?
        -> até onde percebi sim, é um Objeto que serve para representar o Nada
        
    3- ESCOPO É APENAS GLOBAL E LOCAL (LOCAL DEFINIDO POR BLOCO) ?
        -> TEM ESCOPOS:
            => usando a palavra reservada Global e a outra esqueci mas tem como controlar
            => uso de paranteses em alguns casos também define o escopo
"""
