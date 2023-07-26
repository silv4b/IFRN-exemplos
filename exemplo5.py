class Pessoa:
    __nome = None

    def __init__(self):
        pass

    # setter -> atribuição
    def set_nome(self, valor: str):
        self.__nome = valor

    # getters -> retorno
    def get_nome(self):
        return self.__nome


if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.set_nome('Bruno')
    print(pessoa.get_nome())
