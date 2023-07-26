class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo')


class Gato(Animal):
    def __init__(self, nome):
        # super().__init__(nome)
        self.__nome = nome

    # sobrecarga - overload - sobrescrita - overwrite
    def comer(self):
        print(f'O gatinho {self.__nome} está comendo')


if __name__ == '__main__':
    gato = Gato('Tom')

    gato.comer()
