class Pessoa:
    __nome = None

    def __init__(self):
        pass

    # setter -> atribuição
    def set_nome(self, valor):
        # atributo __nome recebe o valor da variável valor
        self.__nome = valor

    # getter -> retorno
    def get_nome(self):
        # retornando o valor do atributo privado __nome
        return self.__nome

if __name__ == '__main__':
    p = Pessoa()

    # atribuição de valor
    p.set_nome('Bruno')

    # retornando o valor
    print(p.get_nome())
    