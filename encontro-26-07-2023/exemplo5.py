class Pessoa:
    __nome = None

    def __init__(self):
        pass

    # setter -> atribuição
    def set_nome(self, valor: str):
        self.__nome = valor

    # getter -> retorno
    def get_nome(self):
        return self.__nome


if __name__ == '__main__':
    pessoa = Pessoa()
    # Usando método Setter para definir o valor de um atributo (privado) da classe
    pessoa.set_nome('Bruno')

    # Usando método Getter para recuperar o valor de um atributo (privado) da classe
    print(pessoa.get_nome())
