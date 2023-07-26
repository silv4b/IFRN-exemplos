class Pai:
    cor_pele = 'branco'

    def __init__(self, nome):
        self.nome = nome
        pass

    def falar(self):
        print('estou falando')


class Filho(Pai):
    # Na herança, o método inicializador da classe Filho precisa chamar o método inicializador da classe que vai herdar, nesse caso, a classe Pai, através o método especial super(), que acessa a classe diretamente superior
    def __init__(self, nome):
        super().__init__(nome)


if __name__ == '__main__':
    f = Filho('Juan')

    # Acessando em Filho atributo público/herdado de Pai
    print(f.cor_pele)

    # Acessando em Filho método público/herdado de Pai
    f.falar()
