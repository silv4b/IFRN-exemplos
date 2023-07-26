class Pessoa:
    __nome = None

    def __init__(self):
        pass

    def set_nome(self, valor):
        self.__nome = valor

    def get_nome(self):
        return self.__nome

if __name__ == '__main__':
    p = Pessoa()
    p.set_nome('Bruno')
    print(p.get_nome())
    