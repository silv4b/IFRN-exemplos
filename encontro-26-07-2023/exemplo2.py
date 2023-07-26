# HERANÇA MÚLTIPLA

class Mae:
    def cor_olho(self):
        print('Olhos verdes da mãe')


class Pai:
    def tom_voz(self):
        print('Voz grave do pai')


class Filho(Pai, Mae):
    # SOBRESCRITA DE MÉTODO HERDADO
    def cor_olho(self):
        print('Olhos verdes castanhos do filho')

    def tom_voz(self):
        print('Tom menos grave do filho')


if __name__ == "__main__":
    c = Filho()

    c.cor_olho()
    c.tom_voz()
