class Pai:
    def falar(self):
        print('Pai fala')

class Mae:
    def olhar(self):
        print('Mae olha')

class Filho(Pai, Mae):
    pass

if __name__ == '__main__':
    f = Filho()
    f.falar()
    f.olhar()
