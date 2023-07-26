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
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_disc(self, disc: str):
        self.disc.append(disc)
        
    def listar_disc(self):
        for i in range(0, len(self.disc)):
            print(f'Disci: {self.disc[i]}')


if __name__ == '__main__':
    e = Instituto()
    e.set_nome('IFRN')
    e.set_disc('PEOO')
    e.set_disc('Info. Básica')
    e.set_disc('Matemática')
    print(f'Disciplinas da escola {e.get_nome()}')
    e.listar_disc()
