"""_____ 3° DIA - 01/06/2023 (week 3 - total = 17)_____"""
""" 
 CUSTOM ITERATOR

"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


for n in Contador(5, 20):
    print(n)
