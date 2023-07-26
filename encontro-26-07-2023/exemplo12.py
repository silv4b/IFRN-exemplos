class Escola:
    nome = None
    disc = []

    def set_nome(self, nome):
        pass

    def get_nome(self):
        pass

    def set_disc(self, disc: str):
        pass

    def listar_disc(self):
        pass


class Instituto(Escola):
    # atributo privado __nome
    __nome = None
    # setters e getters sobrecarregados aqui, mas que foram herdados de Escola

    # acessando atributo privado da classe Instituto
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    # acessando atributo público da classe Instituto, mas que foi herdado de Escola
    def set_disc(self, disc: str):
        self.disc.append(disc)   

    def listar_disc(self):
        for i in range(0, len(self.disc)):
            print(f'Disciplina: {self.disc[i]}')


if __name__ == '__main__':
    e = Instituto()

    # usando setter de nome
    e.set_nome('IFRN')

    # usando setter de disciplina várias vezes
    e.set_disc('PEOO')
    e.set_disc('Info. Básica')
    e.set_disc('Matemática')

    # usando método getter de nome pra recuperar o valor do atributo privado __nome
    print(f'Disciplinas da escola {e.get_nome()}')

    # listando as disciplinas
    e.listar_disc()
