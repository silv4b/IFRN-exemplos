class Pai:
    cor_pele = 'branco'

    def __init__(self, nome):
        self.nome = nome
        pass

    def falar(self):
        print('estou falando')


class Filho(Pai):

    def __init__(self, nome):
        super().__init__(nome)


if __name__ == '__main__':
    f = Filho('Juan')

    print(f.cor_pele)
    f.falar()
