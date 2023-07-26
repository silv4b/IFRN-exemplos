class Animal:
    def __init__(self, nome):
        self.__nome = nome

    # Esse método poderá ser acessado em qualquer classe que usar essa classe em herança
    def comer(self):
        # atributo __nome só pode ser usando dentro da classe Animal
        print(f'{self.__nome} está comendo')

class Gato(Animal):
    def __init__(self, nome): 
        super().__init__(nome)

if __name__ == '__main__':
    g = Gato('Snow Bell')

    # acessando em Gato, um método herdado que existe em Animal
    g.comer()
