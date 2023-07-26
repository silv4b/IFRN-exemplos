# HERANÇA

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade


class Menino(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
