class Animal:
    def __init__(self, nome):
        self.__nome = nome

    # Método criando na classe Animal e posteriormente sobrecarregado na classe Gato, para ter um comportamento diferente
    def comer(self):
        print(f'{self.__nome} está comendo')


class Gato(Animal):
    def __init__(self, nome):
        # super().__init__(nome)
        self.__nome = nome

    # sobrecarga - overload - sobrescrita - overwrite
    # Sobrecarga/Sobrescrita do método comer() que foi criado na classe Animal
    # Aqui ele terá uma lógica diferente
    def comer(self):
        print(f'O gatinho {self.__nome} está comendo')


if __name__ == '__main__':
    gato = Gato('Tom')

    # Acessando método sobrecarregado
    gato.comer()
