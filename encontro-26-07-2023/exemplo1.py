# HERANÇA

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

# MENINO HERDANDO DE PESSOA
class Menino(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
