class Pai:
    nome_pai = "Roberto Carlos"

    def falar(self):
        print('Pai fala')


class Mae:
    nome_mae = "Mara Maravilha"

    def olhar(self):
        print('Mae olha')

# classe Filho herdando atributos e métodos das classes Pai e Mae


class Filho(Pai, Mae):
    pass


if __name__ == '__main__':
    f = Filho()

    # acessando método herdado de Pai, na classe Filho
    f.falar()

    # acessando método sobrescrito mas que inicialmente foi herdado de Pai, na classe Filho
    f.olhar()

    # acessando atributo na classe Filho, mas que foi herdado da classe Pai
    print(f'Nome da pai: {f.nome_pai}')

    # acessando atributo na classe Filho, mas que foi herdado da classe Mae
    print(f'Nome do mãe: {f.nome_mae}')
